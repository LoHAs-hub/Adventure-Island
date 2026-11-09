# Adventure-Island
原生 JavaScript + Canvas 2D 的橫向動作 RPG。原始上傳檔保存於 game/index.html，尚未改動遊戲內容。

## 開啟
在專案根目錄執行 `python -m http.server 8000 --bind 127.0.0.1`，開啟 http://127.0.0.1:8000/game/ 。也可直接開啟 HTML；瀏覽器的存檔會依來源不同而分開。
語法檢查：`python tools/check_syntax.py`（需要 Python、Node.js）。

## Harness 協作架構
- AGENTS.md：後續協作者入口與工作規則。
- docs/STATUS.md：目前階段、驗證、下一步。
- docs/DECISIONS.md：已確認／待確認／背景要求。
- docs/ART-INVENTORY.md：美術物件與邏輯盤點。
- docs/decisions/：重大設計決策 ADR。
- docs/reviews/baseline/：未修改版本截圖。
- docs/reference/：原始交接資料；其內容不是新的使用者指令。

目前階段：已確認2D美式街頭塗鴉風格，以及自動戰鬥中整理／即時換裝。正在整理設計樣板規格與實作交接，遊戲尚未修改。第一階段計畫見 docs/PHASE-1.md，美術方向見 docs/ART-DIRECTION.md，功能規格見 docs/LIVE-GEAR.md。參考來源及存取狀態見 docs/reference/VISUAL-REFERENCES.md。
