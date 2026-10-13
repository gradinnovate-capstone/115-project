'use strict';
const modules = [...document.querySelectorAll('.module')];
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
