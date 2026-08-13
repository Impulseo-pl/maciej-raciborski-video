/* ============================================================
   EKRAN WEJŚCIA — sterowanie. Skrypt siedzi w <head> BEZ defer:
   z defer przez ułamek sekundy widać stronę, a potem kurtynę — wygląda jak błąd.

   Całość poniżej 1,2 s. Gra raz na wizytę (sessionStorage).
   `?intro` w adresie = zagraj ponownie (do pokazywania klientowi).
   ============================================================ */
(function () {
  'use strict';
  try {
    var html = document.documentElement;
    var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion:reduce)').matches;
    var wymus = /[?&]intro\b/.test(location.search);
    var stop = /[?&]intro=stop/.test(location.search);   // kurtyna zostaje w kadrze (do oglądania)
    var bylo = false;
    try { bylo = sessionStorage.getItem('mr-wejscie') === '1'; } catch (e) {}

    if (reduce || (bylo && !wymus)) return;
    try { sessionStorage.setItem('mr-wejscie', '1'); } catch (e) {}

    html.classList.add('wejscie-gra');

    var zdjete = false;
    function zdejmij() {
      if (zdjete) return;
      zdjete = true;
      html.classList.add('wejscie-f2');
      setTimeout(function () {
        html.classList.remove('wejscie-gra', 'wejscie-f1', 'wejscie-f2');
      }, 640);
    }

    // BEZPIECZNIK: twardy limit - kurtyna schodzi niezależnie od wszystkiego
    var limit = stop ? 0 : setTimeout(zdejmij, 1600);

    // BEZPIECZNIK: dowolna reakcja użytkownika przerywa natychmiast
    ['click', 'touchstart', 'wheel', 'keydown'].forEach(function (ev) {
      addEventListener(ev, function przerwij() {
        removeEventListener(ev, przerwij);
        clearTimeout(limit);
        zdejmij();
      }, { passive: true, once: true });
    });

    function start() {
      var kadr = document.createElement('div');
      kadr.className = 'wejscie';
      kadr.setAttribute('aria-hidden', 'true');
      kadr.innerHTML =
        '<div class="wejscie__plyta wejscie__plyta--gora"></div>' +
        '<div class="wejscie__plyta wejscie__plyta--dol"></div>' +
        '<img class="wejscie__logo" src="' + (window.MR_BAZA || '') + 'media/logo.webp" alt="">' +
        '<span class="wejscie__kreska"></span>';
      document.body.appendChild(kadr);

      requestAnimationFrame(function () {
        html.classList.add('wejscie-f1');
        if (!stop) setTimeout(zdejmij, 560);   // 560 + 620 animacji = ok. 1,18 s
      });
    }

    if (document.body) start();
    else document.addEventListener('DOMContentLoaded', start, { once: true });
  } catch (e) {
    // przy jakimkolwiek błędzie strona ma wyglądać normalnie
    try { document.documentElement.classList.remove('wejscie-gra', 'wejscie-f1', 'wejscie-f2'); } catch (e2) {}
  }
})();
