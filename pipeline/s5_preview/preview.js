// preview.js — 自写 URDF→three 场景加载器（B6 退路，依赖受阻后启用，决策记 AGENT-LAB）
// 边界（PIPELINE §3-S5 / B6）：本文件只做 URDF XML 解析 + 坐标变换 + 关节交互；
// DAE 解析用官方 ColladaLoader、STL 用官方 STLLoader（均 vendor 于 libs/，随附原版 MIT LICENSE——修正 3/R10-⑤）。
// 模型读取的就是 models/ 入库文件（相对路径 ../../models/…，可核对）。
// v4（R10-⑤ STL 支路）：模型无关化——?model=<name> 读 pipeline/configs/<name>.json 驱动，
// 入库路径/引用协议（package:// ∥ relative）全按 config；M2+ 加模型预览零改码。

import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { ColladaLoader } from 'three/addons/loaders/ColladaLoader.js';
import { STLLoader } from 'three/addons/loaders/STLLoader.js';

const MODEL_NAME = new URLSearchParams(location.search).get('model') ?? 'unitree_go2';
const pageTitle = document.getElementById('page-title'); // 旧缓存 html 无此 id，兜底不崩
if (pageTitle) pageTitle.textContent = `${MODEL_NAME} · 质检预览`;
document.title = `${MODEL_NAME} — 仿真模型质检预览（cn-robot-models）`;
const MODEL_BASE = `../../models/${MODEL_NAME}/`;
const CONFIG_URL = `../../pipeline/configs/${MODEL_NAME}.json`;

const meta = document.getElementById('meta');
const net = document.getElementById('net');
const status = document.getElementById('status');

// ---- config 驱动（与管道同一份真源） ----
const config = await fetch(CONFIG_URL).then(r => r.json());
const s2 = config.s2;
const URDF_URL = MODEL_BASE + config.s4.urdf[0].dest; // 入库路径按 s4 对账表，不重推
const urdfDir = URDF_URL.slice(0, URDF_URL.lastIndexOf('/') + 1);
const refStyle = s2.urdf.ref_style ?? 'package';
const pkgPrefix = `package://${s2.urdf.package}/`;

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
// 视口按体型粗调（仅观感参数，不影响几何）：v5 起 config s5.viewport 驱动；
// unitree_g1 为 v4 时代先例，无 s5 段，回退按人形保持兼容（X2 起新模型一律 config 声明）
const isHumanoid = config.s5?.viewport === 'humanoid' || config.model === 'unitree_g1';
camera.position.set(...(isHumanoid ? [2.2, 1.4, 2.4] : [1.5, 1.0, 1.6]));
const controls = new OrbitControls(camera, renderer.domElement);
controls.target.set(0, isHumanoid ? 0.7 : 0.25, 0);
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

// ---- 连杆挂接：joint origin 把 child group 挂进 parent group（v4 重写时曾整段丢失，
//      症状 = 只渲染根 link 网格、包围盒塌缩到单件尺寸；L10 记档） ----
for (const j of jointEls) {
  const pg = groups.get(j.querySelector('parent').getAttribute('link'));
  const cg = groups.get(j.querySelector('child').getAttribute('link'));
  const o = originOf(j);
  cg.position.copy(o.pos);
  cg.quaternion.copy(o.quat);
  pg.add(cg);
}

// ---- 网格加载：按扩展名分流；STL 无 UV/材质 → 统一中性着色（格式天性，如实标注不伪装） ----
const daeLoader = new ColladaLoader();
const stlLoader = new STLLoader();
// DoubleSide（R19）：负 scale 镜像（lite3 hip/thigh `1 -1 1` 等）翻转三角形绕向，
// FrontSide 会让镜像腿内翻缺面；闭合实体背面本就被深度测试遮挡，双面渲染零观感代价
const STL_MATERIAL = new THREE.MeshStandardMaterial({
  color: 0x8d99a6, metalness: 0.15, roughness: 0.55,
  side: THREE.DoubleSide,
});
const jobs = [];
let meshCount = 0;
const stlUrls = new Set();  // 唯一 URL 计数（引用 13 处可能是 4 物理件复用——Lite3 实测）
let loadFail = 0;
for (const link of linkEls) {
  const g = groups.get(link.getAttribute('name'));
  for (const vis of link.querySelectorAll('visual')) {
    const meshEl = vis.querySelector('geometry > mesh');
    if (!meshEl) continue;
    const uri = meshEl.getAttribute('filename') ?? '';
    // URDF <mesh scale="sx sy sz">（R18-L12）：忽略此属性会把缩放网格按原生尺寸渲染——
    // X2 徽标件 native 3.96 m，上游两格式同 scale 收为 12 cm；解析器沉默 ≠ 文件事实
    const scaleAttr = meshEl.getAttribute('scale');
    let url;
    if (refStyle === 'relative') {
      // G1 协议：uri 相对 URDF 自身目录（入库保持 meshes/ 与 urdf 同目录）
      url = urdfDir + uri;
    } else {
      if (!uri.startsWith(pkgPrefix)) {
        status.textContent += `非本包网格引用：${uri}\n`;
        continue;
      }
      url = `${MODEL_BASE}urdf_meshes/${uri.slice(pkgPrefix.length)}`;
    }
    const ext = (url.split('?')[0].split('.').pop() ?? '').toLowerCase();
    const vOrigin = originOf(vis);
    jobs.push(new Promise(res => {
      const done = obj => {
        obj.position.copy(vOrigin.pos);
        obj.quaternion.copy(vOrigin.quat);
        if (scaleAttr) obj.scale.set(...num3(scaleAttr));
        g.add(obj);
        meshCount += 1;
        res();
      };
      const fail = () => { status.textContent += `网格加载失败：${url}\n`; loadFail += 1; res(); };
      if (ext === 'stl') {
        stlUrls.add(url);
        stlLoader.load(url, geom => {
          done(new THREE.Mesh(geom, STL_MATERIAL));
        }, undefined, fail);
      } else {
        daeLoader.load(url, collada => done(collada.scene), undefined, fail);
      }
    }));
  }
}
await Promise.all(jobs);

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

// 落地对齐 v3：放在滑条初始化之后（初始蹲姿才算数），且测量前强制刷新世界矩阵——
// 初次渲染前父级 matrixWorld 是陈旧值，bbox 会算错（L5 真根因）；只按可见网格，排除灯/空节点
model.updateMatrixWorld(true);
const bbox = new THREE.Box3();
model.traverse(o => { if (o.isMesh) bbox.expandByObject(o); });
const lift = -bbox.min.y;
model.position.y += lift;
bbox.min.y += lift;
bbox.max.y += lift;
const center = bbox.getCenter(new THREE.Vector3());
controls.target.set(0, center.y, 0);
window.__preview = { model, scene, camera, bbox }; // 调试钩子

// ---- 断网自检（质检动作本身上屏） ----
setTimeout(() => {
  const res = performance.getEntriesByType('resource');
  const ext = res.filter(e => !e.name.startsWith(location.origin)).length;
  net.innerHTML = ext === 0
    ? `<span class="ok">断网自检：${res.length} 个资源全部本机，外网请求 0 ✓</span>`
    : `<span class="bad">断网自检：发现 ${ext} 个外网请求！</span>`;
}, 800);

const stlNote = stlUrls.size > 0
  ? ` · <span class="ok">STL ${stlUrls.size} 件（物理文件）统一中性着色——无 UV/材质为格式天性，非上游外观</span>`
  : '';
meta.innerHTML =
  `<b>${config.model}</b> · links ${linkEls.length} · joints ${jointEls.length}（revolute ${revolute.length}）· visual 网格 ${meshCount}${stlNote}<br>` +
  `根 link：<b>${rootName}</b> · 源：${URDF_URL} · 引用协议 ${refStyle}<br>` +
  `<span class="ok">载入版本 v4（config 驱动）</span> · 落地抬升 ${lift.toFixed(3)} m · ` +
  `包围盒 y [${bbox.min.y.toFixed(3)}, ${bbox.max.y.toFixed(3)}]` +
  (loadFail ? ` · <span class="bad">加载失败 ${loadFail} 件</span>` : '');
status.textContent = '拖动旋转 / 滚轮缩放 / 滑条动关节（越 URDF 限位标红）';

addEventListener('resize', () => {
  camera.aspect = innerWidth / innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(innerWidth, innerHeight);
});
renderer.setAnimationLoop(() => renderer.render(scene, camera));
