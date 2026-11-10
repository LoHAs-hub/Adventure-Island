# 重新實作：正式來源映射

來源：game/source/baseline.html（不可變原HTML）＋game/redesign/*.js／style.css。Node內建Acorn按AST函式邊界接線，tools/build_redesign.cjs產出單檔game/index.html。禁止以舊失敗版為建置輸入。

| 覆蓋 | 正式來源／共用入口 | 變體與錨點／降級 | 證據 |
|---|---|---|---|
| 主框架／管理 | ui.js RUI；style.css | 固定背包、12格身上裝備、比較／行動；800×450 Canvas；右側進階原面板 | core-results／battle三尺寸 |
| 原系統 | 原show／render*保留，RUI.shown＋新元件CSS | 26節點、m0/m17導向新首頁、m18舊導航；原資料與頁面功能 | views-results／system-* |
| 裝備／UI圖示 | assets.js內嵌27SVG參考；icoImg／itemIconC | 12部位、7稀有度；武器依職業／分支；cache鍵含部位／稀有／遠古 | 裝備圖片／core-results |
| 玩家／轉職 | art.js Art.char／weapon／hair／hat；原apOfP加純顯示branch欄 | 5職業、12分支；盾／槍／弩／主教冠與杖等輪廓；8臉12髮6膚14服裝；原ID、腳底、sc、P關節 | art-results／atlas-characters／atlas-motion |
| 預覽 | drawPreview／drawCreate／Art.portrait／avatar | 戰鬥、選角、建角、美容同一char；預覽以畫布尺寸限縮武器／帽子邊界；非另一套素材 | system-m12／m14及首頁 |
| 敵方 | dEnt／Art.enemy／13 draw* | 原T288定義含5玩家＋283敵方；col/col2、sc、方向、boss/elite保留；13種獨立造型 | atlas-enemies／art-results |
| 寵物／神獸 | drawPet／Art.pet／drawBeast／Art.beast | 9寵物、5神獸與覺醒；沿用原跟隨位置／技能；低畫質不依賴glow辨識 | atlas-companions |
| 世界 | Art.landscape／themes／bg | 10種地標與3層視差；FY284／ZM122／STG.tint不改；低畫質移除邊緣網點 | atlas-worlds |
| 動作／技能 | 原poseOf／animate／KF／ANK；新drawSlash／Sp／Ult／dPr／dFx | 攻擊幀、CD與取值不改；proj/dash/up/aoe與beam/storm/blizzard/meteor/quake各有形狀；重用原狀態時間 | atlas-motion、preservation-results、正式戰鬥截圖 |
| HUD／警告 | hud／miniMap／goalHud／drawTele／Art.warningGeometry／warningTop | HUDA新座標與原滑鼠映射共用；高低畫質危險描邊在特效上方 | hazard-results／warning-l/h-* |
| 地面互動 | dItem／drawPortals | 原位置／碰撞不動；金幣、藥水、裝備、符文、輪迴、門的新形狀與稀有色帶 | 正式戰鬥截圖 |
| 事件 | effects.js gAnim／Reveal／showModal | 演出與原發獎分離；跳過／再抽／少動態／焦點返回；低頻單次揭曉 | event-results／gacha-* |

落雷視覺半徑改為48×24以符合原dz×2判定；衝撞預警涵蓋原f0=-30、f1=46+12×sc及30幀×9速度的整段路徑，深度±30。僅修正預警，不修改攻擊判定。27個實際bossSp／hitBox樣本與新顯示範圍一致。

連線背包仍採原本本機存檔信任界線；物品ID清單、房主重算與場次／版本ACK是同步保障，不宣稱可驗證入房前存檔或本機強化亂數。連線冒險中先提供裝備／養成，轉蛋在返回大廳後使用（原版也沒有戰鬥中轉蛋入口）。

M5來源補充：effects.js的render／titleLoop／teleHud／raidHud／hidHud／offArrows取代舊覆蓋效果；門在原世界錨點明確繪製，進化／蓄力／護盾破防與復活費用提示保留。art.js依原c.heads/tail/leaf/mane/bodyC/top/glow/crown顯示變體，wanc依原布林語意區分遠古與一般武器。

NET入房清單使UID前進到已知ID之後，addInv對收到ID亦前進UID，既有ID不改號。ledgerV4依event接收水位裁剪，保護尚未到達的房主授予。原本本機帳號／養成信任界線未改為防作弊服務。

正式對照採相同原版存檔與第90模擬幀，實體／位置／HP／擊倒數相等；comparison-results有斷言。效能與DOM對比見對應results，完整未驗證項見VALIDATION。
