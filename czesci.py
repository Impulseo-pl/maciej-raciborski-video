#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Wspólne części stron (nagłówek, stopka, head) - żeby cztery podstrony
nie rozjechały się przy pierwszej poprawce. Uruchom: python3 czesci.py
"""
import pathlib, re

WERSJA = "11"


def sklej(html):
    """Twarda spacja po jednoliterowych spójnikach - tylko w treści, nie w atrybutach."""
    def w_tresci(m):
        return m.group(1) + re.sub(
            r'(?<=[\s(>])([iwzoauIWZOAU])\s+(?=[A-Za-z0-9\u0104-\u017c])',
            lambda x: x.group(1) + '\u00a0', m.group(2)) + m.group(3)
    return re.sub(r'(<(?:p|h1|h2|h3|li|span|summary|figcaption)[^>]*>)([^<]+)(</(?:p|h1|h2|h3|li|span|summary|figcaption)>)',
                  w_tresci, html)

def head(tytul, opis, sciezka="", og="media/aftermovie_poster.jpg", wejscie=False):
    """sciezka: '' dla strony głównej, '../' dla podstron"""
    p = sciezka
    intro_css = ""
    intro_js = ""
    if wejscie:
        intro_css = f'<link rel="stylesheet" href="{p}wejscie.css?v={WERSJA}">'
        intro_js = f'<script src="{p}wejscie.js?v={WERSJA}"></script>'
    return f'''<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{tytul}</title>
<meta name="description" content="{opis}">
<meta property="og:title" content="{tytul}">
<meta property="og:description" content="{opis}">
<meta property="og:image" content="{p}{og}">
<meta property="og:type" content="website">
<link rel="stylesheet" href="{p}app.css?v={WERSJA}">
{intro_css}
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "Maciej Raciborski",
  "description": "Produkcja wideo i prowadzenie social mediów dla marek.",
  "url": "https://maciejraciborski.pl/",
  "email": "kontakt@maciejraciborski.pl",
  "areaServed": "PL",
  "serviceType": ["Produkcja wideo", "Prowadzenie social mediów", "Materiały reklamowe"]
}}
</script>
{intro_js}
</head>
<body>

<a class="skip" href="#tresc">Przejdź do treści</a>
'''


def nav(aktywna="", sciezka=""):
    p = sciezka
    def a(nazwa, href, klucz, klasa=""):
        akt = ' aria-current="page"' if aktywna == klucz else ''
        kl = f' class="{klasa}"' if klasa else ''
        return f'<a href="{p}{href}"{kl}{akt}>{nazwa}</a>'
    return f'''
<header class="nav" id="gora">
  <a class="nav__logo" href="{p}index.html" aria-label="Strona główna"><img src="{p}media/logo.webp" alt="Maciej Raciborski" width="415" height="58"></a>
  <button class="nav__burger" aria-label="Menu" aria-expanded="false"><span></span><span></span></button>
  <nav class="nav__links" aria-label="Menu główne">
    {a("Realizacje", "realizacje/", "realizacje")}
    {a("O mnie", "o-mnie/", "o-mnie")}
    {a("Współpraca", "wspolpraca/", "wspolpraca")}
    {a("Kontakt", "kontakt/", "kontakt", "nav__cta")}
  </nav>
</header>
'''


def stopka(sciezka=""):
    p = sciezka
    return f'''
<footer class="stopka">
  <div class="stopka__in">
    <div class="stopka__marka">
      <img src="{p}media/logo.webp" alt="Maciej Raciborski" width="415" height="58" class="stopka__logo">
      <p class="stopka__opis">Wideo i social media dla marek. Eventy, motoryzacja, marki lifestyle'owe.</p>
    </div>
    <nav class="stopka__menu" aria-label="Stopka">
      <a href="{p}realizacje/">Realizacje</a>
      <a href="{p}o-mnie/">O mnie</a>
      <a href="{p}wspolpraca/">Współpraca</a>
      <a href="{p}kontakt/">Kontakt</a>
    </nav>
    <div class="stopka__kontakt">
      <a href="mailto:kontakt@maciejraciborski.pl">kontakt@maciejraciborski.pl</a>
      <a href="{p}kontakt/" class="btn btn--pusty btn--maly">Umów rozmowę</a>
    </div>
  </div>
  <p class="stopka__podpis">Projekt strony: <a href="https://impulseo.pl" rel="noopener" target="_blank">Impulseo</a></p>
</footer>

<div class="pasek-mob" aria-label="Szybki kontakt">
  <a href="{p}realizacje/">Realizacje</a>
  <a href="{p}kontakt/" class="pasek-mob--akcent">Umów rozmowę</a>
</div>

<!-- ODTWARZACZ pełnego filmu (musi być na KAŻDEJ stronie z kaflami) -->
<div class="lightbox" id="lightbox" hidden>
  <button class="lightbox__zamknij" id="lightbox-zamknij" aria-label="Zamknij">&times;</button>
  <figure class="lightbox__ramka">
    <video id="lightbox-video" controls playsinline preload="none"></video>
    <figcaption id="lightbox-tytul"></figcaption>
  </figure>
</div>

<script src="{p}app.js?v={WERSJA}"></script>
</body>
</html>
'''

if __name__ == "__main__":
    print("Moduł pomocniczy - importowany przez buduj.py")
