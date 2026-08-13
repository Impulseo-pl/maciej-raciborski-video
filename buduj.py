#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator strony demo dla Maciej Raciborski (Impulseo).
Jedno źródło prawdy dla nagłówka/stopki - podstrony nie rozjadą się przy poprawce.

Uruchom:  python3 buduj.py
"""
import pathlib, shutil
from czesci import head, nav, stopka, sklej, WERSJA

KAT = pathlib.Path(__file__).parent

# ── dane realizacji (opisy oparte WYŁĄCZNIE na tym, co widać w materiałach;
#    żadnych zmyślonych liczb - te wchodzą dopiero od klienta) ──────────────
REALIZACJE = [
    dict(
        slug="spektaklove",
        marka="Spektaklove",
        typ="Aftermovie z premiery",
        loop="media/aftermovie_loop.mp4",
        full="media/aftermovie_full.mp4",
        poster="media/aftermovie_poster.jpg",
        kontekst="Premiera spektaklu z czerwonym dywanem, ścianką sponsorską i publicznością. Wydarzenie żyje jeden wieczór - materiał ma je przedłużyć na kolejne tygodnie.",
        zadanie="Zamknąć cały wieczór w krótkiej formie, która obroni się na Instagramie i będzie mogła pójść do partnerów wydarzenia.",
        praca=[
            "zdjęcia przez cały wieczór: goście, ścianka, kulisy, scena",
            "montaż w pionie 9:16 pod Reels i TikToka",
            "tempo cięć prowadzone muzyką, bez lektora",
            "logotypy partnerów widoczne, ale nie zasłaniające akcji",
        ],
        efekt="Jeden materiał, który działa jako podsumowanie dla widzów i jako dowód zasięgu dla sponsorów.",
    ),
    dict(
        slug="toyota",
        marka="Toyota",
        typ="Materiał terenowy",
        loop="media/szyon_toyota_waw_v2_loop.mp4",
        full="media/szyon_toyota_waw_v2_full.mp4",
        poster="media/szyon_toyota_waw_v2_poster.jpg",
        kontekst="Zdjęcia zimą, w plenerze, z autem jako bohaterem. Warunki, w których nie da się powtórzyć ujęcia - światła starcza na kilka godzin.",
        zadanie="Pokazać samochód w realnym użyciu, a nie w studiu. Materiał ma wyglądać jak scena z życia, nie jak katalog.",
        praca=[
            "plan zdjęciowy dopasowany do godzin ze światłem",
            "ujęcia z ręki i z gimbala, blisko bohatera",
            "pion 9:16 z myślą o publikacji w social mediach",
            "kolor utrzymany w chłodnej, zimowej palecie",
        ],
        efekt="Materiał, który marka może wykorzystać zarówno w rolce, jak i w reklamie płatnej.",
    ),
    dict(
        slug="mascotte",
        marka="RAGE × Mascotte",
        typ="Event i koncert",
        loop="media/rich_amiri_mascotte_v2_loop.mp4",
        full="media/rich_amiri_mascotte_v2_full.mp4",
        poster="media/rich_amiri_mascotte_v2_poster.jpg",
        kontekst="Wieczór z DJ-em, stoiskiem marki i tłumem. Trudne światło: czerwone reflektory, dym, ciemne wnętrze.",
        zadanie="Oddać energię wieczoru i pokazać obecność marki tak, żeby nie wyglądała na wklejoną.",
        praca=[
            "zdjęcia w ruchu, blisko ludzi i sceny",
            "praca w trudnym świetle bez dodatkowego oświetlenia",
            "produkt marki w kadrze naturalnie, przy okazji akcji",
            "montaż w rytm muzyki, zakończony planszą marki",
        ],
        efekt="Materiał dla marki i dla organizatora - jedne zdjęcia, dwa zastosowania.",
    ),
    dict(
        slug="beauty",
        marka="Beauty",
        typ="Rolka produktowa",
        loop="media/Manicure-reels1_loop.mp4",
        full="media/Manicure-reels1_full.mp4",
        poster="media/Manicure-reels1_poster.jpg",
        kontekst="Usługa, której efekt widać w szczegółach. Klientka wybiera salon oczami - zdjęcie z telefonu tego nie sprzeda.",
        zadanie="Pokazać precyzję pracy w zbliżeniu i utrzymać uwagę widza przez kilkanaście sekund.",
        praca=[
            "makro na dłoniach i narzędziach",
            "stałe, miękkie światło zamiast lampy sufitowej",
            "krótkie ujęcia, jedno działanie na ujęcie",
            "format pionowy pod Reels i TikToka",
        ],
        efekt="Powtarzalny schemat, który salon może wykorzystywać przy kolejnych zabiegach.",
    ),
]


# ══════════════════════════════════════════════════════════════════════════
def strona_glowna():
    t = head("Maciej Raciborski - wideo i social media dla marek",
             "Produkcja wideo i prowadzenie social mediów dla marek. Realizacje dla eventów, motoryzacji i marek lifestyle'owych.",
             wejscie=True)
    t += nav("")
    t += '''
<main id="tresc">

  <!-- HERO -->
  <section class="hero">
    <video class="hero__ambient" src="media/rich_amiri_mascotte_v2_loop.mp4" poster="media/rich_amiri_mascotte_v2_poster.jpg"
           autoplay muted loop playsinline preload="auto" aria-hidden="true"></video>
    <div class="hero__mask"></div>

    <div class="hero__in">
      <div class="hero__naglowek">
        <p class="hero__nad">Wideo i social media dla marek</p>
        <h1>Buduję wizerunek marek przez wideo</h1>
      </div>

      <div class="hero__ekran">
        <video class="hero__pion" src="media/rich_amiri_mascotte_v2_loop.mp4" poster="media/rich_amiri_mascotte_v2_poster.jpg"
               autoplay muted loop playsinline aria-label="Fragment realizacji: event RAGE i Mascotte"></video>
      </div>

      <div class="hero__reszta">
        <p class="hero__sub">Przejmuję wideo i obecność marki w social mediach w całości - od kierunku, przez produkcję, po publikację.</p>
        <div class="hero__akcje">
          <a class="btn btn--pelny" href="realizacje/">Zobacz realizacje</a>
          <a class="btn btn--pusty" href="kontakt/">Umów rozmowę</a>
        </div>
      </div>
    </div>

    <a class="hero__strzalka" href="#realizacje" aria-label="Przewiń do realizacji"></a>
  </section>

  <!-- PASEK DOWODU -->
  <section class="dowod" aria-label="Wybrane realizacje i marki">
    <div class="dowod__in">
      <div class="dowod__poz"><span class="dowod__k">Spektaklove</span><span class="dowod__v">aftermovie z eventu</span></div>
      <div class="dowod__poz"><span class="dowod__k">Toyota</span><span class="dowod__v">materiał terenowy</span></div>
      <div class="dowod__poz"><span class="dowod__k">Mascotte</span><span class="dowod__v">event i koncert</span></div>
      <div class="dowod__poz"><span class="dowod__k">Sceny i koncerty</span><span class="dowod__v">duże realizacje</span></div>
      <div class="dowod__poz"><span class="dowod__k">Beauty</span><span class="dowod__v">rolki produktowe</span></div>
    </div>
  </section>

  <!-- ŚCIANA REALIZACJI -->
  <section class="realizacje" id="realizacje">
    <div class="sekcja__glowa">
      <h2>Realizacje</h2>
      <p>Najedź, żeby zobaczyć ruch. Kliknij, żeby obejrzeć całość z dźwiękiem.</p>
    </div>

    <div class="sciana">
'''
    for r in REALIZACJE:
        t += f'''      <button class="kafel" data-full="{r["full"]}" data-tytul="{r["marka"]} - {r["typ"].lower()}">
        <video class="kafel__v" src="{r["loop"]}" poster="{r["poster"]}" muted loop playsinline preload="none"></video>
        <span class="kafel__opis"><span class="kafel__t">{r["marka"]}</span><span class="kafel__p">{r["typ"]}</span></span>
      </button>
'''
    t += '''    </div>
    <p class="sciana__wiecej"><a class="link-strzalka" href="realizacje/">Zobacz opisy realizacji</a></p>
  </section>

  <!-- O MNIE -->
  <section class="omnie" id="omnie">
    <div class="omnie__foto">
      <img src="media/omnie.webp" alt="Maciej Raciborski z kamerą podczas zdjęć w plenerze" width="390" height="551">
    </div>
    <div class="omnie__tekst">
      <h2>Maciej Raciborski</h2>
      <p class="lead">Nie sprzedaję pojedynczych filmów. Przejmuję obszar, który zwykle zjada firmie najwięcej czasu - wideo i obecność w social mediach.</p>
      <p>Pracuję ze stałym zespołem odpowiedzialnym za produkcję i publikację, dzięki czemu marka mówi jednym głosem, a nie czterema. Angażuję się w każdą współpracę indywidualnie - nie działam masowo ani szablonowo.</p>
      <p>Po stronie klienta zostaje jedno: akceptacja kierunku.</p>
      <a class="btn btn--pelny" href="o-mnie/">Poznaj mnie bliżej</a>
    </div>
  </section>

  <!-- PAS ZE SCENĄ -->
  <section class="pas stopklatka" aria-label="Realizacje sceniczne">
    <img src="media/polsat.webp" alt="Duża scena koncertowa w świetle reflektorów podczas realizacji" width="1280" height="720">
    <div class="pas__tekst">
      <p class="pas__haslo">Od rolki na telefon po scenę z reflektorami.</p>
      <p class="pas__opis">Eventy, koncerty, materiały produktowe i marki lifestyle'owe.</p>
    </div>
  </section>

  <!-- OŚ PROCESU -->
  <section class="proces proces-os os-mech" id="zakres">
    <div class="proces__in">
      <div class="proces__bok">
        <p class="proces__nad">Jak to działa</p>
        <h2>Za co biorę odpowiedzialność</h2>
        <p class="proces__opis">Cały obszar - od decyzji po efekt. Po Twojej stronie zostaje akceptacja kierunku.</p>
        <div class="proces__licznik">
          <span class="proces__teraz">01</span><span class="proces__ile">/ 04</span>
        </div>
        <div class="proces__pasek"><i></i></div>
        <p class="proces__krok">Kierunek</p>
      </div>

      <ol class="proces__lista" data-os-steps>
        <li>
          <span class="proces__nr">Krok 01</span>
          <h3>Kierunek</h3>
          <p>Biorę odpowiedzialność za kierunek komunikacji, priorytety i decyzje. Działam konsekwentnie, bez improwizacji i nerwowych zmian.</p>
        </li>
        <li>
          <span class="proces__nr">Krok 02</span>
          <h3>Produkcja</h3>
          <p>Biorę na siebie całą produkcję wideo i materiałów wspierających. Nie koordynujesz zdjęć i nie pilnujesz tematów.</p>
        </li>
        <li>
          <span class="proces__nr">Krok 03</span>
          <h3>Dystrybucja</h3>
          <p>Dbam o obecność marki w social mediach. Treści trafiają tam, gdzie powinny - regularnie i spójnie.</p>
        </li>
        <li>
          <span class="proces__nr">Krok 04</span>
          <h3>Efekt</h3>
          <p>Monitoruję efekt i koryguję kierunek, jeśli trzeba. Bez nerwowych ruchów i bez presji na szybki wynik.</p>
        </li>
      </ol>
    </div>
  </section>

  <!-- CTA -->
  <section class="cta">
    <div class="cta__in">
      <h2>Rozmowa wstępna, 30 minut</h2>
      <p>Sprawdzamy dopasowanie. Nie pracuję z każdym - na podstawie rozmowy decydujemy, czy chcemy wejść w długofalową współpracę.</p>
      <a class="btn btn--pelny" href="kontakt/">Umów rozmowę</a>
    </div>
  </section>

</main>
'''
    t += stopka("")
    return t


# ══════════════════════════════════════════════════════════════════════════
def strona_realizacje():
    t = head("Realizacje - Maciej Raciborski",
             "Case studies realizacji wideo: aftermovie z eventu, materiał terenowy dla marki motoryzacyjnej, event i koncert, rolka produktowa.",
             "../")
    t += nav("realizacje", "../")
    t += '''
<main id="tresc">
  <section class="podtytul">
    <div class="podtytul__in">
      <p class="podtytul__nad">Realizacje</p>
      <h1>Co robię i jak to powstaje</h1>
      <p class="podtytul__opis">Cztery realizacje, cztery różne zadania. Każdą można obejrzeć w całości - z dźwiękiem, bez wychodzenia ze strony.</p>
    </div>
  </section>
'''
    for i, r in enumerate(REALIZACJE):
        odwrot = " case--odwrot" if i % 2 else ""
        praca = "\n".join(f"          <li>{p}</li>" for p in r["praca"])
        t += f'''
  <article class="case{odwrot}" id="{r["slug"]}">
    <div class="case__ekran">
      <button class="kafel kafel--case" data-full="../{r["full"]}" data-tytul="{r["marka"]} - {r["typ"].lower()}">
        <video class="kafel__v" src="../{r["loop"]}" poster="../{r["poster"]}" muted loop playsinline preload="none"></video>
        <span class="kafel__opis"><span class="kafel__t">Obejrzyj całość</span><span class="kafel__p">z dźwiękiem</span></span>
      </button>
    </div>
    <div class="case__tekst">
      <p class="case__typ">{r["typ"]}</p>
      <h2>{r["marka"]}</h2>
      <div class="case__blok">
        <h3>Sytuacja</h3>
        <p>{r["kontekst"]}</p>
      </div>
      <div class="case__blok">
        <h3>Zadanie</h3>
        <p>{r["zadanie"]}</p>
      </div>
      <div class="case__blok">
        <h3>Co zrobiłem</h3>
        <ul class="case__lista">
{praca}
        </ul>
      </div>
      <p class="case__efekt">{r["efekt"]}</p>
    </div>
  </article>
'''
    t += '''
  <section class="cta">
    <div class="cta__in">
      <h2>Chcesz podobny materiał dla swojej marki?</h2>
      <p>Zacznijmy od 30-minutowej rozmowy. Sprawdzimy, czy to, co robię, pasuje do tego, czego potrzebujesz.</p>
      <a class="btn btn--pelny" href="../kontakt/">Umów rozmowę</a>
    </div>
  </section>
</main>
'''
    t += stopka("../")
    return t


# ══════════════════════════════════════════════════════════════════════════
def strona_o_mnie():
    t = head("O mnie - Maciej Raciborski",
             "Kim jestem, jak pracuję i dla kogo. Wideo i social media dla marek, które chcą oddać ten obszar w całości.",
             "../", og="media/omnie.webp")
    t += nav("o-mnie", "../")
    t += '''
<main id="tresc">
  <section class="podtytul">
    <div class="podtytul__in">
      <p class="podtytul__nad">O mnie</p>
      <h1>Maciej Raciborski</h1>
      <p class="podtytul__opis">Wideo to nie jest dla mnie usługa na sztuki. To sposób, w jaki marka pokazuje się ludziom - dzień po dniu, przez miesiące.</p>
    </div>
  </section>

  <section class="omnie omnie--pod">
    <div class="omnie__foto">
      <img src="../media/omnie.webp" alt="Maciej Raciborski z kamerą podczas zdjęć w plenerze" width="390" height="551">
    </div>
    <div class="omnie__tekst">
      <p class="lead">Zaczynałem od pojedynczych zleceń: event, jeden film, koniec tematu. Szybko zobaczyłem, gdzie to nie działa.</p>
      <p>Jeden dobry film nie zmienia obecności marki. Zmienia ją konsekwencja - to, że przez kolejne miesiące pod tym samym szyldem wychodzą materiały, które trzymają poziom i mówią jednym głosem. Dlatego dziś nie sprzedaję filmów. Biorę na siebie cały obszar.</p>
      <p>Pracuję ze stałym zespołem odpowiedzialnym za produkcję i publikację. To celowe: jeden człowiek nie utrzyma jakości przy regularnym wypuszczaniu materiałów, a przypadkowi podwykonawcy rozjeżdżają styl marki w trzy miesiące.</p>
    </div>
  </section>

  <section class="zasady">
    <div class="sekcja__glowa">
      <p class="proces__nad">W skrócie</p>
      <h2>Jak pracuję</h2>
    </div>
    <div class="zasady__siatka">
      <article class="zasada">
        <h3>Nie działam masowo</h3>
        <p>Prowadzę kilka marek naraz, nie kilkanaście. To ograniczenie, które daje uwagę - i jedyny sposób, żeby jakość nie spadła po trzecim miesiącu.</p>
      </article>
      <article class="zasada">
        <h3>Biorę decyzje na siebie</h3>
        <p>Nie przychodzę z pytaniem „co publikujemy w tym tygodniu". Przychodzę z kierunkiem, a Ty go akceptujesz albo korygujesz.</p>
      </article>
      <article class="zasada">
        <h3>Bez presji na szybki wynik</h3>
        <p>Efekt w social mediach buduje się miesiącami. Kto obiecuje inaczej, sprzedaje nadzieję, a nie pracę.</p>
      </article>
      <article class="zasada">
        <h3>Materiał ma pracować dalej</h3>
        <p>Ten sam film ma się bronić w rolce, w reklamie płatnej i w rozmowie z partnerem wydarzenia. Kręcę z myślą o wszystkich trzech.</p>
      </article>
    </div>
  </section>

  <section class="pas stopklatka" aria-label="Realizacje sceniczne">
    <img src="../media/polsat.webp" alt="Duża scena koncertowa w świetle reflektorów podczas realizacji" width="1280" height="720">
    <div class="pas__tekst">
      <p class="pas__haslo">Warunki bywają trudniejsze niż plan.</p>
      <p class="pas__opis">Dym, czerwone światło, tłum i jedno podejście - to normalna sytuacja przy evencie.</p>
    </div>
  </section>

  <section class="cta">
    <div class="cta__in">
      <h2>Porozmawiajmy o Twojej marce</h2>
      <p>30 minut wystarczy, żeby sprawdzić, czy mamy wspólne flow.</p>
      <a class="btn btn--pelny" href="../kontakt/">Umów rozmowę</a>
    </div>
  </section>
</main>
'''
    t += stopka("../")
    return t


# ══════════════════════════════════════════════════════════════════════════
def strona_wspolpraca():
    t = head("Współpraca - Maciej Raciborski",
             "Jak wygląda współpraca: zakres, przebieg miesiąca i dla kogo to jest. Wideo i social media prowadzone w całości.",
             "../")
    t += nav("wspolpraca", "../")
    t += '''
<main id="tresc">
  <section class="podtytul">
    <div class="podtytul__in">
      <p class="podtytul__nad">Współpraca</p>
      <h1>Jak to wygląda w praktyce</h1>
      <p class="podtytul__opis">Bez tajemnic co do zakresu. Poniżej to, co biorę na siebie, jak wygląda miesiąc pracy i z kim to działa, a z kim nie.</p>
    </div>
  </section>


  <section class="taras" aria-label="Fragmenty realizacji">
    <div class="taras__in">
      <figure class="taras__kafel">
        <img src="../media/aftermovie_poster.jpg" alt="Kadr z realizacji: aftermovie z premiery" loading="eager" fetchpriority="high">
        <figcaption><span class="taras__t">Spektaklove</span><span class="taras__p">Aftermovie z premiery</span></figcaption>
      </figure>
      <figure class="taras__kafel">
        <img src="../media/szyon_toyota_waw_v2_poster.jpg" alt="Kadr z realizacji: materiał terenowy">
        <figcaption><span class="taras__t">Toyota</span><span class="taras__p">Materiał terenowy</span></figcaption>
      </figure>
      <figure class="taras__kafel">
        <img src="../media/rich_amiri_mascotte_v2_poster.jpg" alt="Kadr z realizacji: event i koncert">
        <figcaption><span class="taras__t">RAGE x Mascotte</span><span class="taras__p">Event i koncert</span></figcaption>
      </figure>
    </div>
  </section>
  <section class="proces proces-os os-mech">
    <div class="proces__in">
      <div class="proces__bok">
        <p class="proces__nad">Przebieg</p>
        <h2>Miesiąc pracy krok po kroku</h2>
        <p class="proces__opis">Ten sam rytm co miesiąc. Przewidywalność jest tu ważniejsza niż efektowność.</p>
        <div class="proces__licznik">
          <span class="proces__teraz">01</span><span class="proces__ile">/ 05</span>
        </div>
        <div class="proces__pasek"><i></i></div>
        <p class="proces__krok">Ustalenie kierunku</p>
      </div>

      <ol class="proces__lista" data-os-steps>
        <li>
          <span class="proces__nr">Krok 01</span>
          <h3>Ustalenie kierunku</h3>
          <p>Rozmowa o marce, celach i tym, czego nie chcesz. Z tego powstaje kierunek na najbliższe miesiące, nie na najbliższy tydzień.</p>
        </li>
        <li>
          <span class="proces__nr">Krok 02</span>
          <h3>Plan zdjęciowy</h3>
          <p>Ustalamy terminy i miejsca. Zdjęcia grupuję w bloki, żeby nie zajmować Ci czasu co tydzień.</p>
        </li>
        <li>
          <span class="proces__nr">Krok 03</span>
          <h3>Produkcja</h3>
          <p>Zdjęcia, montaż, korekta koloru, dźwięk. Materiały powstają z zapasem, nie na styk przed publikacją.</p>
        </li>
        <li>
          <span class="proces__nr">Krok 04</span>
          <h3>Akceptacja i publikacja</h3>
          <p>Dostajesz gotowe materiały do akceptacji kierunku. Publikacją i harmonogramem zajmuję się ja.</p>
        </li>
        <li>
          <span class="proces__nr">Krok 05</span>
          <h3>Podsumowanie miesiąca</h3>
          <p>Co zadziałało, co nie, co zmieniamy w kolejnym miesiącu. Bez nerwowych zwrotów po jednym słabszym materiale.</p>
        </li>
      </ol>
    </div>
  </section>

  <section class="dwie">
    <div class="dwie__in">
      <div class="dwie__kol">
        <h2>Z kim pracuję</h2>
        <ul class="lista-tak">
          <li>Firmy, które chcą oddać wideo i social media w całości</li>
          <li>Marki, dla których spójność jest ważniejsza niż chwilowy wynik</li>
          <li>Klienci rozumiejący, że proces wymaga czasu i konsekwencji</li>
          <li>Marki, które mają co pokazać - realny produkt, usługę albo wydarzenie</li>
        </ul>
      </div>
      <div class="dwie__kol">
        <h2>Z kim nie</h2>
        <ul class="lista-nie">
          <li>Jednorazowe zlecenia „jeden filmik i zobaczymy"</li>
          <li>Oczekiwanie wyników w dwa tygodnie</li>
          <li>Praca, w której każdy materiał przechodzi przez pięć osób decyzyjnych</li>
          <li>Sytuacje, w których wideo ma zastąpić brak pomysłu na markę</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="cta">
    <div class="cta__in">
      <h2>Sprawdźmy dopasowanie</h2>
      <p>Nie pracuję z każdym. Rozmowa wstępna jest po to, żeby obie strony to sprawdziły, zanim cokolwiek podpiszemy.</p>
      <a class="btn btn--pelny" href="../kontakt/">Umów rozmowę</a>
    </div>
  </section>
</main>
'''
    t += stopka("../")
    return t


# ══════════════════════════════════════════════════════════════════════════
def strona_kontakt():
    t = head("Kontakt - Maciej Raciborski",
             "Umów 30-minutową rozmowę wstępną. Sprawdzimy dopasowanie, zanim zaczniemy współpracę.",
             "../")
    t += nav("kontakt", "../")
    t += '''
<main id="tresc">
  <section class="podtytul">
    <div class="podtytul__in">
      <p class="podtytul__nad">Kontakt</p>
      <h1>Rozmowa wstępna, 30 minut</h1>
      <p class="podtytul__opis">Bez prezentacji i bez sztywnej oferty na pierwszej rozmowie. Sprawdzamy, czy mamy wspólne flow i czy w ogóle jest sens rozmawiać dalej.</p>
    </div>
  </section>

  <section class="kontakt" id="kontakt">
    <div class="kontakt__in">
      <div class="kontakt__lewa">
        <h2>Napisz do mnie</h2>
        <p>Najszybciej odpowiem na wiadomość z formularza. Wystarczy nazwa marki i jedno zdanie o tym, czego potrzebujesz.</p>
        <ul class="kontakt__lista">
          <li>Odpowiadam w ciągu 24 godzin w dni robocze</li>
          <li>Rozmowa nie zobowiązuje do niczego</li>
          <li>Jeśli to nie moja działka, powiem wprost</li>
        </ul>
        <p class="kontakt__bezpo">Wolisz mailem? Napisz na <a href="mailto:kontakt@maciejraciborski.pl">kontakt@maciejraciborski.pl</a></p>
      </div>

      <form class="formularz" id="formularz" action="mailto:kontakt@maciejraciborski.pl" method="post" enctype="text/plain" novalidate>
        <label>Imię i firma
          <input type="text" name="imie" required autocomplete="name" placeholder="Jan Kowalski, Marka sp. z o.o.">
        </label>
        <label>Telefon lub e-mail
          <input type="text" name="kontakt" required autocomplete="email" placeholder="600 000 000 albo jan@firma.pl">
        </label>
        <label>Czego potrzebujesz?
          <textarea name="wiadomosc" rows="4" placeholder="Krótko: co za marka, co chcecie osiągnąć"></textarea>
        </label>
        <button type="submit" class="btn btn--pelny btn--szeroki">Wyślij zgłoszenie</button>
        <p class="formularz__info" id="formularz-info" role="status"></p>
      </form>
    </div>
  </section>

  <section class="faq">
    <div class="sekcja__glowa">
      <p class="proces__nad">Zanim napiszesz</p>
      <h2>Częste pytania</h2>
    </div>
    <div class="faq__lista">
      <details class="faq__poz">
        <summary>Ile trwa współpraca?</summary>
        <p>Pracuję długofalowo. Pierwsze efekty w social mediach widać po kilku miesiącach regularnej publikacji - krótsze współprace zwykle nie mają sensu dla żadnej ze stron.</p>
      </details>
      <details class="faq__poz">
        <summary>Czy muszę być na zdjęciach?</summary>
        <p>Nie musisz. Część marek buduje obecność na produkcie, wnętrzu albo pracy zespołu. Ustalamy to na początku, przy kierunku.</p>
      </details>
      <details class="faq__poz">
        <summary>Ile czasu to zajmie po mojej stronie?</summary>
        <p>Zdjęcia grupuję w bloki, żeby nie zajmować Ci czasu co tydzień. Poza dniami zdjęciowymi po Twojej stronie zostaje akceptacja kierunku.</p>
      </details>
      <details class="faq__poz">
        <summary>Czy robisz pojedyncze filmy?</summary>
        <p>Wyjątkowo. Moja praca opiera się na konsekwencji, a jeden materiał nie zmienia obecności marki - dlatego domyślnie proponuję współpracę stałą.</p>
      </details>
    </div>
  </section>
</main>
'''
    t += stopka("../")
    return t


# ══════════════════════════════════════════════════════════════════════════
def main():
    (KAT / "index.html").write_text(sklej(strona_glowna()), encoding="utf-8")

    for nazwa, gen in [("realizacje", strona_realizacje), ("o-mnie", strona_o_mnie),
                       ("wspolpraca", strona_wspolpraca), ("kontakt", strona_kontakt)]:
        d = KAT / nazwa
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(sklej(gen()), encoding="utf-8")
        print(f"  ✓ {nazwa}/index.html")

    print(f"  ✓ index.html")
    print(f"\nGotowe. Wersja zasobów: v{WERSJA}")


if __name__ == "__main__":
    main()
