from pathlib import Path

replacements = {
    'Source: Booking.com · Locationbewertung':'Source: Booking.com · location rating',
    'vor und während des Aufenthalts':'before and during your stay',
    'Das andere Apartment entdecken':'Discover the other apartment',
    'Living room des DesignApartments':'Living room of the DesignApartment',
    'eigene Kitchen · WLAN':'private kitchen · Wi-Fi',
    'eigene Küche · WLAN':'private kitchen · Wi-Fi',
    'WLAN':'Wi-Fi',
    'bedrooms':'bedroom',
}

for path in Path('en').glob('*.html'):
    text = path.read_text(encoding='utf-8')
    for old, new in replacements.items():
        text = text.replace(old, new)
    path.write_text(text, encoding='utf-8')

forbidden = [
    'Locationbewertung', 'vor und während des Aufenthalts', 'Das andere Apartment entdecken',
    ' des DesignApartments', 'eigene Kitchen', 'eigene Küche', ' WLAN',
    'Old towncharme', 'Rückzugsort', 'Originalaufnahmen', 'Bewertungsstand', 'Quelle:'
]
problems = []
for path in Path('en').glob('*.html'):
    text = path.read_text(encoding='utf-8')
    for token in forbidden:
        if token in text:
            problems.append(f'{path}: {token}')
if problems:
    raise SystemExit('Remaining mixed-language fragments:\n' + '\n'.join(problems))
