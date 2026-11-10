# 冒險島

這是原有 JavaScript／Canvas 2D 遊戲的 v0.4 重做版。以重新上傳的原始遊戲為基準，套用淺藍街頭漫畫風、全系統 UI／角色與世界繪圖，以及持續戰鬥中的即時裝備更新。前次 d1942ae 未通過使用者驗收，屬歷史嘗試；本輪沒有沿用其改版程式。

下載 [本輪可玩封裝](releases/Adventure-Island-v0.4-redo.zip)，解壓後開啟 `game/index.html` 單機遊玩。不需要安裝套件；資產、音樂與正式遊戲皆在同一 HTML。原單檔方式保留；本環境已以完全離線載入相同 HTML 驗證，直接 `file://` 開啟受 managed Chrome 政策限制，未宣稱實測過。

冒險預設開啟自動戰鬥。右側可比較／鎖定／換裝、查看素質與進階養成；整理不會暫停。新到貨先顯示計數，按「更新」才加入目前背包排列。換裝依原公式立即更新出戰者，非升級時保留 HP／MP 絕對值並限制到新上限。連線冒險支援整理與養成，轉蛋於大廳使用。

在戰場按 G 展開管理；焦點位於管理區時 Escape 收合，位於戰場時 Escape／P 使用原暫停。兩端連線請使用同一版本。若瀏覽器因更換檔案位置使用不同存檔來源，可先在原版設定匯出，再於新版設定匯入。

- [前後對照](docs/reviews/redo/COMPARISON.html)／[圖片版](docs/reviews/redo/COMPARISON.png)
- [正式驗證與未驗證項目](docs/reviews/redo/VALIDATION.md)
- [47 項實作覆蓋](handoff/v0.4/COVERAGE.csv)／[來源與素材映射](docs/reviews/redo/ASSET-MAP.md)
- [目前狀態](docs/STATUS.md)／[協作入口](START-HERE.md)

開發來源在 `game/redesign/`，不可變原始 HTML 在 `game/source/baseline.html`。已在 Node 24.22.1 驗證建置：

```sh
node --expose-internals tools/build_redesign.cjs
python3 tools/check_syntax.py
```

建置使用 Node 內附 Acorn，輸出可重現的單檔 `game/index.html`，不需要網路或 npm。瀏覽器回歸另需 Playwright 與 Chromium；啟動 `python3 -m http.server 8000 --bind 127.0.0.1` 後執行 `tools/test_redesign_*.cjs`（效能腳本單獨執行）。具體環境、命令及各證據見 VALIDATION。

外網 WebRTC、跨設備長時間效能、所有歷史玩家實檔與全部動畫／裝備交叉組合仍未完整驗證。這些界線與本輪已執行測試分開記錄。
