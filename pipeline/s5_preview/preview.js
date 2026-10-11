// preview.js — 自写 URDF→three 场景加载器（B6 退路，依赖受阻后启用，决策记 AGENT-LAB）
// 边界（PIPELINE §3-S5 / B6）：本文件只做 URDF XML 解析 + 坐标变换 + 关节交互；
// DAE 解析用官方 ColladaLoader（vendor 于 libs/，随附原版 MIT LICENSE——修正 3）。
// 模型读取的就是 models/ 入库文件（相对路径 ../../models/…，可核对）。

import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { ColladaLoader } from 'three/addons/loaders/ColladaLoader.js';

const URDF_URL = '../../models/unitree_go2/urdf/go2_description.urdf';
const MESH_BASE = '../../models/unitree_go2/urdf_meshes/'; // package://go2_description/X → MESH_BASE + X
const PKG_PREFIX = 'package://go2_description/';

const meta = document.getElementById('meta');
const net = document.getElementById('net');
const status = document.getElementById('status');

// ---- URDF 解析（B6 边界内） ----
const num3 = s => (s ?? '0 0 0').trim().split(/\s+/).map(Number);
// URDF rpy = Rz(yaw)·Ry(pitch)·Rx(roll) → three Euler('ZYX') 且分量 x=roll,y=pitch,z=yaw
const rpyQuat = ([r, p, y]) =>
  new THREE.Quaternion().setFromEuler(new THREE.Euler(r, p, y, 'ZYX'));
function originOf(el) {
  const o = el ? el.querySelector(':scope > origin') : null;
  return { pos: new THREE.Vector3(...num3(o?.getAttribute('xyz'))),
           quat: rpyQuat(num3(o?.getAttribute('rpy'))) };
}

const text = await fetch(URDF_URL).then(r => r.text());
const xml = new DOMParser().parseFromString(text, 'text/xml');
const linkEls = [...xml.querySelectorAll('link')];
const jointEls = [...xml.querySelectorAll('joint')];

// ---- three 场景 ----
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(innerWidth, innerHeight);
document.getElementById('app').appendChild(renderer.domElement);
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x101418);
const camera = new THREE.PerspectiveCamera(50, innerWidth / innerHeight, 0.01, 50);
camera.position.set(1.5, 1.0, 1.6);
const controls = new OrbitControls(camera, renderer.domElement);
controls.target.set(0, 0.25, 0);
scene.add(new THREE.HemisphereLight(0xffffff, 0x223344, 1.15));
const sun = new THREE.DirectionalLight(0xffffff, 1.6);
sun.position.set(2, 4, 2);
scene.add(sun);
scene.add(new THREE.GridHelper(4, 20, 0x334455, 0x22303c));

// ---- 连杆树：joint origin 定 child 位姿，visual origin 定网格位姿 ----
const groups = new Map(linkEls.map(l => [l.getAttribute('name'), new THREE.Group()]));
const childNames = new Set([...jointEls].map(j => j.querySelector('child').getAttribute('link')));
const rootName = linkEls.map(l => l.getAttribute('name')).filter(n => !childNames.has(n))[0];
const model = new THREE.Group();
model.add(groups.get(rootName));
model.rotation.x = -Math.PI / 2; // URDF 是 Z-up，three 是 Y-up：绕 X 转 -90° 把机身立起来
scene.add(model);

for (const j of jointEls) {
  const pg = groups.get(j.querySelector('parent').getAttribute('link'));
  const cg = groups.get(j.querySelector('child').getAttribute('link'));
  const o = originOf(j);
  cg.position.copy(o.pos);
  cg.quaternion.copy(o.quat);
  pg.add(cg);
}

const daeLoader = new ColladaLoader();
const jobs = [];
let meshCount = 0;
for (const link of linkEls) {
  const g = groups.get(link.getAttribute('name'));
  for (const vis of link.querySelectorAll('visual')) {
    const meshEl = vis.querySelector('geometry > mesh');
    if (!meshEl) continue;
    const uri = meshEl.getAttribute('filename') ?? '';
    if (!uri.startsWith(PKG_PREFIX)) {
      status.textContent += `非本包网格引用：${uri}\n`;
      continue;
    }
    const url = MESH_BASE + uri.slice(PKG_PREFIX.length);
    const vOrigin = originOf(vis);
    jobs.push(new Promise(res => daeLoader.load(url, collada => {
      const obj = collada.scene;
      obj.position.copy(vOrigin.pos);
      obj.quaternion.copy(vOrigin.quat);
      g.add(obj);
      meshCount += 1;
      res();
    }, undefined, () => { status.textContent += `网格加载失败：${url}\n`; res(); })));
  }
}
await Promise.all(jobs);

// 落地对齐：URDF base 原点在髋部、足端在 z≈-0.32，Z-up 转换后足端 y<0 会沉到网格下——
// 按包围盒把整机抬到足端贴网格面，相机目标对准几何中心
const bbox = new THREE.Box3().setFromObject(model);
const lift = -bbox.min.y;
model.position.y += lift;
bbox.min.y += lift;
bbox.max.y += lift;
const center = bbox.getCenter(new THREE.Vector3());
controls.target.set(0, center.y, 0);

// ---- 关节滑条（质检元素：滑条范围比 URDF 限位宽 0.4rad，越限变红） ----
const sliderBox = document.getElementById('sliders');
const revolute = jointEls.filter(j => j.getAttribute('type') === 'revolute');
for (const j of revolute) {
  const name = j.getAttribute('name');
  const axis = new THREE.Vector3(...num3(j.querySelector('axis')?.getAttribute('xyz')));
  const lim = j.querySelector('limit');
  const lo = parseFloat(lim?.getAttribute('lower') ?? '-3.14');
  const hi = parseFloat(lim?.getAttribute('upper') ?? '3.14');
  const g = groups.get(j.querySelector('child').getAttribute('link'));
  const q0 = g.quaternion.clone();
  // 初值：0 在限位内取 0，否则取限位中点（calf 的 URDF 限位 [-2.72,-0.84] 不含 0，零位非法）
  const init = (0 >= lo && 0 <= hi) ? 0 : (lo + hi) / 2;
  const row = document.createElement('div');
  row.className = 'joint';
  row.innerHTML = `<label><span>${name}</span><span class="val"></span></label>
    <input type="range" min="${(lo - 0.4).toFixed(2)}" max="${(hi + 0.4).toFixed(2)}" step="0.01" value="${init.toFixed(2)}">`;
  const input = row.querySelector('input');
  const val = row.querySelector('.val');
  const apply = () => {
    const th = parseFloat(input.value);
    val.textContent = `${th.toFixed(2)} rad`;
    row.classList.toggle('over', th < lo || th > hi);
    g.quaternion.copy(q0).multiply(new THREE.Quaternion().setFromAxisAngle(axis, th));
  };
  input.addEventListener('input', apply);
  apply();
  sliderBox.appendChild(row);
}

// ---- 断网自检（质检动作本身上屏） ----
setTimeout(() => {
  const res = performance.getEntriesByType('resource');
  const ext = res.filter(e => !e.name.startsWith(location.origin)).length;
  net.innerHTML = ext === 0
    ? `<span class="ok">断网自检：${res.length} 个资源全部本机，外网请求 0 ✓</span>`
    : `<span class="bad">断网自检：发现 ${ext} 个外网请求！</span>`;
}, 800);

meta.innerHTML =
  `links ${linkEls.length} · joints ${jointEls.length}（revolute ${revolute.length}）· visual 网格 ${meshCount}<br>` +
  `根 link：<b>${rootName}</b> · 源：${URDF_URL}`;
status.textContent = '拖动旋转 / 滚轮缩放 / 滑条动关节（越 URDF 限位标红）';

addEventListener('resize', () => {
  camera.aspect = innerWidth / innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(innerWidth, innerHeight);
});
renderer.setAnimationLoop(() => renderer.render(scene, camera));
