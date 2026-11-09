from pathlib import Path
import hashlib, json, sys
root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
failures = []
for entry in manifest["files"]:
    path = (root / entry["path"]).resolve()
    if not path.is_relative_to(root) or not path.is_file():
        failures.append(entry["path"] + ": missing or invalid path")
        continue
    data = path.read_bytes()
    if len(data) != entry["bytes"] or hashlib.sha256(data).hexdigest() != entry["sha256"]:
        failures.append(entry["path"] + ": checksum mismatch")
game = root / "game/index.html"
if not game.is_file() or hashlib.sha256(game.read_bytes()).hexdigest() != manifest["baseline_game_sha256"]:
    failures.append("game/index.html: original baseline mismatch")
if failures:
    print("FAILED\n" + "\n".join(failures))
    raise SystemExit(1)
print(f"Verified {len(manifest['files'])} files; original game SHA-256 matches.")
