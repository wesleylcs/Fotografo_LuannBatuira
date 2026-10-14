(() => {
  'use strict';
  // Preencha com os IDs reais. Enquanto tiverem "XXXX", nada é carregado.
  const GTM_ID = 'GTM-XXXXXXX';
  const GA_ID = 'G-XXXXXXXXXX';

  const ok = (id) => id && !/X{4}/.test(id);
  const w = window;
  w.dataLayer = w.dataLayer || [];
  w.gtag = function () { w.dataLayer.push(arguments); };

  const load = (src) => {
    const s = document.createElement('script');
    s.async = true;
    s.src = src;
    document.head.appendChild(s);
  };

  let started = false;
  const start = () => {
    if (started) return;
    started = true;
    if (ok(GTM_ID)) {
      w.dataLayer.push({ 'gtm.start': Date.now(), event: 'gtm.js' });
      load('https://www.googletagmanager.com/gtm.js?id=' + GTM_ID);
    }
    if (ok(GA_ID)) {
      w.gtag('js', new Date());
      w.gtag('config', GA_ID);
      load('https://www.googletagmanager.com/gtag/js?id=' + GA_ID);
    }
  };

  // Carrega depois da página pronta (ou na 1ª interação) para não pesar no desempenho.
  const later = () => ('requestIdleCallback' in w ? w.requestIdleCallback(start, { timeout: 4000 }) : setTimeout(start, 2000));
  ['pointerdown', 'keydown', 'scroll', 'touchstart'].forEach((e) => w.addEventListener(e, start, { once: true, passive: true }));
  document.readyState === 'complete' ? later() : w.addEventListener('load', later);
})();
