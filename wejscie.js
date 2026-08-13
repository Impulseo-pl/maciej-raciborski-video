/* ============================================================
   EKRAN WEJŚCIA „montaż" — sterowanie.
   Skrypt siedzi w <head> BEZ defer: z defer przez ułamek sekundy widać stronę,
   a dopiero potem kurtynę — wygląda jak błąd.

   Przebieg (razem ok. 1,5 s):
     0–520 ms   cztery kadry z realizacji przelatują po 130 ms (montaż)
     520–1000   podpis + kreska akcentu
     1000–1700  kadr rozsuwa się i odsłania stronę

   Gra raz na wizytę (sessionStorage).
   `?intro` = zagraj ponownie (do pokazywania), `?intro=stop` = zatrzymaj do oglądania.
   ============================================================ */
(function () {
  'use strict';
  try {
    var html = document.documentElement;
    var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion:reduce)').matches;
    var wymus = /[?&]intro\b/.test(location.search);
    var stop = /[?&]intro=stop/.test(location.search);
    var bylo = false;
    try { bylo = sessionStorage.getItem('mr-wejscie') === '1'; } catch (e) {}

    if (reduce || (bylo && !wymus)) return;
    try { sessionStorage.setItem('mr-wejscie', '1'); } catch (e) {}

    /* kadry w PEŁNEJ rozdzielczości (900×1600) — plakaty filmów mają 506 px szerokości
       i rozciągnięte na cały ekran robiły się papką (zgłoszenie K. 13.08). Kadr pokazujemy
       teraz w całości (contain), więc piksele idą 1:1 zamiast 3× w górę. */
    var KADRY = [
      'media/aftermovie_intro.webp',
      'media/szyon_toyota_waw_v2_intro.webp',
      'media/rich_amiri_mascotte_v2_intro.webp',
      'media/Manicure-reels1_intro.webp'
    ];
    var KLATKA = 130;                     // ile trwa jeden kadr
    var PODPIS = KADRY.length * KLATKA;   // 520 ms — wtedy wchodzi podpis
    var CIECIE = PODPIS + 480;            // 1000 ms — wtedy kadr się rozsuwa

    html.classList.add('wejscie-gra');

    var zdjete = false;
    function zdejmij() {
      if (zdjete) return;
      zdjete = true;
      html.classList.add('wejscie-f2');
      setTimeout(function () {
        html.classList.remove('wejscie-gra', 'wejscie-f1', 'wejscie-f2');
        var k = document.querySelector('.wejscie');
        if (k && k.parentNode) k.parentNode.removeChild(k);
      }, 720);
    }

    // BEZPIECZNIK: twardy limit — kurtyna schodzi niezależnie od wszystkiego
    var limit = stop ? 0 : setTimeout(zdejmij, 2200);

    // BEZPIECZNIK: dowolna reakcja użytkownika przerywa natychmiast
    ['click', 'touchstart', 'wheel', 'keydown'].forEach(function (ev) {
      addEventListener(ev, function przerwij() {
        removeEventListener(ev, przerwij);
        clearTimeout(limit);
        zdejmij();
      }, { passive: true, once: true });
    });

    function start() {
      var baza = window.MR_BAZA || '';
      function kadry() {
        return '<div class="wejscie__kadry">' + KADRY.map(function (k, i) {
          return '<div class="wejscie__slot" data-i="' + i + '">'
               +   '<div class="wejscie__tlo" style="background-image:url(' + baza + k + ')"></div>'
               +   '<img class="wejscie__kadr" src="' + baza + k + '" alt="">'
               + '</div>';
        }).join('') + '</div>';
      }

      var kadr = document.createElement('div');
      kadr.className = 'wejscie';
      kadr.setAttribute('aria-hidden', 'true');
      kadr.innerHTML =
        '<div class="wejscie__plyta wejscie__plyta--gora">' + kadry() + '</div>' +
        '<div class="wejscie__plyta wejscie__plyta--dol">' + kadry() + '</div>' +
        '<span class="wejscie__szpara"></span>' +
        '<img class="wejscie__logo" src="' + baza + 'media/logo.webp" alt="">' +
        '<span class="wejscie__kreska"></span>';
      document.body.appendChild(kadr);

      // montaż: kolejne kadry zapalają się co KLATKA ms (obie płyty równocześnie)
      KADRY.forEach(function (_, i) {
        setTimeout(function () {
          if (zdjete) return;
          kadr.querySelectorAll('.wejscie__slot').forEach(function (slot) {
            slot.classList.toggle('jest', +slot.dataset.i === i);
          });
        }, i * KLATKA);
      });

      // ostatni kadr gaśnie, wchodzi podpis
      setTimeout(function () {
        if (zdjete) return;
        kadr.querySelectorAll('.wejscie__slot').forEach(function (s) { s.classList.remove('jest'); });
        html.classList.add('wejscie-f1');
      }, PODPIS);

      if (!stop) setTimeout(zdejmij, CIECIE);
    }

    if (document.body) start();
    else document.addEventListener('DOMContentLoaded', start, { once: true });
  } catch (e) {
    try { document.documentElement.classList.remove('wejscie-gra', 'wejscie-f1', 'wejscie-f2'); } catch (e2) {}
  }
})();
