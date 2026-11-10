# v0.4 全版美術交接：淺藍 × 平順粗線

本版依使用者最新回饋修訂：**粗硬程度保留、線條更滑順、減少外凸尖角、主色淺藍、保留左戰鬥／右管理。** 全遊戲套用同一美術語言，優先完成掉寶、裝備管理與素質；自動戰鬥中可換裝並立即影響能力。

[下載最新完整專案 ZIP](https://github.com/LoHAs-hub/Adventure-Island/archive/refs/heads/work.zip) · [可直接貼給實作端的 Prompt](IMPLEMENTATION_PROMPT.md) · [七張樣板截圖](../../design/mockups/v0.4/README.md)

## 新聊天室先讀

先讀根目錄 [START-HERE](../../START-HERE.md) 與 [PROJECT-CONTEXT](../../docs/PROJECT-CONTEXT.md)。背景、需求演進、已確認方向、完成／未完成清單與下一步均已整理。使用 [NEW-CHAT-PROMPT](NEW-CHAT-PROMPT.md) 配合完整專案ZIP交給實作端，不需要提供本次聊天紀錄。

## 交接內容

| 檔案 | 用途 |
|---|---|
| NEW-CHAT-PROMPT.md | 可直接貼到新聊天室的背景、進度與接手任務 |
| ../../START-HERE.md、../../docs/PROJECT-CONTEXT.md | 從討論起點整理的背景、需求、方向與目前狀態 |
| IMPLEMENTATION_PROMPT.md | 完整實作任務、不可遺漏的行為與交付要求 |
| ART-SPEC.md、design-tokens.json／css | 顏色、輪廓、字級、布局、狀態與特效規格 |
| COVERAGE.csv | 26 個既存面板節點與全部視覺分類的修改／驗收對照；含空殼與舊入口處理 |
| ASSET-GUIDE.md | 44 個 SVG 參考素材的角色、使用方式、完整資產製作清單 |
| IMPLEMENTATION-PLAN.md、ACCEPTANCE.md | 分批順序與正式遊戲驗收 |
| ../../design/mockups/v0.4/index.html | 五頁可離線開啟的設計樣板 |
| ../../game/index.html | 原始正式遊戲，逐位元保存，供實作基準 |
| ../../AGENTS.md、../../docs/ | Harness 協作記憶、決策、代碼盤點與即時換裝規則 |

最新完整專案ZIP解壓後先開啟根目錄 START-HERE.md，再依README開啟 `design/mockups/v0.4/index.html`。正式遊戲位於 `game/index.html`。根目錄已有完整協作資料，不必取得聊天歷史才能接手。

## 交付狀態

本次完成的是**新版互動樣板、全版美術規格、向量參考素材與實作交接包**。原遊戲尚未套用新版，也尚未完成正式即時換裝。樣板中的角色、關卡、物品、數值與計時為獨立示例；不可搬成正式遊戲的公式或獎勵。全版介面頁的卡片是樣式規格，並非各系統已實作的宣告。

淺藍及順線方向已由使用者確認；色碼、圓角與時間值是本次可直接採用的設計落地值。實作端應依規格推進，不重啟已定案的方向討論。若遇到規格與既有機制衝突，記錄具體證據、影響與處理，不自行更改遊戲數值。

## 舊設計封裝

[Adventure-Island-Art-Handoff-v0.4.zip](Adventure-Island-Art-Handoff-v0.4.zip)、RELEASE.json與PACKAGE-MANIFEST.json保留2026-11-09的設計封裝；其中的verify_package.py只驗證該舊包。新增加的接手文件已納入GitHub最新完整專案ZIP，請交付上方最新下載連結。
