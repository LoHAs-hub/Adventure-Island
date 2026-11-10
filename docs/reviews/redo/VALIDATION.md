# 本輪重做：正式遊戲驗證

2026-11-10（Asia/Taipei）。本輪從重新上傳的原始 ZIP 重做，不沿用 d1942ae 的實作或測試結論。M0～M5 的改版內容已整合並可遊玩；以下 PASS 僅指已執行案例，不表示使用者已驗收或全部組合已窮舉。原碼基準 SHA 見 START-HERE，最新遊戲／來源 commit 與封裝 SHA 見 `releases/REDO-RELEASE.json`。

## 環境與方法

Linux／Chromium 156.0.8078.79／Node 24.22.1／Playwright；隔離 BrowserContext，不使用玩家存檔。以本機 HTTP 載入正式 `game/index.html`。三桌機 1280×720、1440×900、1920×1080；另測800／390寬、DPR2與真正全螢幕。完全離線測試直接提供相同 HTML 並禁止全部外部請求；managed Chrome 禁止直接 `file://`，因此不宣稱該路徑實測通過。

所有結果 JSON、截圖與腳本均可核對。`RUN.json` 記錄本輪建置／證據雜湊，`COMPARISON.html`／PNG為前後對照。樣板與靜態聯絡表各有用途，不代替正式戰鬥測試。

## 需求逐項結果

「部分」表示列出案例已通過，但該驗收 ID 含有本環境未完整覆蓋的範圍；不是把未測項目標成 PASS。

| ID | 結果 | 實際證據與界線 |
|---|---|---|
| V01 | PASS | core：三桌機固定比較／主行動在視窗內，Canvas 16:9；800／390無水平溢出。1280主行動底部681px、1440為867px、1920為1043px。 |
| V02 | 部分 | core/state/events：滑鼠、雙擊、鍵盤焦點、鎖定／選取、等級不足、彈窗Tab／Escape、焦點返回；處理中由真實NET ACK狀態顯示。未逐一窮舉全部原系統控制項的所有互動狀態。 |
| V03 | 部分 | contrast：17個正式頁1269個DOM文字樣本，合成背景及透明度後最小4.90:1，無低於4.5:1正文／3:1大字門檻。稀有度有文字標籤、裝備有狀態形狀。未對全部Canvas文字／所有組合做對比認證。 |
| V04 | PASS（抽樣） | state/core/event：超長名稱有完整title、萬／億、正負差值、等級不足、空包／篩選無結果、鎖定與滿包；主要行動仍可達。不是任意長度／任意數值的形式證明。 |
| V05 | PASS（渲染） | views：26個原節點逐一經原show/render入口檢視，m0/m17導向新首頁，m18保留舊導航；8個養成分頁有正式截圖。沒有以空白節點冒充新功能。 |
| G01 | PASS | core＋live-trace：同一G推進、AUTO、攻擊／擊倒持續，收合／展開／切素質／自動穿裝不重開、不隱式pause；15個真實時間樣本。 |
| G02 | PASS | core/state/trace：SVD／statsOf／actor一致；確認換裝立即提交，動態帳號加成每步核對。真實rollP在原讀值時機取得新能力；HUD／摘要同源。 |
| G03 | PASS（抽樣） | core/event/state：HP／MP絕對值、降上限限制、提高上限不補血、死亡不復活、CD／怒氣／進化evH不重置；原升級補滿有效。未窮舉所有進化／升級同幀交錯。 |
| G04 | PASS（已測入口） | core/event/trace：按鈕、實際指標雙擊、卸下、一鍵穿裝，以及原en/sf/cube/papply/flame/fapply路徑；當前出戰能力與正式公式一致。預覽與實際提交分開。 |
| G05 | PASS | state：真實fireShot物件、攻擊am／hit與實際hurtE建立的灼燒傷害快照保持；rollP在原時機取更新S。preservation：fireShot／updPr／spStep等原函式相同，沒有強制把原動態投射物改成快照。 |
| B01 | PASS | core：持續addInv時背包DOM／scrollTop／選取ID不變；新到貨計數，明確更新後加入。排序由原cp公式，不用陣列位置當身分。 |
| B02 | PASS | core：確認後新到貨不加入固定ID集合，途中鎖定物重驗且保留；已穿戴也排除。原進階分解同樣固定確認ID。 |
| B03 | PASS（抽樣） | event/core：全部鎖定的滿包保留舊ID、新到貨真實出售；自動分解／入包／售出記錄實際去向，已消失物不可穿戴。通知不宣稱必然入包。 |
| B04 | PASS（抽樣） | state：2件套裝門檻，預覽與套用公式相同；等級限制、低稀有高攻擊裝備、換其他角色不刷新當前角色。未窮舉全部套裝／流派組合。 |
| I01 | PASS（桌機） | core/state：管理區點擊／雙擊／輸入不攻擊，焦點在換裝後保留；兩視窗、DPR2、全螢幕實際點擊HUDA開關正確。實機觸控未完整驗證。 |
| I02 | 部分 | state/event：原endStage一次性、下一關、選取清理、死亡／升級／重載；network：斷線不被原模擬復活。實機背景休眠／回前景與超長掛機未完整驗證。 |
| S01 | 部分 | preservation/core/state：以原版生成的v3/v4/v5資料與原遷移結果逐項比對；角色、裝備／鎖定ID與重載一致；真實下載匯出及檔案匯入確認往返。沒有全部歷史玩家實檔可測。 |
| N01 | 部分 | network：兩真實頁BroadcastChannel、原房主模擬；雙端換裝／ACK、掉ACK重送、過期場次／版本、未知ID及偽造已知主屬性拒絕、房主掉落授予、UID避碰、清單水位裁剪、斷線與回大廳重開新場次。外網WebRTC／STUN與實機網路未驗證。 |
| A01 | PASS（資料／繪圖） | art：5職業／12分支（12個不同影像）、8臉／12髮／6膚／14服裝與彩虹髮；建角／美容／選角／戰鬥共用Art.char。不是全部外觀×每幀的窮舉。 |
| A02 | PASS（映射／抽樣） | art/ASSET-MAP：T288＝5玩家＋283敵方、13母型全繪圖入口遍歷；保留sc、配色、三頭龍／蠍尾／葉／鬃毛／王冠／光核等差異。聯絡表對大體型縮小展示，不改正式碰撞。 |
| A03 | 部分 | art：9寵物、5神獸及覺醒繪圖、出戰顯示與原跟隨入口；資料／能力／拾取程式維持原引擎。未逐一遊玩全部夥伴、星級、攻擊與拾取交叉組合。 |
| A04 | PASS（繪圖／數據） | art/comparison：10個主題、遠中近地標、原STG.tint與FY284／ZM122；門、掉落與地面互動沿原座標。十主題聯絡表及正式戰場截圖。 |
| C01 | PASS（邊界抽樣） | hazards：27個bossSp／hitBox實際內外邊界樣本全一致，原fan五彈道；落雷顯示改48×24、衝撞完整掃掠，只修視覺。安全內圈與危險外圈區分，描邊在FX上層。 |
| C02 | PASS（受控場景） | hazards：低／中／高畫質各6招、80粒子，警告／HUD仍有；performance：37實體／50粒子。沒有新增鏡頭震動。未窮舉最極端同屏夥伴×技能組合。 |
| E01 | PASS（已測流程） | event：真實10／100連、跳過／退出不再發獎、少動態立即結果、再抽、貨幣不足。發獎仍由原doGacha/gachaOne，結果顯示真實裝備去向。 |
| E02 | PASS（抽樣） | state/event：原升級補滿、離線收益／領取不重發、結算一次性與下一關；模態焦點、少動態僅縮裝飾。實機休眠與全部事件互相交錯未窮舉。 |
| P01 | PASS（同機微基準） | performance：相同種子、資料規模、尺寸／backing與畫質；150次render＋20次實際選裝，另記heap；連續render背包DOM變更0。不是持續FPS／記憶體成長率或所有設備保證。 |
| R01 | PASS（本環境） | 建置／Node語法、全部正式腳本無pageerror；完全離線相同HTML、零外部請求可戰鬥。直接fileURL被環境政策阻擋；外部P2P服務失敗仍沿原回饋，未在實網驗證。 |

## 原玩法與資料保護

`preservation-results.json` 記錄37個核心函式的SHA，包括statsOf、cpOfS、genItem/genAnc、gachaOne、rollP、攻擊／技能／大絕、bossSp／hitBox／hurtP、fireShot／updPr、poseOf／animate、loadSave／fixSave／migrate4/5、offlineGain與endStage。這些函式與不可變原碼字串相同。doGacha移除唯一新增的結果去向註記後與原碼相同，未變成本／權重／發獎。

主要數值表序列化SHA相同：`4f817e69cbe466640bf23408995f0a309af9ca3708fc5fe6b18efe193f4d3e57`。保護表包括T／CH／SL／RAR／AT／KF／ANK／STG／PETS／BEASTS／DF／PV／套裝／神器／魂石／技能符文／圖騰／轉蛋與轉職門檻。

有意修改的行為：戰鬥內裝備／養成提交、管理生命週期／焦點、固定ID安全整理、鎖定滿包保護、UID避碰與NET版本同步、首次冒險AUTO ON。沒有調整掉率／平衡／傷害判定。原雨圈與衝撞顯示不吻合判定的部分改的是顯示，原判定函式相同。

## 效能實測

同一Chromium程序、隔離context，1440×900、固定Canvas backing1200×675、37實體／50粒子／80裝備；各畫質150次同步render與20次實際選裝。效能腳本執行時沒有其他瀏覽器測試。

| 畫質 | 原render中位數 | 新render中位數 | 原選裝中位數 | 新選裝中位數 |
|---|---:|---:|---:|---:|
| 低 | 5.40ms | 1.60ms | 12.80ms | 4.90ms |
| 高 | 4.90ms | 1.60ms | 14.60ms | 4.50ms |

詳細p95／最大值／heap見performance-results。單次heap約原9.5～10.1MB、新5.8～5.8MB，僅供此測試快照。新選裝只改比較／狀態及已讀NEW徽章，不全重建背包；連續繪圖背包childList變更為0。快取鍵為有限部位／稀有度／遠古型，日誌上限60，失效物品清單按事件水位裁剪；未以單次測試宣稱無記憶體洩漏。

## 可重現命令

先在專案根目錄執行建置與語法，再以Python HTTP伺服器提供檔案。需要本環境的Playwright及`/usr/bin/chromium`；一般機器可安裝相應開發依賴後調整executablePath。遊玩本身不需要這些工具。

```sh
node --expose-internals tools/build_redesign.cjs
python3 tools/check_syntax.py
python3 -m http.server 8000 --bind 127.0.0.1
```

另開終端執行core、network、events、states、views、preservation、art、hazards、contrast共9個`tools/test_redesign_*.cjs`；`node tools/trace_redesign.cjs`記錄真實戰鬥，`node tools/capture_redesign_comparison.cjs`產出相同狀態對照。最後單獨執行`node tools/test_redesign_performance.cjs`。證據寫入本目錄；隔離測試存檔僅在忽略的work/redo，不封裝或提交。

## 尚未完整驗證與已知界線

- 外網WebRTC／STUN、不同電腦與網路條件。雙分頁測試覆蓋相同NET處理與房主模擬，但不能替代外網測試；兩端須使用同版。斷線重開沿原大廳流程。
- 原本本機存檔信任界線：新協定有物品清單、主屬性檢查、房主公式重算與版本ACK，不是能驗證入房前帳號／本機養成亂數的防作弊服務。
- 全部歷史玩家實檔、全部職業／外觀／每幀／強化／套裝／夥伴交叉組合；現有是明確的資料遍歷與正式功能抽樣。
- 多設備長時間掛機、實機背景休眠／回前景、真實觸控與所有DPR；本輪沒有這些實機。
- managed Chrome的直接fileURL路徑。相同HTML完全離線已通過，沒有外部靜態依賴；原單檔使用方式及匯入匯出仍保留。

前次未通過的證據在`../implementation/`，只供歷史比較；其PASS不適用本輪。
