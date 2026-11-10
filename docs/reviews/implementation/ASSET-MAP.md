# 正式素材映射與降級

單檔來源 game/index.html；原版繪圖參數／姿勢／判定保持原資料，不使用樣板假資料。

| ID | 正式入口／變體 | 錨點與狀態 | 降級／證據 |
|---|---|---|---|
| UI／全部面板 | show／menuGo／PANELS／共用 CSS | 26 節點；m0 導向 m17，m18 舊導向仍由共用樣式覆蓋 | system-m*.png；visual-results.json |
| 裝備圖示 | COMIC_ICONS／COMIC_SLOT／comicIcon／itemIconC | 12 部位、5 職業武器與槍手；單檔內嵌 SVG；快取包含武器形狀／稀有度／遠古系列 | SVG 無外部請求；原 ID／稀有度7階保留 |
| 玩家／外觀 | drawChibi／apOfP／chHairFront／chHairBack／chWeapon | 原腳底、800×450座標；12平順髮型、8臉、6膚、14服裝資料項；5職業BR全部分支；待機武器向外避免遮臉 | atlas-characters.png；選角／美容／建角共用；彩虹髮色保留獨立平塗條帶 |
| 敵人 | dEnt／13 draw*母型 | T共288定義含5玩家，敵方283；原sc／朝向／出生／動畫／配色／BOSS裝飾 | atlas-enemies.png；全部資料映射；非逐幀動畫驗收 |
| 寵物／神獸 | drawPet／drawPets／drawBeast／drawBeastF | 9寵物、5神獸；保留原追隨、攻擊、拾取位置與覺醒／星級 | atlas-companions.png；低畫質減光暈 |
| 動作 | KF／poseOf／animate／chWeapon | 原關節與時間表不變；套用新輪廓與平塗；只有非攻擊武器朝向視覺調整 | compatibility-results.json 核對KF／ANK；逐攻擊幀組合未全部實測 |
| 場景 | bg／COMIC_THEMES | 10主題、遠景.15／中景.45、原FY／ZM／STG.tint | atlas-worlds.png；低畫質移除邊緣網點 |
| 預警 | drawTele／warningEdges／teleHud | 原drawTele精確路徑再描邊，位於特效之上；衝撞同原280×32；不改判定 | 高低畫質截圖；每招碰撞完整組合仍列未驗證 |
| 特效／地面 | drawSlash／drawSp／drawUlt／dPr／dFx／dItem／drawPortals | 平順接筆、圓弧命中、原生命週期／發獎／互動點；保留原必要形狀 | quality-l/m/h.png；低畫質與少動態減裝飾粒子 |
| 事件 | gAnim／GACHA_RUN／showModal／lvFx | 結果與發獎分離；跳過清計時器、鍵盤可跳過、少動態直接結果；無鏡頭震動 | event-results.json；轉蛋十／百連測試 |
