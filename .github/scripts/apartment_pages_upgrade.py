from pathlib import Path
import re, json

repo = Path('.')
css_path = repo / 'assets/css/style.css'
css = css_path.read_text(encoding='utf-8')

reviews = {
    'altstadtapartment.html': {
        'score':'8,5', 'count':'59', 'location':'9,7',
        'beds':'2 Schlafzimmer',
        'meta_old':'80 m², 1 Schlafzimmer, bis zu 4 Gäste',
        'meta_new':'80 m², 2 Schlafzimmer, bis zu 4 Gäste',
        'schema_old':'"numberOfBedrooms":1',
        'schema_new':'"numberOfBedrooms":2',
        'facts_old':'<span><b>1 Schlafzimmer</b></span><span><b>1 Badezimmer</b></span>',
        'facts_new':'<span><b>2 Schlafzimmer</b></span><span><b>1 Badezimmer</b></span>',
        'amenity_old':'<li>1 Schlafzimmer</li>',
        'amenity_new':'<li>2 Schlafzimmer</li>',
        'guest':'Janine',
        'quote':'Gäste heben besonders die zentrale Lage, die Sauberkeit, bequeme Betten und die vollständige Ausstattung hervor.'
    },
    'designapartment.html': {
        'score':'8,5', 'count':'44', 'location':'9,7',
        'beds':'3 Schlafzimmer',
        'guest':'Jutta',
        'quote':'Gelobt werden vor allem die zentrale Altstadtlage, die großzügige Aufteilung und der unkomplizierte Check-in.'
    }
}

for filename, data in reviews.items():
    path = repo / filename
    html = path.read_text(encoding='utf-8')
    if filename == 'altstadtapartment.html':
        html = html.replace(data['meta_old'], data['meta_new'])
        html = html.replace(data['schema_old'], data['schema_new'])
        html = html.replace(data['facts_old'], data['facts_new'])
        html = html.replace(data['amenity_old'], data['amenity_new'])

    # enrich Apartment schema if present; otherwise add a dedicated JSON-LD block
    schema = {
        '@context':'https://schema.org',
        '@type':'Apartment',
        'name':'AltstadtApartment Dinkelsbühl' if filename.startswith('altstadt') else 'DesignApartment Dinkelsbühl',
        'address':{'@type':'PostalAddress','streetAddress':'Nördlinger Straße 16','postalCode':'91550','addressLocality':'Dinkelsbühl','addressCountry':'DE'},
        'aggregateRating':{'@type':'AggregateRating','ratingValue':data['score'].replace(',','.'),'reviewCount':int(data['count']),'bestRating':'10','worstRating':'1'}
    }
    if 'DETAIL-TRUST-SCHEMA' not in html:
        html = html.replace('</head>', f'<!-- DETAIL-TRUST-SCHEMA --><script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script></head>', 1)

    trust = f'''<section class="detail-trust section-space"><div class="wrap detail-trust__grid"><div data-reveal><p class="eyebrow">Von Gästen bestätigt</p><h2>{data['score']} von 10.<br><i>Lage {data['location']}.</i></h2><p class="detail-trust__lead">Aktueller Bewertungsstand auf Booking.com · {data['count']} Bewertungen.</p></div><div class="detail-trust__cards" data-reveal><article><span class="detail-trust__score">{data['score']}</span><b>Sehr gut bewertet</b><p>{data['quote']}</p><small>Quelle: Booking.com · Bewertungsstand 2026</small></article><article><span class="detail-trust__score">{data['location']}</span><b>Lage</b><p>Nördlinger Straße 16 · mitten in Dinkelsbühl und ideal für Wege zu Fuß.</p><small>Quelle: Booking.com · Lagebewertung</small></article></div></div></section>'''

    if 'detail-trust section-space' not in html:
        html = html.replace('<section class="gallery-section section-space"', trust + '<section class="gallery-section section-space"', 1)

    # add location/conversion block before alternate apartment section
    location_block = '''<section class="detail-location"><div class="wrap detail-location__grid"><div data-reveal><p class="eyebrow">Mitten in Dinkelsbühl</p><h2>Altstadt vor der Tür.<br><i>Kurze Wege inklusive.</i></h2></div><div data-reveal><p>Die Apartments liegen in der Nördlinger Straße 16 in der historischen Altstadt. Restaurants, Cafés und viele Sehenswürdigkeiten lassen sich bequem zu Fuß erreichen.</p><div class="detail-location__facts"><span><b>Historische Altstadt</b> direkt vor der Tür</span><span><b>Parken</b> laut Gastgeber in etwa 5 Gehminuten</span><span><b>Persönlicher Kontakt</b> vor und während des Aufenthalts</span></div><a class="button button-outline" href="buchen.html">Aufenthalt planen <span aria-hidden="true">↗</span></a></div></div></section>'''
    if 'detail-location__grid' not in html:
        html = html.replace('<section class="other-apartment', location_block + '<section class="other-apartment', 1)

    path.write_text(html, encoding='utf-8')

extra = r'''
/* APARTMENT DETAIL UPGRADE */
.detail-trust{background:#f8f9fa;color:#202124}.detail-trust__grid{display:grid;grid-template-columns:.9fr 1.4fr;gap:8vw;align-items:start}.detail-trust h2{color:#202124}.detail-trust h2 i{color:#5f6368}.detail-trust__lead{color:#5f6368;max-width:480px;line-height:1.7}.detail-trust__cards{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}.detail-trust__cards article{background:#fff;border:1px solid #dadce0;border-radius:18px;padding:24px;box-shadow:0 1px 2px rgba(60,64,67,.07);min-height:220px;display:flex;flex-direction:column}.detail-trust__score{font-size:2.4rem;font-weight:600;line-height:1;color:#1a73e8;margin-bottom:14px}.detail-trust__cards b{font-size:.94rem;margin-bottom:10px}.detail-trust__cards p{color:#3c4043;font-size:.86rem;line-height:1.65}.detail-trust__cards small{margin-top:auto;color:#70757a;font-size:.68rem}.detail-location{background:var(--paper);padding-block:clamp(70px,8vw,115px);border-top:1px solid var(--line)}.detail-location__grid{display:grid;grid-template-columns:1fr 1.25fr;gap:8vw;align-items:start}.detail-location__grid>div:last-child>p{color:var(--muted);font-size:1.02rem;line-height:1.75}.detail-location__facts{display:grid;gap:12px;margin:28px 0}.detail-location__facts span{padding:16px 0;border-top:1px solid var(--line);font-size:.84rem;color:var(--muted)}.detail-location__facts b{color:var(--ink)}@media(max-width:800px){.detail-trust__grid,.detail-location__grid{grid-template-columns:1fr;gap:30px}.detail-trust__cards{grid-template-columns:1fr}}
'''
if 'APARTMENT DETAIL UPGRADE' not in css:
    css += extra
css_path.write_text(css, encoding='utf-8')
