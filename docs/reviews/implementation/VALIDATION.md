# 正式遊戲驗證紀錄

2026-11-10（Asia/Taipei），Chromium／Playwright，Linux managed cloud。測試使用隔離 BrowserContext 與暫時存檔，未將玩家／測試存檔提交。對象為正式 game/index.html，非互動樣板。

## 可玩版本與已實作內容

保留原單檔 JavaScript／Canvas 遊戲及所有資料、玩法與存檔流程。共用UI、左右管理、正式公式比較、素質、持續戰鬥即時換裝、掉落／固定ID整理、所有系統頁、向量圖示、人物與敵人／夥伴輪廓、十場景、動作材質、命中／預警、轉蛋與少動態已整合。

原動作關節、攻擊／技能取值和時間表繼續使用。5職業各分支、外觀8／12／6／14資料項、T的288定義（5玩家＋283敵方／13母型）、9寵物、5神獸、10場景有正式繪圖聯絡表。這不等於所有攻擊幀與所有設備均已人工逐一驗收。

## 驗收矩陣

「通過」只涵蓋右欄明載案例；「部分」保留未測組合，不能視為整項完成認證。

| 規格ID | 結果 | 實際證據／剩餘界線 |
|---|---|---|
| V01 | 通過 | core-results：1280×720、1440×900、1920×1080、800／390寬無水平溢出；Canvas 16:9；管理局部捲動 |
| V02 | 部分 | event-results：真正滑鼠雙擊、鍵盤背包選取、彈窗返回焦點；尚未遍歷全部不可用／處理中／懸停組合 |
| V03 | 部分 | state-results：6組核心文字／底色對比均≥4.5；未量測全部Canvas／稀有色逐像素對比 |
| V04 | 部分 | 長名稱、大數字、空篩選、滿鎖定背包通過；所有系統極值組合未窮舉 |
| V05 | 通過 | visual-results：26節點各有入口判定與截圖；m0導向m17，m18保留舊共用導航；各養成分頁均渲染 |
| G01 | 通過 | live-trace：12個連續樣本，同一G、持續模擬、收展／分頁／一鍵換裝時不pause |
| G02 | 通過 | core-results：實際裝備提交後SVD公式與actor.S相同；同G、HP/MP/CD/rage保留；NET另有雙端測試 |
| G03 | 部分 | core/state：提高上限不補血、降低上限夾回、死亡不復活、既存evH保留；同幀升級＋進化到期組合未窮舉 |
| G04 | 部分 | event/core/live-trace：按鈕、真雙擊、卸下、一鍵穿裝、穿戴物強化通過；星力／潛能／星火／自動洗已接單一入口但未逐項機率回歸 |
| G05 | 部分 | 冷卻、怒氣、原攻擊狀態不重建；rollP及攻擊時間表指紋一致；未逐一追蹤飛行中投射物／DoT |
| B01 | 通過 | core：到貨保留同ID與同DOM；手動「更新背包」才重排，篩選仍保留選取 |
| B02 | 通過 | core：確認固定ID，新到貨不加入、鎖定重驗；穿戴物不在背包候選 |
| B03 | 部分 | core/state：自動分解與滿包出售真實去向、鎖定物安全；不存在物品按鈕不提交；轉蛋結果附物品實際去向。完整滿包＋跨端斷線組合未全測 |
| B04 | 部分 | cpOf／statsOf／套裝表未改；比較顯示正負差；全部套裝跨門檻及等級限制組合未窮舉 |
| I01 | 部分 | 管理鍵盤不攻擊、真正雙擊與五尺寸映射通過；所有DPR／全螢幕／實機觸控未窮舉 |
| I02 | 部分 | 結束／收展生命週期及連線斷線已處理；OS休眠／瀏覽器長時間背景／所有復活切關組合未全測 |
| S01 | 部分 | compatibility：原版v5存檔資料相同、v3/v4遷移結果與原版一致、重載ID保留；所有歷史玩家實檔及匯入匯出UI組合未全測 |
| N01 | 部分 | network：同源雙分頁房主／訪客換裝、ACK、舊場次／版本、未知物品ID拒絕、斷線角色保持離場；外網WebRTC/STUN與完整重連未驗證 |
| A01 | 部分 | atlas-characters／motion：5職業BR、外觀ID與基礎動作同源渲染；完整逐幀與每個美容預覽組合未全測 |
| A02 | 通過（資料渲染） | visual-results／atlas-enemies：全部T定義映射，13母型與BOSS參數保留；非逐幀戰鬥認證 |
| A03 | 部分 | atlas-companions：9寵物、5神獸及覺醒渲染；全部拾取／攻擊／復活組合未全測 |
| A04 | 通過（渲染） | atlas-worlds：10主題，原FY／ZM／STG.tint不改；各關卡氣氛粒子組合未逐一體驗 |
| C01 | 部分 | hazard-results：slam/charge/rain/laser/nova/fan高低畫質與密集粒子，描邊重用原幾何；逐招真實碰撞組合未全測 |
| C02 | 部分 | quality-l/m/h及warning-l/h圖片無錯誤；低畫質保留必要預警／HUD；全技能＋最高密度長時間實機未全測 |
| E01 | 部分 | event：十／百連、跳過、離開不重複發獎、少動態結果可退出；稀有率極端與每次重抽中斷組合未窮舉 |
| E02 | 部分 | 彈窗焦點與原lvFx保留；所有結算／離線收益／復活重開組合未全測 |
| P01 | 部分 | performance-results固定種子同畫布微基準；非全設備長時間FPS／記憶體洩漏認證 |
| R01 | 部分 | 語法、正式主要流程無pageerror；完全離線環境載入同一HTML且零外部資源通過。managed Chrome禁止file://，所以直接檔案URL開啟未測；外網連線仍需原有服務 |

## 公式與資料保護

compatibility-results.json 保存函式與資料表SHA。statsOf、cpOfS、genItem、genAnc、rollP、startAtk／Sp／Ult、stepE、addXp、refreshP與存檔遷移原碼相同。doGacha僅新增結果去向文字與CSS變數，測試移除這兩項展示註記後確認發獎／抽取原碼一致。CH/T/SL/RAR/AT/KF/ANK/STG/PETS/BEASTS/DF/PV/SETB/ANCB/ARTS/SOULS/SRN/TOT/GACHA/JOBLV/JOBCOST序列化一致。

原本兩項缺陷因本次流程暴露而修正：滿包沒有未鎖定候選時不再回退出售索引0；連線離線角色不再被後續模擬自動復活。未更改掉率、平衡、攻擊判定或收費機制。

## 網路信任界線

背包仍屬各端本機SVD。房主保存入房物品清單及自己發出的loot ID，裝備更新僅接受已知ID／角色／部位／系列，再重算正式能力；不接受客端任意st當更新。場次／版本／ACK處理重送與過期事件。入房前本機存檔真偽、強化隨機結果與花費仍在原本信任邊界，這不是新防作弊伺服器。

## 重現方式

先 `python tools/prepare_baseline.py`（有Git用3625d38；ZIP使用保留的v0.4設計ZIP取原HTML）。在根目錄 `python -m http.server 8000`。Node需Playwright及Chromium；執行 tools/check_syntax.py、check_game.cjs、check_network.cjs、check_events.cjs、check_compatibility.cjs、check_states.cjs、check_visuals.cjs、check_hazards.cjs、check_performance.cjs、record_live_trace.cjs。效能測試獨立執行，避免其他測試爭用CPU。

測試所有樣本均可丟棄，不應覆寫玩家的本機存檔。GitHub完整原碼含工具，精簡可玩ZIP不含測試資料。
