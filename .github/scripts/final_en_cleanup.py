from pathlib import Path
import re

for p in Path('en').glob('*.html'):
    h=p.read_text(encoding='utf-8')
    h=h.replace('Old town<span>Apartments</span>','Altstadt<span>Apartments</span>')
    h=h.replace('Old town<span>Apartment.</span>','Altstadt<span>Apartment.</span>')
    h=h.replace('Old townApartment','AltstadtApartment')
    h=h.replace('Holiday apartments in Dinkelsbühl Old town','Holiday apartments in Dinkelsbühl old town')
    h=h.replace('Zwei Holiday apartments in der historischen Old town von Dinkelsbühl for up to 4 or 6 guests.','Two holiday apartments in the historic old town of Dinkelsbühl for up to 4 or 6 guests.')
    h=h.replace('AltstadtApartments Dinkelsbühl – Holiday apartment in der historischen Old town','AltstadtApartments Dinkelsbühl – holiday apartment in Dinkelsbühl old town')
    h=h.replace('Das AltstadtApartment bietet Platz for up to 4 guests. Im DesignApartment können bis zu 6 guests übernachten. Die Wohnungen werden einzeln gebucht.','The AltstadtApartment sleeps up to 4 guests. The DesignApartment sleeps up to 6 guests. The apartments are booked separately.')
    h=h.replace('für bis zu 4 oder 6 guests','for up to 4 or 6 guests')
    h=h.replace('für bis zu 4 beziehungsweise 6 guests','for up to 4 or 6 guests')
    h=h.replace('in der historischen Old town','in the historic old town')
    h=h.replace('mitten in der Old town','in the heart of the old town')
    h=h.replace('von Dinkelsbühl','of Dinkelsbühl')
    h=h.replace('Hauptnavigation','Main navigation')
    h=h.replace('Footernavigation','Footer navigation')
    h=h.replace('Apartment-Fotogalerie','Apartment photo gallery')
    p.write_text(h,encoding='utf-8')
