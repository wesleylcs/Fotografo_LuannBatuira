(() => {
  'use strict';
  const dlg = document.getElementById('lb');
  const img = document.getElementById('lb-img');
  const cap = document.getElementById('lb-cap');
  const items = [...document.querySelectorAll('.ph button[data-full]')];
  let current = 0;

  const year = document.getElementById('ano');
  if (year) year.textContent = new Date().getFullYear();

  if (!dlg || typeof dlg.showModal !== 'function' || !items.length) return;

  const show = (i) => {
    current = (i + items.length) % items.length;
    const b = items[current];
    img.src = b.dataset.full;
    img.width = b.dataset.w;
    img.height = b.dataset.h;
    img.alt = b.dataset.alt;
    cap.textContent = b.closest('figure').querySelector('figcaption').textContent;
  };

  items.forEach((b, i) => b.addEventListener('click', () => { show(i); dlg.showModal(); }));
  dlg.querySelector('.lb-close').addEventListener('click', () => dlg.close());
  dlg.querySelector('.lb-prev').addEventListener('click', () => show(current - 1));
  dlg.querySelector('.lb-next').addEventListener('click', () => show(current + 1));
  dlg.addEventListener('click', (e) => { if (e.target === dlg) dlg.close(); });
  dlg.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft') show(current - 1);
    else if (e.key === 'ArrowRight') show(current + 1);
  });
})();
