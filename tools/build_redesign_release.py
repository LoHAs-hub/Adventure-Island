"""Seal the committed redo source and evidence; exclude runtime saves and rejected releases."""
from pathlib import Path
import csv
import hashlib
import json
import subprocess
import zipfile

root = Path(__file__).resolve().parents[1]
release = root / "releases"
release.mkdir(exist_ok=True)
sha = lambda data: hashlib.sha256(data).hexdigest()
source_commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
status = subprocess.check_output(["git", "status", "--porcelain", "--untracked-files=normal"], cwd=root, text=True)
unexpected = [line for line in status.splitlines() if not line[3:].startswith("releases/")]
assert not unexpected, "Commit source/evidence before sealing: " + repr(unexpected)
game_hash = sha((root / "game/index.html").read_bytes())
run = json.loads((root / "docs/reviews/redo/RUN.json").read_text())
assert game_hash == run["game_sha256"]
with (root / "handoff/v0.4/COVERAGE.csv").open(encoding="utf-8-sig", newline="") as stream:
    rows = list(csv.DictReader(stream))
assert len(rows) == 47
for row in rows:
    assert row["implementation_status"] and row["evidence"]
    for evidence in row["evidence"].split("; "):
        assert (root / evidence).is_file(), evidence

paths = [root / name for name in ["README.md", "START-HERE.md", "AGENTS.md", "game/index.html", "game/source/baseline.html"]]
paths += list((root / "game/redesign").glob("*"))
paths += [p for p in (root / "docs").rglob("*") if p.is_file() and "reviews/implementation/" not in p.as_posix()]
paths += [p for p in (root / "handoff/v0.4").glob("*") if p.is_file() and p.suffix != ".zip"]
paths += [p for p in (root / "design/mockups/v0.4").rglob("*") if p.is_file()]
paths += list((root / "tools").glob("test_redesign_*.cjs"))
paths += [root / "tools" / name for name in ["README.md", "build_redesign.cjs", "check_syntax.py", "trace_redesign.cjs", "capture_redesign_comparison.cjs", "build_redesign_release.py"]]
files = {p.relative_to(root).as_posix(): p.read_bytes() for p in paths if p.is_file()}
assert all(not n.startswith(("work/", ".git/")) for n in files)
files["README-PLAY.txt"] = """冒險島 · v0.4 本輪重做版

解壓後開啟 game/index.html 單機遊玩；無需安裝套件。原始遊戲資料與玩法保留。
自動戰鬥中可從右側比較、鎖定、整理與換裝，能力立即套用；HP/MP不因換裝免費補滿。
新到貨按「更新」才加入目前背包排列。G展開管理；焦點在管理區時Escape收合，戰場Escape/P為原暫停。
連線兩端請使用同版；戰鬥中可整理／養成，轉蛋於大廳使用。
若檔案位置造成不同瀏覽器存檔來源，先從原版設定匯出，再在新版設定匯入。

前後對照：docs/reviews/redo/COMPARISON.html（或COMPARISON.png）
驗證與未驗證項目：docs/reviews/redo/VALIDATION.md
跨聊天室接手：START-HERE.md
來源／每檔SHA：MANIFEST.json；本包不含玩家或測試存檔。

外網WebRTC、跨設備長時間與背景休眠、全部歷史實檔／交叉組合未完整驗證。
相同HTML完全離線、零外部請求已驗證；managed Chrome阻擋直接fileURL，未宣稱該路徑實測。
前次d1942ae未通過使用者驗收；本包直接從重新上傳的原始遊戲重做，不沿用其實作。
""".encode()
files["releases/REDO-RELEASE.json"] = json.dumps({
    "release": "v0.4-redo", "source_commit": source_commit, "game_sha256": game_hash,
    "baseline_sha256": sha(files["game/source/baseline.html"]),
    "note": "Final archive SHA-256 is recorded alongside the ZIP outside the archive; MANIFEST.json verifies all bundled files.",
}, ensure_ascii=False, indent=2).encode()
manifest = {
    "release": "v0.4-redo", "date": "2026-11-10", "timezone": "Asia/Taipei",
    "source_commit": source_commit, "game_sha256": game_hash,
    "baseline_sha256": sha(files["game/source/baseline.html"]),
    "validation": "docs/reviews/redo/VALIDATION.md",
    "files": {name: sha(data) for name, data in sorted(files.items())},
}
files["MANIFEST.json"] = json.dumps(manifest, ensure_ascii=False, indent=2).encode()
archive = release / "Adventure-Island-v0.4-redo.zip"
with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as output:
    for name, data in sorted(files.items()):
        entry = zipfile.ZipInfo(name, date_time=(2026, 11, 10, 0, 0, 0))
        entry.compress_type = zipfile.ZIP_DEFLATED
        entry.external_attr = 0o100644 << 16
        output.writestr(entry, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
with zipfile.ZipFile(archive) as sealed:
    for name, expected in manifest["files"].items():
        assert sha(sealed.read(name)) == expected, name
metadata = {k: v for k, v in manifest.items() if k != "files"}
metadata.update(archive=archive.name, archive_sha256=sha(archive.read_bytes()), archive_bytes=archive.stat().st_size, file_count=len(files), manifest_verified=True)
(release / "REDO-RELEASE.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(metadata, ensure_ascii=False))
