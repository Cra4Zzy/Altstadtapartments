from pathlib import Path

root = Path('.')
files = list((root/'en').glob('*.html'))

replacements = {
    # Global/meta fragments
    ' · bis 4 guests':' · up to 4 guests',
    ' · bis 6 guests':' · up to 6 guests',
    'bis zu 4 guests':'up to 4 guests',
    'bis zu 6 guests':'up to 6 guests',
    'Private kitchen, WLAN und Originalbilder':'Private kitchen, free Wi-Fi and original photos',
    'Private kitchen, WLAN und Originalbilder.':'Private kitchen, free Wi-Fi and original photos.',
    'Verfügbarkeit & Buchung':'Availability & booking',
    'Verfügbarkeit &amp; Buchung':'Availability &amp; booking',
    '← Zur Home':'← Back to home',
    '01 / WILLKOMMEN':'01 / WELCOME',

    # Home: apartment cards
    'Old towncharme trifft auf Ihren eigenen Rückzugsort.':'Old-town charm meets your own private retreat.',
    'Heller Wohnbereich, warme Holzböden und kurze Wege nach draußen. Für entspannte Tage zu zweit oder mit der Familie.':'A bright living area, warm wooden floors and the old town just outside. Perfect for relaxed days as a couple or with the family.',
    'Zusammen unterwegs. Mit Raum für jeden.':'Travelling together. With space for everyone.',
    'Ein historisches Bürgerhaus, moderne Einrichtung und Platz für gemeinsame Tage. Ideal für Familien und kleine Gruppen.':'A historic townhouse, modern interiors and plenty of room to spend time together. Ideal for families and small groups.',

    # Home: direct booking
    'Wenn Sie direkt über AltstadtApartments buchen, bleiben Anfrage und Aufenthalt in einer Hand: ohne Umweg über große Buchungsportale, mit persönlichem Contact zu Kurt Stollenmeier und fairen Direct-booking rates.':'Book directly with AltstadtApartments and everything stays personal from enquiry to arrival: no detour through large booking portals, direct contact with Kurt Stollenmeier and transparent direct-booking rates.',
    'Direkt buchen und unnötige Vermittlungswege vermeiden.':'Book direct and avoid unnecessary booking-platform detours.',
    'Persönlicher Contact':'Personal contact',
    'Fragen zu Anreise, Parken oder Aufenthalt direkt mit dem Gastgeber klären.':'Ask the host directly about arrival, parking or anything related to your stay.',
    'Verfügbarkeit und konkrete Konditionen transparent im Buchungsprozess prüfen.':'Check availability and the exact conditions transparently during the booking process.',
    'Direkt Check availability':'Check direct availability',

    # Home: slow living
    'Den Kaffee noch in Ruhe austrinken. Frische Zutaten mitbringen und zusammen kochen. Oder einfach die Stadt auf sich wirken lassen.':'Take your time over coffee. Pick up fresh ingredients and cook together. Or simply let the town set the pace.',
    'Kochen, wann Sie möchten.':'Cook whenever you like.',
    'Eine voll ausgestattete Küche in jedem Apartment.':'A fully equipped kitchen in every apartment.',
    'Verbunden bleiben.':'Stay connected.',
    'Free Wi-Fi ist in beiden Wohnungen dabei.':'Free Wi-Fi is included in both apartments.',
    'Das Auto auch mal stehen lassen.':'Leave the car behind.',
    'Kostenlose Parkplätze in etwa fünf Gehminuten.':'Free parking is available around a five-minute walk away.',
    'Küche und großer Esstisch im DesignApartment':'Kitchen and large dining table in the DesignApartment',
    'Für den ersten Kaffee. Und lange Gespräche.':'For the first coffee of the day. And long conversations.',
    'bedrooms des DesignApartments mit grünen Textilien':'Bedroom in the DesignApartment with green textiles',
    'Und dann: ausschlafen.':'And then: sleep in.',

    # Home: town/event
    'Fachwerk, historische Plätze und eine erhaltene Stadtmauer: Dinkelsbühl an der Romantischen Straße lädt dazu ein, einfach loszugehen. Die Old town ist Ihre Nachbarschaft auf Zeit.':'Timber-framed houses, historic squares and a preserved town wall: Dinkelsbühl on the Romantic Road invites you to simply start walking. The old town becomes your neighbourhood for a while.',
    'Old townbummel':'Old-town stroll',
    'Gemeinsame Auszeit':'Time away together',
    'Ausflugstipp 2026':'2026 day-trip tip',
    'Vom <strong>24. April bis 4. Oktober 2026</strong> findet in Ellwangen die Landesgartenschau statt. Für guests der AltstadtApartments ist sie ein attraktives zusätzliches Ausflugsziel während eines Aufenthalts in der Region.':'From <strong>24 April to 4 October 2026</strong>, Ellwangen hosts the Landesgartenschau garden show. It makes an attractive additional day trip for guests staying at AltstadtApartments.',
    'Offizielle Informationen':'Official information',

    # Home: reviews
    'Bewertungsübersicht':'Rating overview',
    '4,4 von 5 Sternen':'4.4 out of 5 stars',
    '34 Bewertungen · Zusammenfassung aus Reiseportalen':'34 reviews · summary from travel platforms',
    'Google Travel bündelt Bewertungen externer Buchungsplattformen. Die unten gezeigten Stimmen stammen von Booking.com.':'Google Travel combines ratings from external booking platforms. The guest comments shown below are sourced from Booking.com.',
    'Booking.com · Deutschland':'Booking.com · Germany',
    'Positive guestsbewertung':'Positive guest review',
    'Besonders gelobt wurden die zentrale Location, die Sauberkeit, die bequemen Betten und die vollständige Ausstattung.':'Guests especially praised the central location, cleanliness, comfortable beds and complete amenities.',
    'Die Location und Ausstattung überzeugten; Ein- und Auschecken wurden als besonders unkompliziert beschrieben.':'Guests praised the location and amenities, and described check-in and check-out as especially straightforward.',
    'Die sehr zentrale Location und der besondere Charme der historischen Altbauweise blieben positiv in Erinnerung.':'The very central location and the distinctive charm of the historic building were remembered particularly positively.',
    'Quelle: Booking.com':'Source: Booking.com',
    'Transparenz':'Transparency',
    'Die Darstellung ist an die klare Kartenoptik von Google angelehnt. Es handelt sich nicht um eingebettete Google-Rezensionen; die Bewertungsdaten werden transparent mit ihrer jeweiligen Quelle angegeben.':'The presentation is inspired by Google’s clean card layout. These are not embedded Google reviews; each rating and guest comment is transparently labelled with its source.',

    # Home: host/contact/footer
    'Vom ersten Contact bis zur Anreise haben Sie einen direkten Ansprechpartner. Fragen zu Parkplatz, Check-in oder Aufenthalt lassen sich persönlich und unkompliziert klären.':'From your first enquiry through to arrival, you have one direct contact person. Questions about parking, check-in or your stay can be handled personally and easily.',
    'Die wichtigsten Antworten für Ihre Holiday apartment in Dinkelsbühl.':'The key answers for your holiday apartment stay in Dinkelsbühl.',
    'Sie möchten etwas zu Ihrem Aufenthalt wissen? Ihr Ansprechpartner Kurt Stollenmeier hilft Ihnen persönlich weiter.':'Have a question about your stay? Your host, Kurt Stollenmeier, will be happy to help you personally.',
    'Zwei Apartments.<br>Ein Stück Zuhause in the old town.':'Two apartments.<br>A little piece of home in the old town.',

    # AltstadtApartment detail page
    '<h1>Old town<i>Apartment.</i></h1>':'<h1>Altstadt<i>Apartment.</i></h1>',
    'Wohnzimmer des AltstadtApartments':'Living room of the AltstadtApartment',
    'bathroom des AltstadtApartments':'Bathroom in the AltstadtApartment',
    'Wohnen mit Charme.<br><i>Mitten im Leben.</i>':'Charming living.<br><i>Right in the heart of it.</i>',
    'Ein gemütlicher Rückzugsort mitten in Dinkelsbühl. Mit warmen Holzböden, einer eigenen Küche und Platz für Ihre gemeinsame Zeit.':'A cosy retreat in the heart of Dinkelsbühl, with warm wooden floors, your own kitchen and space to enjoy time together.',
    'Die Holiday apartment liegt in the historic old town. Cafés, Restaurants und Sehenswürdigkeiten erreichen Sie zu Fuß. Nach einem Tag unterwegs genießen Sie die angenehm ruhige Atmosphäre Ihres Apartments.':'The apartment is located in the historic old town. Cafés, restaurants and sights are all within walking distance. After a day out, enjoy the calm atmosphere of your own apartment.',
    'Ein eigenes bathroom':'Private bathroom',
    'Anreise zwischen 15:00 und 18:00 Uhr · Abreise bis 10:00 Uhr, sofern nichts anderes vereinbart wurde.':'Check-in is between 3:00 pm and 6:00 pm · check-out is by 10:00 am, unless otherwise agreed.',
    'Die genaue Anfahrt und Ihre Ankunftszeit stimmen Sie bitte mit dem Gastgeber ab.':'Please coordinate your exact arrival details and arrival time directly with the host.',
    'Ihre Tage<br><i>in Dinkelsbühl.</i>':'Your stay<br><i>in Dinkelsbühl.</i>',
    'Von guestsn bestätigt':'Confirmed by guests',
    '8,5 von 10.':'8.5 out of 10.',
    'Location 9,7.':'Location 9.7.',
    'Aktueller Bewertungsstand auf Booking.com · 59 Bewertungen.':'Current Booking.com rating · 59 reviews.',
    'Aktueller Bewertungsstand auf Booking.com · 44 Bewertungen.':'Current Booking.com rating · 44 reviews.',
    'guests heben besonders die zentrale Location, die Sauberkeit, bequeme Betten und die vollständige Ausstattung hervor.':'Guests especially praise the central location, cleanliness, comfortable beds and complete amenities.',
    'Gelobt werden vor allem die zentrale Old townlage, die großzügige Aufteilung und der unkomplizierte Check-in.':'Guests particularly praise the central old-town location, generous layout and straightforward check-in.',
    'Nördlinger Straße 16 · mitten in Dinkelsbühl und ideal für Wege zu Fuß.':'Nördlinger Straße 16 · right in Dinkelsbühl and ideal for exploring on foot.',
    'Quelle: Booking.com · Locationbewertung':'Source: Booking.com · location rating',
    '7 Originalaufnahmen · AltstadtApartment':'7 original photos · AltstadtApartment',
    'Originalaufnahmen · DesignApartment':'Original photos · DesignApartment',
    'Abendstimmung im AltstadtApartment':'Evening atmosphere in the AltstadtApartment',
    'Schlafmöglichkeit im Wohnbereich':'Sleeping area in the living room',
    'Sitzecke im AltstadtApartment':'Seating area in the AltstadtApartment',
    'Dusche im AltstadtApartment':'Shower in the AltstadtApartment',
    'Apartments liegen in der Nördlinger Straße 16 in the historic old town. Restaurants, Cafés und viele Sehenswürdigkeiten lassen sich bequem zu Fuß erreichen.':'The apartments are located at Nördlinger Straße 16 in the historic old town. Restaurants, cafés and many sights are within easy walking distance.',
    '<b>Historic old town</b> direkt vor der Tür':'<b>Historic old town</b> right outside the door',
    '<b>Parken</b> laut Gastgeber in etwa 5 Gehminuten':'<b>Parking</b> according to the host, around a 5-minute walk away',
    '<b>Persönlicher Contact</b> vor und während des Aufenthalts':'<b>Personal contact</b> before and during your stay',

    # DesignApartment detail page
    'Mehr Raum für gemeinsame Tage':'More room for time together',
    'Historisches Haus.<br><i>Moderner Rückzugsort.</i>':'Historic house.<br><i>Modern retreat.</i>',
    'Das DesignApartment verbindet individuellen Charakter mit großzügigem Platz für Familien und kleine Gruppen.':'The DesignApartment combines individual character with generous space for families and small groups.',
    'Drei bedrooms, eine eigene Küche und ein heller Wohnbereich machen die Wohnung zum komfortablen Ausgangspunkt für Ihre Zeit in Dinkelsbühl.':'Three bedrooms, a private kitchen and a bright living area make the apartment a comfortable base for your time in Dinkelsbühl.',
    'Bis zu 6 guests':'Up to 6 guests',
    'bedrooms des DesignApartments':'Bedroom in the DesignApartment',
    'Wohnzimmer':'Living room',
    'Küche':'Kitchen',
    'Arbeitsplatz':'Workspace',

    # Dinkelsbühl page/meta
    'Discover Dinkelsbühl: historische Old town, Romantic Road und kurze Wege von den AltstadtApartments.':'Discover Dinkelsbühl: historic old town, the Romantic Road and everything within easy reach of AltstadtApartments.',
    'Fachwerk, Türme, Stadtmauer und verwinkelte Gassen: Von Ihrem Apartment aus beginnt Dinkelsbühl direkt vor der Tür.':'Timber-framed houses, towers, the town wall and winding lanes: from your apartment, Dinkelsbühl begins right outside the door.',
    'Die historische Old town lässt sich am besten zu Fuß entdecken. Cafés, Restaurants, Plätze und Sehenswürdigkeiten liegen nah beieinander – ideal für entspannte Tage ohne festen Plan.':'The historic old town is best explored on foot. Cafés, restaurants, squares and sights are close together – ideal for relaxed days without a fixed plan.',
    'Spazieren Sie durch die vollständig erhaltene historische Stadtanlage und entdecken Sie immer wieder neue Perspektiven zwischen den alten Häuserzeilen.':'Stroll through the remarkably well-preserved historic town and discover new perspectives between the old rows of houses at every turn.',
    'Dinkelsbühl gehört zu den bekanntesten Orten entlang der Romantischen Straße und eignet sich perfekt als Ausgangspunkt für weitere Ausflüge in die Region.':'Dinkelsbühl is one of the best-known stops along the Romantic Road and makes an excellent base for further trips around the region.',
    'Die Kinderzeche gehört zu den prägenden Traditionen der Stadt und macht die Geschichte Dinkelsbühls jedes Jahr auf besondere Weise erlebbar.':'The Kinderzeche is one of the town’s defining traditions and brings Dinkelsbühl’s history to life in a special way every year.',
    'Mit einer Holiday apartment in the old town bleiben viele Wege kurz. Für konkrete Anfahrt und Parkmöglichkeiten erhalten Sie die Informationen direkt vom Gastgeber.':'With an apartment in the old town, many places are only a short walk away. The host will provide detailed arrival and parking information directly.',

    # Booking page/meta/content
    'Wählen Sie Ihr AltstadtApartment for up to 4 guests oder Ihr DesignApartment for up to 6 guests und prüfen Sie die Verfügbarkeit in der bestehenden Smoobu-Buchung.':'Choose the AltstadtApartment for up to 4 guests or the DesignApartment for up to 6 guests and check availability in the Smoobu booking system.',
    'Wählen Sie ein Apartment. Im nächsten Schritt prüfen Sie freie Termine, Preise und Booking terms direkt in unserer Smoobu-Buchung.':'Choose an apartment. In the next step, check available dates, prices and booking conditions directly in the Smoobu booking system.',
    '80 m² · bis zu 4 guests':'80 m² · up to 4 guests',
    '85 m² · bis zu 6 guests':'85 m² · up to 6 guests',
    '2 bedrooms · eigene Küche · WLAN':'2 bedrooms · private kitchen · Wi-Fi',
    '3 bedrooms · eigene Küche · WLAN':'3 bedrooms · private kitchen · Wi-Fi',
    'Vorteile der Direktbuchung':'Benefits of direct booking',
    'Ohne Umweg über große Buchungsportale und ohne zusätzliche Plattformgebühren.':'Book without the detour through large booking portals and without additional platform fees.',
    'Kurt Stollenmeier unterstützt Sie bei Fragen rund um Ihren Aufenthalt.':'Kurt Stollenmeier is available personally for questions about your stay.',
    'Freie Termine und die konkreten Konditionen direkt für Ihr Wunsch-Apartment prüfen.':'Check available dates and the exact conditions directly for your preferred apartment.',

    # Misc ALT/ARIA text
    'aria-label="4,4 von 5 Sternen"':'aria-label="4.4 out of 5 stars"',
    'aria-label="Positive guestsbewertung"':'aria-label="Positive guest review"',
    'data-caption="Wohnzimmer des AltstadtApartments"':'data-caption="Living room of the AltstadtApartment"',
    'data-caption="Wohnzimmer des DesignApartments"':'data-caption="Living room of the DesignApartment"',
}

for path in files:
    html = path.read_text(encoding='utf-8')
    for old, new in replacements.items():
        html = html.replace(old, new)
    path.write_text(html, encoding='utf-8')

# Targeted cleanup for phrases that differ between pages.
idx = root/'en/index.html'
if idx.exists():
    html = idx.read_text(encoding='utf-8')
    html = html.replace('Dinkelsbühl. Right outside.</p><h2>Lanes full of history.<br><i>Days full of possibilities.</i></h2></div><div class="town-bottom"><p data-reveal>', 'Dinkelsbühl. Right outside.</p><h2>Lanes full of history.<br><i>Days full of possibilities.</i></h2></div><div class="town-bottom"><p data-reveal>')
    html = html.replace('<p class="eyebrow">2026 day-trip tip</p><h2>Landesgartenschau<br><i>Ellwangen 2026.</i></h2>', '<p class="eyebrow">2026 day-trip tip</p><h2>Ellwangen Garden Show<br><i>2026.</i></h2>')
    idx.write_text(html, encoding='utf-8')

# Normalise decimal punctuation for English visible ratings.
for path in files:
    html = path.read_text(encoding='utf-8')
    html = html.replace('>8,5<','>8.5<').replace('>9,7<','>9.7<').replace('>4,4<','>4.4<')
    path.write_text(html, encoding='utf-8')

# Safety check: fail the build if obvious German UI fragments remain.
forbidden = [
    ' Ihren ', ' Ihre ', ' Sie ', ' für ', ' und ', ' mit ', 'Anreise zwischen', 'Abreise',
    'Bewertungen', 'Bewertungsstand', 'Quelle:', 'Persönlicher', 'Parken', 'Wohnbereich',
    'Rückzugsort', 'Aufenthalt wissen', 'Zwei Apartments.<br>Ein Stück', 'Zur Home',
    'eigene Küche', 'Originalaufnahmen', 'Mit einer Holiday apartment', 'historische Old town',
    'liegt in der', 'direkt vor der Tür', 'Gehminuten', 'Unterwegs',
]
problems=[]
for path in files:
    text=path.read_text(encoding='utf-8')
    for token in forbidden:
        if token in text:
            problems.append(f'{path}: {token}')
if problems:
    raise SystemExit('Untranslated English-page fragments remain:\n'+'\n'.join(problems))
