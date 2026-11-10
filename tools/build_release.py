"""Build a self-contained playable release; never package runtime saves or work/."""
from pathlib import Path
import hashlib, json, subprocess, zipfile
root = Path(__file__).resolve().parents[1]
release = root / 'releases'
release.mkdir(exist_ok=True)
source_commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip()
readme = '''冒險島 · v0.4 美術與即時換裝正式整合版
2026-11-10（Asia/Taipei）

解壓後開啟 game/index.html 即可單機遊玩；所有正式資產均內嵌或程序繪製，不需安裝套件或架設服務。
冒險中右側整理裝備／查看素質，戰鬥繼續；G展開、Escape收合。
掉落不會自動重排正在比較的背包，按「更新背包」顯示新到貨。
換裝使用原公式；非升級時HP／MP不免費補滿。
若換檔案位置後瀏覽器使用不同存檔來源，可由原版設定匯出，再用新版既有匯入功能。

前後對照：docs/reviews/implementation/COMPARISON.html
完整驗證與剩餘界線：docs/reviews/implementation/VALIDATION.md
完整來源／工具／歷史：https://github.com/LoHAs-hub/Adventure-Island/tree/work

核心正式測試、雙分頁同步、存檔比對及資料聯絡表已通過；仍未完整驗證外網WebRTC、逐攻擊幀／逐招碰撞與全部強化邊界、所有歷史實檔／匯入匯出UI及跨設備長時間效能。
managed Chrome禁止file://，本輪以完全離線載入相同HTML驗證單檔依賴，未宣稱直接file://已測。
這份封裝不包含任何玩家或測試存檔。MANIFEST.json供選用的SHA-256核對。
'''
files = {'README-PLAY.txt': readme.encode()}
paths = [root/'game/index.html', root/'handoff/v0.4/COVERAGE.csv', root/'docs/STATUS.md', root/'docs/DECISIONS.md', root/'docs/PROJECT-CONTEXT.md',root/'docs/LIVE-GEAR.md',root/'START-HERE.md',root/'AGENTS.md']
paths += list((root/'docs/reviews/implementation').glob('*'))
paths += list((root/'docs/decisions').glob('*.md'))
paths += list((root/'design/mockups/v0.4/assets').glob('*.svg'))
paths += [root/'handoff/v0.4'/n for n in ['ART-SPEC.md','ASSET-GUIDE.md','ACCEPTANCE.md','IMPLEMENTATION-PLAN.md','IMPLEMENTATION_PROMPT.md','NEW-CHAT-PROMPT.md','design-tokens.json','design-tokens.css']]
for p in paths:
    if p.is_file(): files[p.relative_to(root).as_posix()] = p.read_bytes()
manifest = {'design_version':'v0.4','date':'2026-11-10','timezone':'Asia/Taipei','source_commit':source_commit,'game_sha256':hashlib.sha256(files['game/index.html']).hexdigest(),'files':{n:hashlib.sha256(v).hexdigest() for n,v in sorted(files.items())}}
files['MANIFEST.json'] = json.dumps(manifest,ensure_ascii=False,indent=2).encode()
archive = release/'Adventure-Island-v0.4-playable.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for n,v in sorted(files.items()): z.writestr(n,v)
with zipfile.ZipFile(archive) as z:
    for n,sha in manifest['files'].items(): assert hashlib.sha256(z.read(n)).hexdigest()==sha, n
metadata = {k:v for k,v in manifest.items() if k!='files'}
metadata.update(archive=archive.name,archive_sha256=hashlib.sha256(archive.read_bytes()).hexdigest(),archive_bytes=archive.stat().st_size,manifest_verified=True)
(release/'RELEASE.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(metadata,ensure_ascii=False))
