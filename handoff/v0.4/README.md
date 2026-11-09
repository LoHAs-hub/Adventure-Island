# v0.4 全版美術交接：淺藍 × 平順粗線

本版依使用者最新回饋修訂：**粗硬程度保留、線條更滑順、減少外凸尖角、主色淺藍、保留左戰鬥／右管理。** 全遊戲套用同一美術語言，優先完成掉寶、裝備管理與素質；自動戰鬥中可換裝並立即影響能力。

[下載完整 ZIP](Adventure-Island-Art-Handoff-v0.4.zip) · [可直接貼給實作端的 Prompt](IMPLEMENTATION_PROMPT.md) · [七張樣板截圖](../../design/mockups/v0.4/README.md)

## 交接內容

| 檔案 | 用途 |
|---|---|
| IMPLEMENTATION_PROMPT.md | 完整實作任務、不可遺漏的行為與交付要求 |
| ART-SPEC.md、design-tokens.json／css | 顏色、輪廓、字級、布局、狀態與特效規格 |
| COVERAGE.csv | 26 個既存面板節點與全部視覺分類的修改／驗收對照；含空殼與舊入口處理 |
| ASSET-GUIDE.md | 44 個 SVG 參考素材的角色、使用方式、完整資產製作清單 |
| IMPLEMENTATION-PLAN.md、ACCEPTANCE.md | 分批順序與正式遊戲驗收 |
| ../../design/mockups/v0.4/index.html | 五頁可離線開啟的設計樣板 |
| ../../game/index.html | 原始正式遊戲，逐位元保存，供實作基準 |
| ../../AGENTS.md、../../docs/ | Harness 協作記憶、決策、代碼盤點與即時換裝規則 |

ZIP 解壓後開啟根目錄 README.md；先執行 `python verify_package.py`，再開啟 `design/mockups/v0.4/index.html`。正式遊戲位於 `game/index.html`。根目錄已有完整協作資料，不必取得聊天歷史才能接手。

## 交付狀態

本次完成的是**新版互動樣板、全版美術規格、向量參考素材與實作交接包**。原遊戲尚未套用新版，也尚未完成正式即時換裝。樣板中的角色、關卡、物品、數值與計時為獨立示例；不可搬成正式遊戲的公式或獎勵。全版介面頁的卡片是樣式規格，並非各系統已實作的宣告。

淺藍及順線方向已由使用者確認；色碼、圓角與時間值是本次可直接採用的設計落地值。實作端應依規格推進，不重啟已定案的方向討論。若遇到規格與既有機制衝突，記錄具體證據、影響與處理，不自行更改遊戲數值。
