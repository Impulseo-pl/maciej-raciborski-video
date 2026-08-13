/* Maciej Raciborski — demo Impulseo */
(function () {
  'use strict';
  try {

  /* --- nawigacja: przyklejenie po zjechaniu z hero --- */
  var nav = document.querySelector('.nav');
  var ostatni = -1;
  addEventListener('scroll', function () {
    var y = scrollY > 60;
    if (y !== ostatni) { nav.classList.toggle('nav--przyklejona', y); ostatni = y; }
  }, { passive: true });

  /* --- kafle: pętla rusza dopiero po najechaniu (plik wczytuje się wtedy) --- */
  document.querySelectorAll('.kafel').forEach(function (kafel) {
    var v = kafel.querySelector('.kafel__v');
    if (!v) return;

    function start() {
      if (v.preload === 'none') { v.preload = 'auto'; v.load(); }
      var p = v.play();
      if (p && p.catch) p.catch(function () {});
    }
    function stop() { v.pause(); try { v.currentTime = 0; } catch (e) {} }

    kafel.addEventListener('mouseenter', start);
    kafel.addEventListener('mouseleave', stop);
    kafel.addEventListener('focus', start);
    kafel.addEventListener('blur', stop);
  });

  /* --- na telefonie: pętla startuje, gdy kafel wjedzie w kadr (po jednym) --- */
  var dotyk = matchMedia('(hover:none)').matches;
  if (dotyk && 'IntersectionObserver' in window) {
    var obs = new IntersectionObserver(function (wpisy) {
      wpisy.forEach(function (w) {
        var v = w.target.querySelector('.kafel__v');
        if (!v) return;
        if (w.isIntersecting) {
          if (v.preload === 'none') { v.preload = 'auto'; v.load(); }
          var p = v.play(); if (p && p.catch) p.catch(function () {});
        } else { v.pause(); }
      });
    }, { threshold: 0.6 });
    document.querySelectorAll('.kafel').forEach(function (k) { obs.observe(k); });
  }

  /* --- odtwarzacz pełnego filmu --- */
  var lb = document.getElementById('lightbox');
  var lbV = document.getElementById('lightbox-video');
  var lbT = document.getElementById('lightbox-tytul');
  var lbX = document.getElementById('lightbox-zamknij');
  var wracaDo = null;
  var maLightbox = !!(lb && lbV && lbX);          // podstrona bez odtwarzacza to nie błąd

  function otworz(src, tytul, zrodlo, plakat) {
    if (!maLightbox) return;
    wracaDo = zrodlo || null;
    if (plakat) lbV.poster = plakat;
    lbV.preload = 'auto';
    lbV.src = src;
    lbV.load();
    lbT.textContent = tytul || '';
    lb.hidden = false;
    document.body.style.overflow = 'hidden';
    lbX.focus();
    var p = lbV.play(); if (p && p.catch) p.catch(function () {});
  }
  function zamknij() {
    lbV.pause(); lbV.removeAttribute('src'); lbV.load();
    lb.hidden = true;
    document.body.style.overflow = '';
    if (wracaDo) wracaDo.focus();
  }

  document.querySelectorAll('.kafel').forEach(function (kafel) {
    kafel.addEventListener('click', function () {
      var v = kafel.querySelector('.kafel__v');
      otworz(kafel.dataset.full, kafel.dataset.tytul, kafel, v ? v.getAttribute('poster') : null);
    });
  });
  if (maLightbox) {
    lbX.addEventListener('click', zamknij);
    lb.addEventListener('click', function (e) { if (e.target === lb) zamknij(); });
    addEventListener('keydown', function (e) { if (e.key === 'Escape' && !lb.hidden) zamknij(); });
  }

  /* --- formularz (demo: bez wysyłki na serwer) --- */
  var form = document.getElementById('formularz');
  var info = document.getElementById('formularz-info');
  if (!form || !info) return;                     // formularz jest tylko na /kontakt/
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var imie = form.imie.value.trim();
    var kontakt = form.kontakt.value.trim();
    info.className = 'formularz__info';

    if (imie.length < 2 || kontakt.length < 5) {
      info.textContent = 'Uzupełnij imię oraz telefon lub e-mail — inaczej nie mam jak odpisać.';
      info.classList.add('formularz__info--blad');
      return;
    }
    info.textContent = 'Dziękuję. Odezwę się w ciągu 24 godzin. (To wersja demonstracyjna — zgłoszenie nie zostało wysłane.)';
    info.classList.add('formularz__info--ok');
    form.reset();
  });

  } catch (e) { /* jeden efekt mniej, strona działa dalej */ }
})();

/* ============================================================
   OŚ PROCESU — sekcja przyklejona na czas przejścia przez kroki.
   Strona zatrzymuje się na sekcji, przeprowadza przez cały proces i puszcza dalej.
   Lewa kolumna (numer, nazwa, pasek) przechodzi razem z krokami, nie przeskakuje.

   BEZPIECZNIK: klasę .pin-on nadaje wyłącznie ten skrypt. Bez niego albo przy błędzie
   sekcja jest zwykłą listą - wszystko widoczne. Na telefonie przyklejania nie ma.
   ============================================================ */
(function () {
  'use strict';
  try {
    if (matchMedia('(prefers-reduced-motion:reduce)').matches) return;
    var sekcje = [].slice.call(document.querySelectorAll('.proces'));
    if (!sekcje.length) return;

    var duzyEkran = function () { return innerWidth >= 901; };
    if (duzyEkran()) document.documentElement.classList.add('pin-on');
    document.documentElement.classList.add('os-on');

    sekcje.forEach(function (sek) {
      var kroki = [].slice.call(sek.querySelectorAll('.proces__lista > li'));
      if (kroki.length < 2) return;
      var lista = sek.querySelector('.proces__lista');
      var teraz = sek.querySelector('.proces__teraz');
      var pasek = sek.querySelector('.proces__pasek > i');
      var nazwa = sek.querySelector('.proces__krok');
      var bok = sek.querySelector('.proces__bok');
      sek.style.setProperty('--kroki', kroki.length);

      var aktualny = -1;

      function ustawKrok(i, postep) {
        if (i !== aktualny) {
          aktualny = i;
          kroki.forEach(function (li, n) {
            li.classList.toggle('os-teraz', n === i);
            li.classList.toggle('os-bylo', n < i);
          });
          // lewa kolumna: krótkie wyjście i wejście zamiast skoku
          if (bok) {
            bok.classList.add('zmiana');
            setTimeout(function () {
              if (teraz) teraz.textContent = String(i + 1).padStart(2, '0');
              var h3 = kroki[i].querySelector('h3');
              if (nazwa && h3) nazwa.textContent = h3.textContent;
              bok.classList.remove('zmiana');
            }, 190);
          }
          // przy przyklejeniu lista jedzie tak, żeby aktywny krok stał w tym samym miejscu
          if (document.documentElement.classList.contains('pin-on') && duzyEkran()) {
            var cel = kroki[i];
            var przesun = cel.offsetTop - (lista.offsetHeight - cel.offsetHeight) / 2;
            lista.style.transform = 'translateY(' + (-przesun) + 'px)';
          } else {
            lista.style.transform = '';
          }
        }
        if (pasek) pasek.style.width = Math.max(4, Math.min(100, postep * 100)) + '%';
      }

      function odswiez() {
        var r = sek.getBoundingClientRect();
        var droga = sek.offsetHeight - innerHeight;      // ile realnie się przewija
        var postep;
        if (droga > 20 && document.documentElement.classList.contains('pin-on') && duzyEkran()) {
          postep = Math.max(0, Math.min(1, -r.top / droga));
        } else {
          // bez przyklejania: krok wyznacza pozycja treści na ekranie
          var srodek = innerHeight * 0.55, wybrany = 0;
          kroki.forEach(function (li, n) { if (li.getBoundingClientRect().top <= srodek) wybrany = n; });
          ustawKrok(wybrany, (wybrany + 1) / kroki.length);
          return;
        }
        var i = Math.min(kroki.length - 1, Math.floor(postep * kroki.length + 0.0001));
        ustawKrok(i, (postep * (kroki.length - 1) + 1) / kroki.length);
      }

      var czeka = false;
      addEventListener('scroll', function () {
        if (czeka) return;
        czeka = true;
        requestAnimationFrame(function () { odswiez(); czeka = false; });
      }, { passive: true });
      addEventListener('resize', function () {
        document.documentElement.classList.toggle('pin-on', duzyEkran());
        aktualny = -1;
        odswiez();
      }, { passive: true });
      odswiez();
    });
  } catch (e) {
    try { document.documentElement.classList.remove('pin-on'); } catch (e2) {}
  }
})();

/* ---- menu na telefonie ---- */
(function () {
  try {
    var burger = document.querySelector('.nav__burger');
    var navEl = document.querySelector('.nav');
    if (!burger || !navEl) return;
    burger.addEventListener('click', function () {
      var otwarte = navEl.classList.toggle('nav--otwarte');
      burger.setAttribute('aria-expanded', otwarte ? 'true' : 'false');
      document.body.style.overflow = otwarte ? 'hidden' : '';
    });
    navEl.querySelectorAll('.nav__links a').forEach(function (a) {
      a.addEventListener('click', function () {
        navEl.classList.remove('nav--otwarte');
        burger.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      });
    });
    addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && navEl.classList.contains('nav--otwarte')) burger.click();
    });
  } catch (e) {}
})();

/* ---- pasek akcji na telefonie chowa się na pierwszym ekranie ----
   Powód: zasłaniał rolkę w hero, czyli najmocniejszy element strony (uwaga K. 13.08).
   Warunek oparty na przewinięciu, nie na widoczności hero — hero bywa wyższe niż ekran,
   więc obserwator trzymał pasek schowany zbyt długo (zmierzone: 600 px i nadal ukryty). */
(function () {
  try {
    var html = document.documentElement;
    if (!document.querySelector('.hero')) return;      // podstrony mają pasek od razu
    var prog = function () { return Math.min(innerHeight * 0.62, 480); };
    var ustaw = function () { html.classList.toggle('hero-widoczne', scrollY < prog()); };
    ustaw();
    var czeka = false;
    addEventListener('scroll', function () {
      if (czeka) return;
      czeka = true;
      requestAnimationFrame(function () { ustaw(); czeka = false; });
    }, { passive: true });
    addEventListener('resize', ustaw, { passive: true });
  } catch (e) {}
})();
