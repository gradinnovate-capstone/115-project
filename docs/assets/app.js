'use strict';
const modules = [...document.querySelectorAll('.module')];
const checks = [...document.querySelectorAll('[data-complete]')];
const storageKey = 'gradinnovate-115-progress-v1';
let completed = new Set();
try {
  const stored = JSON.parse(localStorage.getItem(storageKey) || '[]');
  if (Array.isArray(stored)) completed = new Set(stored.filter(id => checks.some(c => c.dataset.complete === id)));
} catch { document.querySelector('#storage-note').textContent = '此瀏覽器無法讀取儲存進度，本次仍可使用。'; }
function updateProgress() {
  checks.forEach(c => { c.checked = completed.has(c.dataset.complete); });
  document.querySelector('#progress').value = completed.size;
  document.querySelector('#progress-count').textContent = `${completed.size} / ${checks.length}`;
}
function saveProgress() {
  try { localStorage.setItem(storageKey, JSON.stringify([...completed])); }
  catch { document.querySelector('#storage-note').textContent = '無法儲存進度；關閉頁面後可能遺失。'; }
  updateProgress();
}
checks.forEach(c => c.addEventListener('change', () => {
  if (c.checked) completed.add(c.dataset.complete); else completed.delete(c.dataset.complete);
  saveProgress();
}));
document.querySelector('#reset').addEventListener('click', () => { completed.clear(); saveProgress(); });
updateProgress();
let stage = '全部';
const search = document.querySelector('#search');
const filters = [...document.querySelectorAll('[data-filter]')];
function filterModules() {
  const query = search.value.trim().toLocaleLowerCase();
  let count = 0;
  modules.forEach(m => {
    m.hidden = !((stage === '全部' || m.dataset.stage === stage) && m.textContent.toLocaleLowerCase().includes(query));
    if (!m.hidden) count++;
  });
  document.querySelector('#empty').hidden = count !== 0;
  document.querySelector('#result-count').textContent = `顯示 ${count} 個單元`;
  filters.forEach(b => { const active = b.dataset.filter === stage; b.classList.toggle('active', active); b.setAttribute('aria-pressed', String(active)); });
}
search.addEventListener('input', filterModules);
filters.forEach(b => b.addEventListener('click', () => { stage = b.dataset.filter; filterModules(); }));
function revealHash() {
  const target = modules.find(m => '#' + m.id === location.hash);
  if (target) { stage = '全部'; search.value = ''; filterModules(); target.scrollIntoView(); }
}
window.addEventListener('hashchange', revealHash);
document.querySelectorAll('.module-nav a').forEach(a => a.addEventListener('click', () => { stage = '全部'; search.value = ''; filterModules(); }));
if (location.hash) revealHash();
function updateAttention() {
  const temp = Number(document.querySelector('#temperature').value);
  const masked = document.querySelector('#mask').checked;
  const exps = [2, 1, 0].map((x, i) => masked && i === 2 ? 0 : Math.exp((x - 2) / temp));
  const sum = exps.reduce((a,b) => a+b, 0);
  const weights = exps.map(x => x/sum);
  document.querySelector('#temp-output').textContent = temp.toFixed(1);
  weights.forEach((w,i) => {
    document.querySelector(`#bar-${i}`).style.width = `${w*100}%`;
    document.querySelector(`#weight-${i}`).textContent = `${(w*100).toFixed(1)}%`;
  });
  const value = weights.reduce((a,w,i) => a+w*(i+1)*10, 0);
  document.querySelector('#attention-result').textContent = `加權輸出 = ${value.toFixed(2)}${masked ? '；第三個位置權重為 0。' : '；權重總和 = 1。'}`;
}
document.querySelector('#temperature').addEventListener('input', updateAttention);
document.querySelector('#mask').addEventListener('change', updateAttention);
updateAttention();
