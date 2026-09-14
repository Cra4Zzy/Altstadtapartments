from pathlib import Path

# German/root pages: clean links back to homepage while preserving GitHub Pages repo base.
root_files = [p for p in Path('.').glob('*.html')]
for path in root_files:
    html = path.read_text(encoding='utf-8')
    html = html.replace('href="index.html#', 'href="./#')
    html = html.replace("href='index.html#", "href='./#")
    html = html.replace('href="index.html"', 'href="./"')
    html = html.replace("href='index.html'", "href='./'")
    path.write_text(html, encoding='utf-8')

# English pages: ./ is /en/ on both GitHub Pages and the production domain.
en_dir = Path('en')
if en_dir.exists():
    for path in en_dir.glob('*.html'):
        html = path.read_text(encoding='utf-8')
        html = html.replace('href="index.html#', 'href="./#')
        html = html.replace("href='index.html#", "href='./#")
        html = html.replace('href="index.html"', 'href="./"')
        html = html.replace("href='index.html'", "href='./'")
        path.write_text(html, encoding='utf-8')
