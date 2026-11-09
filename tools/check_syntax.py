from pathlib import Path
import re, subprocess, tempfile
source = Path(__file__).resolve().parents[1] / "game/index.html"
scripts = re.findall(r"<script\b[^>]*>(.*?)</script>", source.read_text(), re.S | re.I)
assert scripts, "No inline script found"
for script in scripts:
    with tempfile.TemporaryDirectory() as temp:
        path = Path(temp) / "game.js"
        path.write_text(script)
        subprocess.run(["node", "--check", str(path)], check=True)
print(f"Syntax OK: {len(scripts)} inline script(s)")
