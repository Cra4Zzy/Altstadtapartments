from pathlib import Path
import re, json

ROOT = Path('.')
BASE = 'https://altstadtapartments-dinkelsbuehl.de'
HERO = 'https://le-de.cdn-website.com/e35529a37aa04f9483de0850a03a6db2/dms3rep/multi/opt/808983347-1920w.jpg'
HTML_FILES = ['index.html','altstadtapartment.html','designapartment.html','dinkelsbuehl.html','buchen.html','impressum.html','datenschutz.html','agb.html']
LABELS = {
    'altstadtapartment.html':'AltstadtApartment', 'designapartment.html':'DesignApartment',
    'dinkelsbuehl.html':'Dinkelsbühl erleben', 'buchen.html':'Verfügbarkeit & Buchung',
    'impressum.html':'Impressum', 'datenschutz.html':'Datenschutz', 'agb.html':'Buchungshinweise'
}

SOCIAL_MARK='<!-- SEO-GEO-SOCIAL -->'
BREAD_MARK='<!-- SEO-GEO-BREADCRUMB -->'
HOME_MARK='<!-- SEO-GEO-HOME-UPGRADE -->'
BOOK_MARK='<!-- SEO-GEO-BOOKING-UPGRADE -->'

def read(p): return (ROOT/p).read_text(encoding='utf-8')
def write(p,s): (ROOT/p).write_text(s,encoding='utf-8')

def attr(text, pattern, default=''):
    m=re.search(pattern,text,re.I|re.S)
    return re.sub(r'\s+',' ',m.group(1)).strip() if m else default

def canonical(filename): return BASE+'/' if filename=='index.html' else f'{BASE}/{filename}'

def inject_social(filename):
    text=read(filename)
    if SOCIAL_MARK in text: return
    title=attr(text,r'<title>(.*?)</title>','AltstadtApartments Dinkelsbühl')
    desc=attr(text,r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']')
    if not desc:
        desc=attr(text,r'<meta[^>]+content=["\'](.*?)["\'][^>]+name=["\']description["\']')
    url=canonical(filename)
    block=f'''{SOCIAL_MARK}<meta name="robots" content="index,follow,max-image-preview:large"><link rel="preconnect" href="https://le-de.cdn-website.com" crossorigin><meta property="og:type" content="website"><meta property="og:locale" content="de_DE"><meta property="og:site_name" content="AltstadtApartments Dinkelsbühl"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{url}"><meta property="og:image" content="{HERO}"><meta property="og:image:alt" content="AltstadtApartments Dinkelsbühl – Ferienwohnung in der historischen Altstadt"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{desc}"><meta name="twitter:image" content="{HERO}">'''
    text=text.replace('</head>',block+'</head>',1)
    write(filename,text)

def inject_breadcrumb(filename):
    if filename=='index.html': return
    text=read(filename)
    if BREAD_MARK in text: return
    label=LABELS[filename]
    nav=f'''{BREAD_MARK}<nav class="breadcrumbs wrap" aria-label="Breadcrumb"><a href="index.html">Startseite</a><span aria-hidden="true">/</span><span aria-current="page">{label}</span></nav>'''
    text=text.replace('<main id="inhalt">','<main id="inhalt">'+nav,1)
    write(filename,text)

for f in HTML_FILES:
    inject_social(f)
    inject_breadcrumb(f)

text=read('index.html')
if HOME_MARK not in text:
    org={
      '@context':'https://schema.org','@type':'Organization','@id':BASE+'/#organization',
      'name':'AltstadtApartments Dinkelsbühl','url':BASE+'/','telephone':'+491711228765',
      'email':'stollenmeierk@yahoo.de','founder':{'@type':'Person','name':'Kurt Stollenmeier'},
      'areaServed':{'@type':'City','name':'Dinkelsbühl'}
    }
    org_script='<script type="application/ld+json">'+json.dumps(org,ensure_ascii=False,separators=(',',':'))+'</script>'
    text=text.replace('</head>',org_script+'</head>',1)
    direct='''<!-- SEO-GEO-HOME-UPGRADE --><section class="direct-booking" id="direkt-buchen"><div class="wrap direct-booking__grid"><div data-reveal><p class="eyebrow">Direkt statt Umweg</p><h2>Direkt bei uns buchen.<br><i>Persönlicher ankommen.</i></h2></div><div class="direct-booking__copy" data-reveal><p>Wenn Sie direkt über AltstadtApartments buchen, bleiben Anfrage und Aufenthalt in einer Hand: ohne Umweg über große Buchungsportale, mit persönlichem Kontakt zu Kurt Stollenmeier und fairen Direktkonditionen.</p><div class="direct-booking__benefits"><div><span>01</span><b>Keine Plattformgebühren</b><p>Direkt buchen und unnötige Vermittlungswege vermeiden.</p></div><div><span>02</span><b>Persönlicher Kontakt</b><p>Fragen zu Anreise, Parken oder Aufenthalt direkt mit dem Gastgeber klären.</p></div><div><span>03</span><b>Faire Konditionen</b><p>Verfügbarkeit und konkrete Konditionen transparent im Buchungsprozess prüfen.</p></div></div><a class="button" href="buchen.html">Direkt Verfügbarkeit prüfen <span aria-hidden="true">↗</span></a></div></div></section>'''
    text=text.replace('<section class="slow-section">',direct+'<section class="slow-section">',1)
    trust='''<section class="review-proof" id="bewertungen"><div class="wrap review-proof__grid"><div data-reveal><p class="eyebrow">Echte Erfahrungen zählen</p><h2>Von Gästen<br><i>bereits bewertet.</i></h2></div><div data-reveal><p class="review-proof__copy">Die AltstadtApartments werden bereits auf Buchungsplattformen bewertet. Für die Live-Seite können ausgewählte Original-Gästestimmen mit eindeutiger Quellenangabe eingebunden werden – transparent und ohne erfundene Testimonials.</p><div class="review-source"><strong>Booking.com</strong><span>Originalbewertungen als Vertrauenssignal vorgesehen</span></div></div></div></section><section class="host-section"><div class="wrap host-section__grid"><div data-reveal><p class="eyebrow">Ihr Gastgeber</p><h2>Persönlich für Sie da.<br><i>Kurt Stollenmeier.</i></h2></div><div data-reveal><p>Vom ersten Kontakt bis zur Anreise haben Sie einen direkten Ansprechpartner. Fragen zu Parkplatz, Check-in oder Aufenthalt lassen sich persönlich und unkompliziert klären.</p><a class="text-link" href="tel:+491711228765">0171 122 87 65 <span aria-hidden="true">↗</span></a></div></div></section>'''
    text=text.replace('<section class="faq-section',trust+'<section class="faq-section',1)
    write('index.html',text)

text=read('buchen.html')
if BOOK_MARK not in text:
    block='''<!-- SEO-GEO-BOOKING-UPGRADE --><section class="booking-trust wrap" aria-label="Vorteile der Direktbuchung"><div><b>Direktkonditionen</b><p>Ohne Umweg über große Buchungsportale und ohne zusätzliche Plattformgebühren.</p></div><div><b>Persönlicher Ansprechpartner</b><p>Kurt Stollenmeier unterstützt Sie bei Fragen rund um Ihren Aufenthalt.</p></div><div><b>Klare Verfügbarkeit</b><p>Freie Termine und die konkreten Konditionen direkt für Ihr Wunsch-Apartment prüfen.</p></div></section>'''
    text=text.replace('</main>',block+'</main>',1)
    write('buchen.html',text)

css_path='assets/css/style.css'; css=read(css_path)
if '/* SEO-GEO-THEMES */' not in css:
    css += r'''
/* SEO-GEO-THEMES */
:root[data-theme="warm"]{--navy:#5b3b30;--navy-dark:#3b2822;--paper:#fbf7ef;--sand:#efe4d7;--copper:#b96f50;--ink:#322b27;--muted:#746b64;--line:#ddd3c8}
:root[data-theme="nature"]{--navy:#26483f;--navy-dark:#18352f;--paper:#f7f4ea;--sand:#e4e9df;--copper:#ae8a57;--ink:#283630;--muted:#68756f;--line:#d1d9d2}
:root[data-theme="elegant"]{--navy:#303238;--navy-dark:#202228;--paper:#f7f5f1;--sand:#e8e5df;--copper:#9b715e;--ink:#26282c;--muted:#6d6e73;--line:#d7d4cf}
:root[data-theme="warm"] .hero-copy h1 i,:root[data-theme="warm"] .slow-copy h2 i{color:#e2c2a7}:root[data-theme="nature"] .hero-copy h1 i,:root[data-theme="nature"] .slow-copy h2 i{color:#d7c69b}:root[data-theme="elegant"] .hero-copy h1 i,:root[data-theme="elegant"] .slow-copy h2 i{color:#d8c3ba}
.theme-preview{position:fixed;left:18px;bottom:18px;z-index:160;width:min(390px,calc(100vw - 36px));background:rgba(255,255,255,.94);color:#242729;border:1px solid rgba(20,25,28,.14);box-shadow:0 18px 60px rgba(0,0,0,.2);backdrop-filter:blur(16px);padding:12px;border-radius:18px}.theme-preview__top{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:2px 4px 10px}.theme-preview__top strong{font-size:.72rem;letter-spacing:.12em;text-transform:uppercase}.theme-preview__top span{font-size:.68rem;color:#6d7376}.theme-preview__options{display:grid;grid-template-columns:repeat(3,1fr);gap:7px}.theme-preview button{appearance:none;border:1px solid #dadbda;background:#fff;color:#333;padding:10px 7px;border-radius:12px;font-size:.72rem;line-height:1.25}.theme-preview button[aria-pressed="true"]{border-color:#222;box-shadow:inset 0 0 0 1px #222}.theme-preview button:before{content:'';display:block;width:100%;height:8px;border-radius:99px;margin-bottom:7px;background:var(--swatch)}.theme-preview button[data-set-theme="warm"]{--swatch:linear-gradient(90deg,#5b3b30 0 33%,#b96f50 33% 66%,#fbf7ef 66%)}.theme-preview button[data-set-theme="nature"]{--swatch:linear-gradient(90deg,#26483f 0 33%,#ae8a57 33% 66%,#f7f4ea 66%)}.theme-preview button[data-set-theme="elegant"]{--swatch:linear-gradient(90deg,#303238 0 33%,#9b715e 33% 66%,#f7f5f1 66%)}
.direct-booking{background:var(--paper);padding-block:clamp(70px,8vw,120px);border-block:1px solid var(--line)}.direct-booking__grid{display:grid;grid-template-columns:.9fr 1.35fr;gap:8vw;align-items:start}.direct-booking h2 i{color:var(--copper)}.direct-booking__copy>p{color:var(--muted);max-width:720px;font-size:1.03rem}.direct-booking__benefits{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:var(--line);border:1px solid var(--line);margin-top:34px}.direct-booking__benefits div{background:var(--paper);padding:24px}.direct-booking__benefits span{display:block;font-family:var(--serif);font-size:2rem;color:var(--copper);line-height:1;margin-bottom:14px}.direct-booking__benefits b{display:block;font-size:.9rem;margin-bottom:6px}.direct-booking__benefits p{font-size:.78rem;line-height:1.6;color:var(--muted)}.direct-booking .button{margin-top:28px}
.review-proof{background:var(--sand);padding-block:clamp(65px,7vw,105px)}.review-proof__grid,.host-section__grid{display:grid;grid-template-columns:1fr 1.35fr;gap:8vw;align-items:center}.review-proof__copy,.host-section__grid>div:last-child>p{font-size:1.02rem;color:var(--muted);max-width:700px}.review-source{display:flex;align-items:center;justify-content:space-between;gap:20px;border-top:1px solid var(--line);margin-top:28px;padding-top:20px}.review-source strong{font-family:var(--serif);font-size:1.35rem}.review-source span{font-size:.75rem;color:var(--muted);text-align:right}.host-section{padding-block:clamp(65px,7vw,105px);background:var(--paper)}.host-section h2 i{color:var(--copper)}.host-section .text-link{margin-top:26px}.breadcrumbs{display:flex;flex-wrap:wrap;gap:9px;align-items:center;padding-top:24px;margin-bottom:0;font-size:.72rem;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}.breadcrumbs a{border-bottom:1px solid transparent}.breadcrumbs a:hover{border-color:currentColor}.breadcrumbs span[aria-hidden]{opacity:.5}.booking-trust{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:var(--line);border:1px solid var(--line);margin-bottom:clamp(55px,7vw,90px)}.booking-trust>div{background:var(--paper);padding:24px}.booking-trust b{display:block;margin-bottom:7px}.booking-trust p{font-size:.8rem;line-height:1.6;color:var(--muted)}
@media(max-width:800px){.direct-booking__grid,.review-proof__grid,.host-section__grid{grid-template-columns:1fr;gap:32px}.direct-booking__benefits,.booking-trust{grid-template-columns:1fr}.review-source{align-items:flex-start;flex-direction:column}.review-source span{text-align:left}.theme-preview{left:12px;bottom:12px;width:calc(100vw - 24px)}.theme-preview__top span{display:none}}@media print{.theme-preview{display:none!important}}
'''
    write(css_path,css)

js_path='assets/js/main.js'; js=read(js_path)
if 'SEO-GEO-THEME-PREVIEW' not in js:
    js += r'''
;(() => {
  'use strict';
  // SEO-GEO-THEME-PREVIEW
  const themes={warm:{label:'Warm & historisch',color:'#5b3b30'},nature:{label:'Natur & ruhig',color:'#26483f'},elegant:{label:'Elegant & klar',color:'#303238'}};
  const params=new URLSearchParams(location.search),requested=params.get('theme'),stored=localStorage.getItem('altstadt-theme');
  let active=themes[requested]?requested:(themes[stored]?stored:'warm');
  const apply=(theme,updateUrl=false)=>{active=theme;document.documentElement.dataset.theme=theme;localStorage.setItem('altstadt-theme',theme);const meta=document.querySelector('meta[name="theme-color"]');if(meta)meta.content=themes[theme].color;if(updateUrl){const u=new URL(location.href);u.searchParams.set('theme',theme);history.replaceState(null,'',u)}document.querySelectorAll('[data-set-theme]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.setTheme===theme)))};
  apply(active);
  const preview=location.hostname.includes('github.io')||['localhost','127.0.0.1'].includes(location.hostname)||location.protocol==='file:';
  if(!preview)return;
  const box=document.createElement('aside');box.className='theme-preview';box.setAttribute('aria-label','Farbvarianten für die Kundenabstimmung');box.innerHTML='<div class="theme-preview__top"><strong>Farbwelt auswählen</strong><span>Live-Vorschau</span></div><div class="theme-preview__options">'+Object.entries(themes).map(([k,v])=>`<button type="button" data-set-theme="${k}">${v.label}</button>`).join('')+'</div>';document.body.append(box);box.addEventListener('click',e=>{const b=e.target.closest('[data-set-theme]');if(b)apply(b.dataset.setTheme,true)});apply(active);
})();
'''
    write(js_path,js)

Path('llms.txt').write_text('''# AltstadtApartments Dinkelsbühl\n\n> Zwei Ferienwohnungen in der historischen Altstadt von Dinkelsbühl. Persönlicher Ansprechpartner: Kurt Stollenmeier.\n\n## Wichtigste Seiten\n- https://altstadtapartments-dinkelsbuehl.de/ — Übersicht beider Ferienwohnungen\n- https://altstadtapartments-dinkelsbuehl.de/altstadtapartment.html — AltstadtApartment, 80 m², bis zu 4 Gäste\n- https://altstadtapartments-dinkelsbuehl.de/designapartment.html — DesignApartment, 85 m², bis zu 6 Gäste\n- https://altstadtapartments-dinkelsbuehl.de/dinkelsbuehl.html — Dinkelsbühl und Umgebung\n- https://altstadtapartments-dinkelsbuehl.de/buchen.html — Verfügbarkeit und Direktbuchung\n\n## Fakten\n- Historische Altstadt von Dinkelsbühl\n- Kostenloses WLAN\n- Eigene voll ausgestattete Küche in beiden Apartments\n- Kostenlose Parkmöglichkeiten laut Gastgeber in etwa 5 Gehminuten\n- Direkter Kontakt: +49 171 1228765 / stollenmeierk@yahoo.de\n\nPreise und Verfügbarkeiten sind dynamisch und ausschließlich über den Buchungsprozess bzw. die Buchungsbestätigung verbindlich.\n''',encoding='utf-8')
Path('SEO-LAUNCH-CHECKLIST.md').write_text('''# SEO / GEO Launch-Checkliste\n\n## Im Preview technisch umgesetzt\n- Titles, Meta-Descriptions, Canonicals\n- Open Graph + Twitter Cards\n- bestehendes LodgingBusiness-/Apartment-/FAQ-Schema plus Organization-Identität\n- Breadcrumbs auf Unterseiten\n- Direktbuchungs-Vorteile als zitierbarer Text\n- Gastgeber-/Vertrauensbereich\n- FAQ als klare Frage-Antwort-Inhalte\n- CDN-Preconnect, vorhandene Alt-Texte/Lazy Loading\n- drei Farbvarianten im GitHub-Pages-Preview\n- llms.txt (experimentell)\n- Sitemap + robots.txt\n\n## Für den Livegang / mit Kundenzugang\n1. Google Search Console verifizieren und sitemap.xml einreichen.\n2. Bing Webmaster Tools verifizieren und Sitemap einreichen.\n3. Apartmentbilder vom alten cdn-website.com auf dauerhaftes eigenes Hosting migrieren und responsive WebP/AVIF-Varianten erzeugen.\n4. Freigegebene Booking-/Google-Bewertungslinks oder Originalzitate liefern; danach Bewertungsbereich finalisieren und nur bei belastbaren Daten aggregateRating auszeichnen.\n5. Exakte Objektadressen der Apartments nur nach Kundenbestätigung ins Apartment-Schema aufnehmen.\n6. Foto von Kurt Stollenmeier ergänzen, sobald freigegeben.\n7. NAP-Daten auf Google Business, Booking.com, Tripadvisor und regionalen Portalen vereinheitlichen.\n8. Tourist-Info Dinkelsbühl, FrankenTourismus und Romantische Straße wegen Listung/Backlink anfragen.\n''',encoding='utf-8')
Path('robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: https://altstadtapartments-dinkelsbuehl.de/sitemap.xml\n',encoding='utf-8')

pages=['','altstadtapartment.html','designapartment.html','dinkelsbuehl.html','buchen.html','impressum.html','datenschutz.html','agb.html']
urls=[]
for page in pages:
    loc=BASE+'/'+page
    freq='weekly' if page in ('','buchen.html') else 'monthly'
    priority='1.0' if page=='' else ('0.9' if 'apartment' in page else '0.7')
    urls.append(f'  <url><loc>{loc}</loc><lastmod>2026-09-13</lastmod><changefreq>{freq}</changefreq><priority>{priority}</priority></url>')
Path('sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+'\n'.join(urls)+'\n</urlset>\n',encoding='utf-8')

print('AltstadtApartments SEO/GEO upgrade applied.')
