from pathlib import Path
import re

root = Path('.')
core = ['index.html','altstadtapartment.html','designapartment.html','dinkelsbuehl.html','buchen.html']

# Fix remaining German booking-page fact first.
buchen = root/'buchen.html'
text = buchen.read_text(encoding='utf-8')
text = text.replace('1 Schlafzimmer · eigene Küche · WLAN','2 Schlafzimmer · eigene Küche · WLAN')
buchen.write_text(text,encoding='utf-8')

# Language metadata + switcher hooks for German pages.
def add_de_meta(html, filename):
    de_url = 'https://altstadtapartments-dinkelsbuehl.de/' if filename=='index.html' else f'https://altstadtapartments-dinkelsbuehl.de/{filename}'
    en_url = 'https://altstadtapartments-dinkelsbuehl.de/en/' if filename=='index.html' else f'https://altstadtapartments-dinkelsbuehl.de/en/{filename}'
    if 'hreflang="de"' not in html:
        html = html.replace('</head>', f'<link rel="alternate" hreflang="de" href="{de_url}"><link rel="alternate" hreflang="en" href="{en_url}"><link rel="alternate" hreflang="x-default" href="{de_url}"><script src="assets/js/language.js" defer></script></head>',1)
    return html

for filename in core:
    p=root/filename
    html=p.read_text(encoding='utf-8')
    p.write_text(add_de_meta(html,filename),encoding='utf-8')

# Translation dictionary for visible copy. This is intentionally explicit rather than machine-translated at runtime.
repl = {
    'lang="de"':'lang="en"',
    'Zum Inhalt springen':'Skip to content',
    'Die Apartments':'Apartments',
    'Dinkelsbühl erleben':'Discover Dinkelsbühl',
    'Gut zu wissen':'Good to know',
    'Aufenthalt planen':'Plan your stay',
    'Startseite':'Home',
    'Kontakt':'Contact',
    'Zur Startseite':'Back to home',
    'Alle Apartments':'All apartments',
    'FERIENWOHNUNGEN IN DINKELSBÜHL':'HOLIDAY APARTMENTS IN DINKELSBÜHL',
    'Altstadt draußen.':'Old town outside.',
    'Ankommen<br>drinnen.':'Feel at home<br>inside.',
    'Morgens durch historische Gassen schlendern.<br>Abends die Tür zum eigenen Lieblingsplatz öffnen.':'Stroll through historic lanes in the morning.<br>Come home to your own favourite place in the evening.',
    'Ihr Apartment entdecken':'Discover your apartment',
    'Zwei Apartments. Mitten in der Altstadt.':'Two apartments. Right in the old town.',
    'Einfach mal bleiben':'Stay a little longer',
    'Historische Altstadt':'Historic old town',
    'Für 1–6 Gäste je nach Apartment':'For 1–6 guests depending on apartment',
    'Eigene Küche &amp; WLAN':'Private kitchen &amp; Wi-Fi',
    'Verfügbarkeit prüfen':'Check availability',
    'Ihr Zuhause auf Zeit':'Your home away from home',
    'Nicht nur zu Besuch.':'More than a visit.',
    'Ein bisschen zu Hause.':'A little like home.',
    'Ein Städtetrip zu zweit, gemeinsame Tage mit der Familie oder eine berufliche Reise: In unseren Ferienwohnungen in Dinkelsbühl wohnen Sie zentral und gestalten Ihren Tag in Ihrem eigenen Rhythmus.':'A city break for two, time with the family or a business trip: our apartments put you right in the heart of Dinkelsbühl, with the freedom to set your own pace.',
    'Restaurants, Cafés und Sehenswürdigkeiten liegen in der Altstadt. Und drinnen? Platz zum Zurückziehen, eine eigene Küche und Zeit füreinander.':'Restaurants, cafés and sights are all in the old town. Inside, you have space to unwind, your own kitchen and time together.',
    'Zwei Adressen fürs Wohlfühlen':'Two places to feel at home',
    'Welches passt<br><i>zu Ihrer Auszeit?</i>':'Which one fits<br><i>your stay?</i>',
    'Kleinere Runde oder mehr Platz für alle.<br>Entdecken Sie unsere beiden Apartments.':'A cosy stay for a few or extra room for everyone.<br>Discover our two apartments.',
    'Charmant &amp; gemütlich':'Charming &amp; cosy',
    'Großzügig &amp; individuell':'Spacious &amp; individual',
    'Bis zu <b>4 Gäste</b>':'Up to <b>4 guests</b>',
    'Bis zu <b>6 Gäste</b>':'Up to <b>6 guests</b>',
    '<b>2 Schlafzimmer</b>':'<b>2 bedrooms</b>',
    '<b>3 Schlafzimmer</b>':'<b>3 bedrooms</b>',
    '<b>1 Badezimmer</b>':'<b>1 bathroom</b>',
    'Das Apartment ansehen':'View apartment',
    'AltstadtApartment entdecken':'Discover AltstadtApartment',
    'DesignApartment entdecken':'Discover DesignApartment',
    'Direkt statt Umweg':'Book direct',
    'Direkt bei uns buchen.':'Book directly with us.',
    'Persönlicher ankommen.':'A more personal stay.',
    'Keine Plattformgebühren':'No platform fees',
    'Persönlicher Kontakt':'Personal contact',
    'Faire Konditionen':'Fair direct rates',
    'Direkt Verfügbarkeit prüfen':'Check direct availability',
    'Kleine Dinge. Gute Tage.':'Small things. Good days.',
    'Kein fester Takt.':'No fixed schedule.',
    'Nur Ihrer.':'Only yours.',
    'Dinkelsbühl. Direkt vor der Tür.':'Dinkelsbühl. Right outside.',
    'Gassen voller Geschichte.':'Lanes full of history.',
    'Tage voller Möglichkeiten.':'Days full of possibilities.',
    'Dinkelsbühl entdecken':'Discover Dinkelsbühl',
    'Gästestimmen':'Guest reviews',
    'Was Gäste<br><i>über den Aufenthalt sagen.</i>':'What guests<br><i>say about their stay.</i>',
    'Ihr Gastgeber':'Your host',
    'Persönlich für Sie da.':'Personally here for you.',
    'Vor der Reise<br><i>noch eine Frage?</i>':'A question<br><i>before your trip?</i>',
    'Vorfreude beginnt mit einem Hallo.':'Your stay starts with hello.',
    'Eine Frage?':'Any questions?',
    'Sehr gerne.':'Gladly.',
    'FERIENWOHNUNG IN DINKELSBÜHL ALTSTADT':'HOLIDAY APARTMENT IN DINKELSBÜHL OLD TOWN',
    'Charmant wohnen. Zentral ankommen.':'Charming living. Central location.',
    'Großzügig wohnen. Gemeinsam ankommen.':'Spacious living. Arrive together.',
    'Wohnfläche':'living space',
    'Gäste':'guests',
    'Schlafzimmer':'bedrooms',
    'Badezimmer':'bathroom',
    'Bild vergrößern':'Enlarge image',
    'Alle 7 Bilder ansehen':'View all 7 photos',
    'Alle Bilder ansehen':'View all photos',
    'Das erwartet Sie':'What to expect',
    'Voll ausgestattete Küche':'Fully equipped kitchen',
    'Kostenloses WLAN':'Free Wi-Fi',
    'Zentrale Altstadtlage':'Central old-town location',
    'Ein eigenes Badezimmer':'Private bathroom',
    'Kostenlose Parkplätze in ca. 5 Gehminuten':'Free parking around a 5-minute walk away',
    'Ankommen &amp; Abreisen':'Arrival &amp; departure',
    'Vorfreude reservieren':'Reserve your stay',
    'Freie Termine und aktuelle Preise sehen Sie in unserer Buchung.':'See available dates and current prices in our booking system.',
    'Weiter zur Buchung bei Smoobu':'Continue to Smoobu booking',
    'Lieber persönlich fragen?':'Prefer to ask us directly?',
    'Von Gästen bestätigt':'Confirmed by guests',
    'Sehr gut bewertet':'Very well rated',
    'Lage':'Location',
    'Quelle: Booking.com · Bewertungsstand 2026':'Source: Booking.com · 2026 rating status',
    'Quelle: Booking.com · Lagebewertung':'Source: Booking.com · location rating',
    'Ein erster Blick nach drinnen':'A first look inside',
    'So wohnen <i>Sie hier.</i>':'Your <i>home here.</i>',
    'Mitten in Dinkelsbühl':'In the heart of Dinkelsbühl',
    'Altstadt vor der Tür.':'Old town at your doorstep.',
    'Kurze Wege inklusive.':'Everything close by.',
    'Noch eine Möglichkeit':'Another option',
    'Mehr Platz für Ihre Reise?':'Need more space for your stay?',
    'Etwas kompakter unterwegs?':'Looking for something more compact?',
    'Dinkelsbühl · Romantische Straße':'Dinkelsbühl · Romantic Road',
    'Eine Altstadt,':'An old town',
    'die bleibt.':'to remember.',
    'Einfach losgehen':'Simply start walking',
    'Historisch schön.':'Beautifully historic.',
    'Herrlich unkompliziert.':'Wonderfully easy.',
    'Altstadt':'Old town',
    'Gassen, Türme &amp; Fachwerk.':'Lanes, towers &amp; timber framing.',
    'Romantische Straße':'Romantic Road',
    'Ein besonderer Zwischenstopp.':'A special stop along the way.',
    'Tradition':'Tradition',
    'Kinderzeche &amp; Stadtgeschichte.':'Kinderzeche &amp; local history.',
    'Ihr Ausgangspunkt':'Your starting point',
    'Mittendrin statt unterwegs.':'Stay right in the middle of it all.',
    'Ihre Auszeit beginnt hier':'Your stay starts here',
    'Welches darf<br><i>es für Sie sein?</i>':'Which apartment<br><i>will it be?</i>',
    'Termine &amp; Preise prüfen':'Check dates &amp; prices',
    'Öffnet die bestehende Smoobu-Buchung':'Opens the existing Smoobu booking',
    'Apartment vorher ansehen':'View apartment first',
    'Direktkonditionen':'Direct-booking rates',
    'Persönlicher Ansprechpartner':'Personal contact',
    'Klare Verfügbarkeit':'Clear availability',
    'Entdecken':'Explore',
    'Verfügbarkeit &amp; Buchung':'Availability &amp; booking',
    'Persönlich für Sie da':'Here for you personally',
    'Buchungsbedingungen':'Booking terms',
    'Impressum':'Legal notice',
    'Datenschutz':'Privacy',
}

# Translate generated English copies and fix paths/meta.
en_dir=root/'en'; en_dir.mkdir(exist_ok=True)
for filename in core:
    html=(root/filename).read_text(encoding='utf-8')
    for a,b in repl.items(): html=html.replace(a,b)
    # path fixes for assets and cross-language links
    html=html.replace('href="assets/','href="../assets/').replace('src="assets/','src="../assets/')
    html=html.replace('href="index.html','href="index.html').replace('href="../','href="../')
    # legal pages remain German but are accessible from English footer
    html=html.replace('href="impressum.html"','href="../impressum.html"').replace('href="datenschutz.html"','href="../datenschutz.html"').replace('href="agb.html"','href="../agb.html"')
    # canonical + alternates
    de_url='https://altstadtapartments-dinkelsbuehl.de/' if filename=='index.html' else f'https://altstadtapartments-dinkelsbuehl.de/{filename}'
    en_url='https://altstadtapartments-dinkelsbuehl.de/en/' if filename=='index.html' else f'https://altstadtapartments-dinkelsbuehl.de/en/{filename}'
    html=re.sub(r'<link rel="canonical" href="[^"]+">',f'<link rel="canonical" href="{en_url}">',html,1)
    html=re.sub(r'<link rel="alternate" hreflang="de"[^>]+><link rel="alternate" hreflang="en"[^>]+><link rel="alternate" hreflang="x-default"[^>]+>',f'<link rel="alternate" hreflang="de" href="{de_url}"><link rel="alternate" hreflang="en" href="{en_url}"><link rel="alternate" hreflang="x-default" href="{de_url}">',html,1)
    # point language JS one level up
    html=html.replace('src="assets/js/language.js"','src="../assets/js/language.js"')
    html=html.replace('src="../assets/js/main.js"','src="../assets/js/main.js"')
    # English OG locale
    html=html.replace('content="de_DE"','content="en_GB"')
    # English page URLs in OG URL if present
    html=re.sub(r'<meta property="og:url" content="[^"]+">',f'<meta property="og:url" content="{en_url}">',html,1)
    (en_dir/filename).write_text(html,encoding='utf-8')

# Shared language logic: browser language on first visit, persistent manual override, visible flags in header.
js = r'''(() => {
  'use strict';
  const KEY='altstadt-language';
  const path=location.pathname;
  const isEn=/\/en(?:\/|$)/.test(path);
  const current=isEn?'en':'de';
  const saved=localStorage.getItem(KEY);
  const browser=(navigator.languages&&navigator.languages[0]||navigator.language||'de').toLowerCase();
  const preferred=saved||(browser.startsWith('de')?'de':'en');
  const mapTo=(lang)=>{
    const clean=path.replace(/\/en\/?/,'/');
    if(lang==='en') return '/en'+(clean==='/'?'/':clean);
    return clean||'/';
  };
  if(!saved && preferred!==current && !location.search.includes('langstay=1')){
    location.replace(mapTo(preferred)+location.search+location.hash);return;
  }
  const header=document.querySelector('.site-header .header-actions');
  if(!header)return;
  const wrap=document.createElement('div');
  wrap.className='language-switch';
  wrap.setAttribute('aria-label',current==='de'?'Sprache wählen':'Choose language');
  wrap.innerHTML=`<button type="button" data-lang="de" aria-pressed="${current==='de'}" title="Deutsch"><span class="lang-flag" aria-hidden="true">🇩🇪</span><span>DE</span></button><span class="lang-divider" aria-hidden="true"></span><button type="button" data-lang="en" aria-pressed="${current==='en'}" title="English"><span class="lang-flag" aria-hidden="true">🇬🇧</span><span>EN</span></button>`;
  header.insertBefore(wrap,header.querySelector('.menu-button'));
  wrap.addEventListener('click',e=>{
    const b=e.target.closest('[data-lang]');if(!b)return;
    const lang=b.dataset.lang;localStorage.setItem(KEY,lang);
    if(lang!==current) location.href=mapTo(lang)+'?langstay=1';
  });
})();
'''
(root/'assets/js/language.js').write_text(js,encoding='utf-8')

# Header styling for flags / compact switcher.
css_path=root/'assets/css/style.css'; css=css_path.read_text(encoding='utf-8')
lang_css=r'''
/* LANGUAGE SWITCHER */
.language-switch{display:flex;align-items:center;gap:5px;height:34px;padding:3px 5px;border:1px solid rgba(255,255,255,.24);border-radius:999px;background:rgba(255,255,255,.06);backdrop-filter:blur(10px);margin-right:8px}.site-header.scrolled .language-switch{border-color:var(--line);background:rgba(255,255,255,.78)}.language-switch button{border:0;background:transparent;color:inherit;display:flex;align-items:center;gap:5px;padding:5px 7px;border-radius:999px;font:600 .67rem/1 var(--sans);letter-spacing:.05em;cursor:pointer;opacity:.58}.language-switch button[aria-pressed="true"]{background:rgba(255,255,255,.16);opacity:1}.site-header.scrolled .language-switch button[aria-pressed="true"]{background:var(--sand)}.lang-flag{font-size:.86rem;line-height:1}.lang-divider{width:1px;height:14px;background:currentColor;opacity:.18}@media(max-width:760px){.language-switch{height:32px;margin-right:2px}.language-switch button{padding:4px 5px;font-size:.61rem}.lang-flag{font-size:.78rem}.header-book{display:none}}
'''
if 'LANGUAGE SWITCHER' not in css: css += lang_css
css_path.write_text(css,encoding='utf-8')
