from pathlib import Path

script_path = Path('.github/scripts/complete_english_cleanup.py')
source = script_path.read_text(encoding='utf-8')
source = '\n'.join(line for line in source.splitlines() if "' und '" not in line)
exec(compile(source, str(script_path), 'exec'), {'__name__': '__main__'})
