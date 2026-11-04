// Keep sliders and number boxes in sync; example-field buttons; crop guide filters.
document.querySelectorAll('input[type=range][data-for]').forEach(r => {
  const n = document.getElementById(r.dataset.for);
  const paint = () => r.style.setProperty('--fill', ((r.value - r.min) / (r.max - r.min) * 100) + '%');
  r.addEventListener('input', () => { n.value = r.value; paint(); });
  n.addEventListener('input', () => { if (n.value !== '') { r.value = n.value; paint(); } });
  paint();
});
document.querySelectorAll('#presets button').forEach(b => b.addEventListener('click', () => {
  const p = JSON.parse(b.dataset.p);
  Object.entries(p).forEach(([k, v]) => { const n = document.getElementById('id_' + k); n.value = v; n.dispatchEvent(new Event('input')); });
}));
const grid = document.getElementById('cropgrid');
if (grid) {
  const q = document.getElementById('q'), s = document.getElementById('season'), w = document.getElementById('water'), none = document.getElementById('none');
  const run = () => {
    let shown = 0;
    grid.querySelectorAll('.crop').forEach(c => {
      const ok = c.dataset.name.includes(q.value.trim().toLowerCase())
        && (!s.value || c.dataset.season.includes(s.value))
        && (!w.value || c.dataset.water.includes(w.value));
      c.hidden = !ok; shown += ok;
    });
    none.hidden = shown > 0;
  };
  [q, s, w].forEach(e => e.addEventListener('input', run));
}
// Eye button to show/hide password on every password field
const EYE = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-7 11-7 11 7 11 7-4 7-11 7S1 12 1 12z"/><circle cx="12" cy="12" r="3"/></svg>';
const EYE_OFF = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17.9 17.9A10.9 10.9 0 0 1 12 19C5 19 1 12 1 12a18.4 18.4 0 0 1 5.1-5.9M9.9 4.2A10.7 10.7 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.2 3.2M1 1l22 22"/></svg>';

document.querySelectorAll('input[type=password]').forEach(inp => {
  const wrap = document.createElement('div');
  wrap.className = 'pw';
  inp.parentNode.insertBefore(wrap, inp);
  wrap.appendChild(inp);

  const btn = document.createElement('button');
  btn.type = 'button';
  btn.className = 'pw-eye';
  btn.setAttribute('aria-label', 'Show password');
  btn.innerHTML = EYE;
  btn.addEventListener('click', () => {
    const show = inp.type === 'password';
    inp.type = show ? 'text' : 'password';
    btn.innerHTML = show ? EYE_OFF : EYE;
    btn.setAttribute('aria-label', show ? 'Hide password' : 'Show password');
  });
  wrap.appendChild(btn);
});