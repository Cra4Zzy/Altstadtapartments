# Seeberger Bau – Website-Redesign

Statische, responsive Onepage-Website auf Basis von HTML, CSS und JavaScript – ohne Build-Prozess und ohne externe Abhängigkeiten.

## Starten

Das ZIP zuerst vollständig entpacken und anschließend `index.html` per Doppelklick im Browser öffnen. Die HTML-Datei nicht direkt innerhalb des ZIP-Archivs starten, da Browser die danebenliegenden Bilder und Schriften dort teilweise nicht laden können.

Für einen lokalen Webserver kann alternativ im Projektordner ausgeführt werden:

```bash
python -m http.server 8080
```

Danach `http://localhost:8080` aufrufen.

## Dateien

- `index.html`: Inhalt, SEO-Metadaten und strukturierte Unternehmensdaten
- `styles.css`: vollständiges Layout, Responsive Design und Animationen
- `script.js`: Navigation, Bildatlas, Leistungs-Akkordeon, ausfallsichere Scroll-Reveals und Kontaktformular
- `assets/images`: Bilder und Logo der bestehenden Seeberger-Website
- `assets/fonts`: lokal eingebundene Open-Source-Schriften

## Vor einer Veröffentlichung

- Kontaktformular an einen echten Formular-Endpunkt oder Mail-Dienst anbinden. In dieser Demo öffnet es das lokale E-Mail-Programm.
- Impressum und Datenschutz rechtlich prüfen und bei Bedarf als eigene Seiten übernehmen.
- Google-Bewertung und laufende Projekte auf Aktualität prüfen.
- Nutzungsrechte für alle übernommenen Bilder final bestätigen.

## Gestaltungskonzept

Die Seite ist als helle, redaktionelle „Bauakte“ gestaltet: typografische Split-Screens, technische Randnotizen, ein wechselnder Projektatlas und ein asymmetrisches Referenzarchiv ersetzen die üblichen dunklen Bau-Website-Kacheln. Alle Schriften und Bilder liegen lokal im Projekt.
