# 正式實作任務與 M0 證據

2026-11-10 Asia/Taipei。來源 work / 3625d38；附件與遠端 game SHA256 均為 63a018e13af27da20a7493918ecb3719faba09a1059a36fb6dd0da96529c09be。

- [x] M0：依序讀入口、規格與全部覆蓋清單；原腳本語法通過；隔離 Chromium context 建立基準圖片 before-*.png。
- [x] M1：共用 tokens、左右管理、比較及素質。
- [x] M2：同步入口、固定物品 ID、真實掉落去向、連線版本／確認。
- [x] M3：全部 panel 的共用樣式與可達性。
- [x] M4：角色／母型／夥伴／場景／特效及預警。
- [x] M5：事件動畫、少動態、回歸、打包與推送。

## 原碼映射

面板清單 PANELS（26）：m0 為 HUB 導向空殼；m18 強化舊入口，實際養成由 m4 共用；m30 每日舊入口；其他保留 show／menuGo 原路由，不新增玩法。

DOM 管理 renderGrowth／detHTML／invSorted；能力 statsOf／cpWith；所有持久變更 saveG；自動洗潛能每三次 saveG，需另接每次實際套用。場上 refreshP 已保留 HP／MP 絕對值與原進化 evH。所有角色、怪物繪圖經 drawChibi／dEnt，預覽共用 X。Canvas 800×450、HUDA 保留。

NET 背包為每端 SVD 自有，房主原本只收到 hello 的 st，並無中央物品帳本。新增同步不得宣稱可驗證外部存檔真偽，須以原存檔信任邊界、房主重算、場次／版本／ACK 防止任意 st／過期更新；公開 P2P 與 BC 分開列驗證。

M0～M5實作整合及交付已完成；驗收勾選不是所有案例全PASS，剩餘界線見VALIDATION.md。
