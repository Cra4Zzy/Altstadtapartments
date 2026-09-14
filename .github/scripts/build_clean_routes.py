from pathlib import Path
import re

ROOT_ROUTES = [
    'altstadtapartment', 'designapartment', 'dinkelsbuehl', 'buchen',
    'impressum', 'datenschutz', 'agb'
]
EN_ROUTES = ['altstadtapartment', 'designapartment', 'dinkelsbuehl', 'buchen']

DOMAIN = 'https://altstadtapartments-dinkelsbuehl.de'


def clean_absolute_urls(html: str) -> str:
    for slug in ROOT_ROUTES:
        html = html.replace(f'{DOMAIN}/{slug}.html', f'{DOMAIN}/{slug}/')
    for slug in EN_ROUTES:
        html = html.replace(f'{DOMAIN}/en/{slug}.html', f'{DOMAIN}/en/{slug}/')
    return html


def clean_root_index(html: str) -> str:
    html = clean_absolute_urls(html)
    for slug in ROOT_ROUTES:
        html = html.replace(f'href="{slug}.html', f'href="{slug}/')
        html = html.replace(f"href='{slug}.html", f"href='{slug}/")
    return html


def clean_en_index(html: str) -> str:
    html = clean_absolute_urls(html)
    for slug in EN_ROUTES:
        html = html.replace(f'href="{slug}.html', f'href="{slug}/')
        html = html.replace(f"href='{slug}.html", f"href='{slug}/")
    for slug in ['impressum', 'datenschutz', 'agb']:
        html = html.replace(f'href="../{slug}.html', f'href="../{slug}/')
        html = html.replace(f"href='../{slug}.html", f"href='../{slug}/")
    return html


def nested_root_page(html: str) -> str:
    html = clean_absolute_urls(html)

    # Assets are one directory further down on clean routes.
    html = html.replace('href="assets/', 'href="../assets/')
    html = html.replace("href='assets/", "href='../assets/")
    html = html.replace('src="assets/', 'src="../assets/')
    html = html.replace("src='assets/", "src='../assets/")

    # Homepage links from /slug/ back to site root.
    html = html.replace('href="./#', 'href="../#')
    html = html.replace("href='./#", "href='../#")
    html = html.replace('href="./"', 'href="../"')
    html = html.replace("href='./'", "href='../'")
    html = html.replace('href="index.html#', 'href="../#')
    html = html.replace("href='index.html#", "href='../#")
    html = html.replace('href="index.html"', 'href="../"')
    html = html.replace("href='index.html'", "href='../'")

    # Sibling clean routes.
    for slug in ROOT_ROUTES:
        html = html.replace(f'href="{slug}.html', f'href="../{slug}/')
        html = html.replace(f"href='{slug}.html", f"href='../{slug}/")

    return html


def nested_en_page(html: str) -> str:
    html = clean_absolute_urls(html)

    # Existing EN pages reference shared root assets with ../assets; nested clean routes need ../../assets.
    html = html.replace('href="../assets/', 'href="../../assets/')
    html = html.replace("href='../assets/", "href='../../assets/")
    html = html.replace('src="../assets/', 'src="../../assets/')
    html = html.replace("src='../assets/", "src='../../assets/")

    # Homepage links from /en/slug/ back to /en/.
    html = html.replace('href="./#', 'href="../#')
    html = html.replace("href='./#", "href='../#")
    html = html.replace('href="./"', 'href="../"')
    html = html.replace("href='./'", "href='../'")
    html = html.replace('href="index.html#', 'href="../#')
    html = html.replace("href='index.html#", "href='../#")
    html = html.replace('href="index.html"', 'href="../"')
    html = html.replace("href='index.html'", "href='../'")

    # Sibling English routes.
    for slug in EN_ROUTES:
        html = html.replace(f'href="{slug}.html', f'href="../{slug}/')
        html = html.replace(f"href='{slug}.html", f"href='../{slug}/")

    # German legal pages live two levels above /en/slug/.
    for slug in ['impressum', 'datenschutz', 'agb']:
        html = html.replace(f'href="../{slug}.html', f'href="../../{slug}/')
        html = html.replace(f"href='../{slug}.html", f"href='../../{slug}/")
        html = html.replace(f'href="../{slug}/', f'href="../../{slug}/')
        html = html.replace(f"href='../{slug}/", f"href='../../{slug}/")

    return html


def redirect_stub(target: str, canonical: str, lang: str = 'de') -> str:
    title = 'Weiterleitung' if lang == 'de' else 'Redirecting'
    text = 'Sie werden weitergeleitet.' if lang == 'de' else 'You are being redirected.'
    return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="robots" content="noindex,follow"><link rel="canonical" href="{canonical}"><title>{title}</title><script>location.replace('{target}'+location.search+location.hash);</script><meta http-equiv="refresh" content="0;url={target}"></head><body><p>{text} <a href="{target}">{target}</a></p></body></html>'''

# Root homepage: keep root index but point all navigation/canonical references at clean routes.
root_index = Path('index.html')
root_index.write_text(clean_root_index(root_index.read_text(encoding='utf-8')), encoding='utf-8')

# English homepage stays /en/ and gets clean links.
en_index = Path('en/index.html')
en_index.write_text(clean_en_index(en_index.read_text(encoding='utf-8')), encoding='utf-8')

# Build real directory-index routes and leave backwards-compatible redirects at old .html URLs.
for slug in ROOT_ROUTES:
    source = Path(f'{slug}.html')
    if not source.exists():
        continue
    original = source.read_text(encoding='utf-8')
    clean = nested_root_page(original)
    destination = Path(slug) / 'index.html'
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(clean, encoding='utf-8')
    source.write_text(
        redirect_stub(f'{slug}/', f'{DOMAIN}/{slug}/', 'de'),
        encoding='utf-8'
    )

for slug in EN_ROUTES:
    source = Path('en') / f'{slug}.html'
    if not source.exists():
        continue
    original = source.read_text(encoding='utf-8')
    clean = nested_en_page(original)
    destination = Path('en') / slug / 'index.html'
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(clean, encoding='utf-8')
    source.write_text(
        redirect_stub(f'{slug}/', f'{DOMAIN}/en/{slug}/', 'en'),
        encoding='utf-8'
    )

# Update discoverability files to advertise clean canonical routes.
for filename in ['sitemap.xml', 'llms.txt', 'SEO-LAUNCH-CHECKLIST.md']:
    p = Path(filename)
    if p.exists():
        text = p.read_text(encoding='utf-8')
        text = clean_absolute_urls(text)
        p.write_text(text, encoding='utf-8')
