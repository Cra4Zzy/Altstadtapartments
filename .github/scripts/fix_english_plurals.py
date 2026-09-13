from pathlib import Path
import re

for path in Path('en').glob('*.html'):
    text = path.read_text(encoding='utf-8')
    text = re.sub(r'\b2 bedroom\b(?!s)', '2 bedrooms', text)
    text = re.sub(r'\b3 bedroom\b(?!s)', '3 bedrooms', text)
    text = re.sub(r'\bThree bedroom\b(?!s)', 'Three bedrooms', text)
    path.write_text(text, encoding='utf-8')

problems = []
patterns = [
    re.compile(r'\b2 bedroom\b(?!s)'),
    re.compile(r'\b3 bedroom\b(?!s)'),
    re.compile(r'\bThree bedroom\b(?!s)'),
]
for path in Path('en').glob('*.html'):
    text = path.read_text(encoding='utf-8')
    for pattern in patterns:
        if pattern.search(text):
            problems.append(f'{path}: {pattern.pattern}')
if problems:
    raise SystemExit('Incorrect English bedroom plurals remain:\n' + '\n'.join(problems))
