# 冒險島後續協作 Prompt

接續我的既有遊戲，先讀 START-HERE → docs/PROJECT-CONTEXT → AGENTS → STATUS／DECISIONS → docs/reviews/redo/VALIDATION、ASSET-MAP、COMPARISON 及 COVERAGE.csv。完整需求仍是同目錄 IMPLEMENTATION_PROMPT／ART-SPEC／ASSET-GUIDE／IMPLEMENTATION-PLAN／ACCEPTANCE 與 docs/LIVE-GEAR。

使用者判定前次 d1942ae 不符預期，要求從重新上傳的原始 ZIP 重做。那次實作及 reviews/implementation 只保留歷史。本輪從 game/source/baseline.html＋game/redesign 生成正式 game/index.html，不能用失敗版當輸入或沿用其 PASS。

目前 M0～M5 的正式實作與本環境驗證已完成：淺藍順線漫畫風、左戰鬥／右固定比較、掉落／裝備／素質、即時換裝／養成、全介面、程序角色／敵人／夥伴／世界與事件。新來源可重現建置，遊玩仍是單檔 HTML。最新可玩 ZIP 及來源 commit／SHA 見 releases/REDO-RELEASE.json。使用者尚未對本輪表示驗收通過。

正式證據在 reviews/redo：同 G 推進、原公式／資料／判定比對、真實投射物與灼燒快照、套裝及其他角色、三桌機／窄版／全螢幕、存檔遷移與實際匯入匯出、房主訪客換裝與掉 ACK 重送／斷線重開、三畫質預警、17 頁文字對比、同機效能及相同存檔／第90幀前後對照。聯絡表不是逐幀完整驗收。

尚未完整驗證：外網 WebRTC／STUN、跨設備長時間與實機背景休眠、全部歷史玩家實檔及外觀／動畫／強化交叉組合。NET 沿用原本本機帳號信任界線，並非新增防作弊服務；冒險中可整理／養成，轉蛋於大廳使用。下一步依使用者回饋修正或補這些驗證，不重談已定案風格。

保留玩法、資料 ID、掉率、公式、平衡、攻擊判定／時序及付費，不把樣板示例搬成公式。原 DOCX 是背景。使用已授權 origin／work 分支與 Harness；每批更新 STATUS、47項 COVERAGE 和必要 DECISIONS／ADR，不強推、不提交測試存檔。
