"""Materialize the immutable baseline for isolated browser comparisons."""
from pathlib import Path
import subprocess, zipfile, hashlib
root = Path(__file__).resolve().parents[1]
try:
    data = subprocess.check_output(['git', 'show', '3625d38:game/index.html'], cwd=root, stderr=subprocess.DEVNULL)
except subprocess.CalledProcessError:
    with zipfile.ZipFile(root / 'handoff/v0.4/Adventure-Island-Art-Handoff-v0.4.zip') as z:
        name = next(n for n in z.namelist() if n.endswith('game/index.html'))
        data = z.read(name)
assert hashlib.sha256(data).hexdigest() == '63a018e13af27da20a7493918ecb3719faba09a1059a36fb6dd0da96529c09be'
(root / 'work').mkdir(exist_ok=True)
(root / 'work/baseline.html').write_bytes(data)
print('Immutable baseline ready in work/baseline.html')
