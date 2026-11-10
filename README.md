# 冒險島

既有 JavaScript／Canvas 2D 遊戲，已將 v0.4 淺藍街頭漫畫風與戰鬥中即時換裝整合至正式 [game/index.html](game/index.html)。資料、公式、原玩法及單檔單機模式保留。

解壓後開啟 game/index.html 即可單機遊玩；不需要安裝套件或架伺服器。進入冒險後右側可整理裝備／切換素質，戰鬥繼續；G展開整理、Escape收合。新掉落不搶比較，按「更新背包」才重排。換裝使用正式公式，HP／MP不免費補滿。

若換了檔案位置而瀏覽器視為另一個儲存來源，可從原版「設定」匯出，再於新版使用既有匯入功能。

- [最新狀態](docs/STATUS.md)
- [驗證與未驗證項目](docs/reviews/implementation/VALIDATION.md)
- [前後對照與截圖](docs/reviews/implementation/COMPARISON.html)
- [素材映射](docs/reviews/implementation/ASSET-MAP.md)
- [47項覆蓋清單](handoff/v0.4/COVERAGE.csv)
- [背景與決策](START-HERE.md)

完整設計規格與過往樣板仍保留於 handoff/v0.4、design/mockups/v0.4。它們是設計基準；正式成果與測試以game及docs/reviews/implementation為準。外網WebRTC、所有攻擊幀／碰撞組合及長時間跨設備效能仍未完整驗證，不能將本次測試視為全項驗收通過。
