# 冒險島：接手入口

更新：2026-11-10（Asia/Taipei）。目前是依使用者「前次不符預期，重新執行」要求完成的重做版；尚未取得使用者對本輪交付的驗收回覆。

本輪直接從重新上傳 ZIP 的原始遊戲重做，沒有使用被拒絕的 d1942ae 作為輸入。原始檔保存在 `game/source/baseline.html`，SHA-256 `63a018e13af27da20a7493918ecb3719faba09a1059a36fb6dd0da96529c09be`。正式遊戲是 `game/index.html`；可維護來源為 `game/redesign/`，建置工具為 `tools/build_redesign.cjs`。

已完成 M0～M5 的實作與本環境驗證：共用 UI、桌機左戰鬥／右管理、固定背包／比較／主行動、掉落與角色素質、持續戰鬥中的換裝及養成同步、全部原介面、玩家／敵人／夥伴／場景／動作與事件繪圖。保留原玩法、資料、公式、掉率及攻擊判定。測試全部在正式遊戲執行，未將樣板示例搬成正式能力公式。

驗證包含三桌機尺寸／窄版、真實攻擊與灼燒快照、全部裝備修改入口抽測、固定 ID 批次、v3/v4/v5 舊資料遷移比對與匯入匯出、雙分頁房主／訪客及掉 ACK 重送／斷線重開、三畫質預警、17 頁文字對比與同機效能對照。未完整驗證外網 WebRTC、所有歷史實檔、全部交叉組合、跨設備長時間／背景休眠。細節以本輪 VALIDATION 為準。

閱讀順序：

1. [背景與需求演進](docs/PROJECT-CONTEXT.md)
2. [協作規則](AGENTS.md)、[狀態](docs/STATUS.md)、[決策](docs/DECISIONS.md)
3. [本輪驗證](docs/reviews/redo/VALIDATION.md)、[前後對照](docs/reviews/redo/COMPARISON.html)、[素材／程式映射](docs/reviews/redo/ASSET-MAP.md)
4. [完整原實作需求](handoff/v0.4/IMPLEMENTATION_PROMPT.md)、ART-SPEC／ASSET-GUIDE／COVERAGE／IMPLEMENTATION-PLAN／ACCEPTANCE，以及 [LIVE-GEAR](docs/LIVE-GEAR.md)

使用者已確認：2D 美式粗硬街頭漫畫、順線粗框、淺藍主色、左右布局、自動戰鬥優先看掉寶／裝備／素質、戰鬥中立即換裝。不要再把這些當成等待風格確認的關卡。色碼與尺寸是 v0.4 設計落地值，不是使用者逐值指定。

本輪下載：[可玩 ZIP](releases/Adventure-Island-v0.4-redo.zip)。完整專案可由 GitHub `work` 分支下載，附有原碼、測試與 Harness。舊設計 ZIP 是背景／樣板；`docs/reviews/implementation/` 與舊 playable ZIP 是被拒絕嘗試的歷史證據，不能當成本輪通過證明。

原 DOCX 是背景參考，不自動擴增需求；44 個 SVG 是靜態輪廓與圖示參考，完整正式視覺另由程序繪圖與原動畫狀態產生。每批仍須更新 STATUS、COVERAGE 與必要決策，使用已授權的 Git 遠端與 `work` 分支，不改寫歷史。
