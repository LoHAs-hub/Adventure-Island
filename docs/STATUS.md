# 本輪重做：交付狀態

2026-11-10（Asia/Taipei）。M0～M5的正式實作、本環境驗證與交付內容完成；未驗證項目另列，不宣稱全組合／使用者驗收通過。使用者判定前次d1942ae不符預期，本輪直接從新上傳ZIP的原遊戲重做，沒有沿用該版程式或PASS。

## 當前入口

- 正式可玩：game/index.html；下載releases/Adventure-Island-v0.4-redo.zip。
- 新來源：game/redesign；不可變原碼：game/source/baseline.html；建置tools/build_redesign.cjs。
- 正式驗證：reviews/redo/VALIDATION.md及RUN.json；相同存檔／第90幀對照：COMPARISON.html／PNG。
- 最新來源commit／遊戲／封裝SHA：releases/REDO-RELEASE.json；已授權Git origin／work保存本輪提交，不改寫歷史。
- 47項COVERAGE皆有本輪實作狀態與實際證據檔路徑；舊發布移至releases/rejected，舊reviews/implementation明標失敗歷史。

## M0～M5結果

| 批次 | 已完成 | 證據 |
|---|---|---|
| M0 | 重讀交接、核對ZIP／Git基準、隔離存檔、保存原HTML與映射 | preservation-results／ASSET-MAP |
| M1 | 共用UI、58/42布局、固定背包／12部位／比較／主行動、素質 | core-results／contrast-results／三桌機截圖 |
| M2 | 即時裝備及養成、原能力同步／資源保留、固定ID整理／真實去向、舊檔及雙端同步 | core／state／event／network／live-trace |
| M3 | 全部26原節點、8養成分頁、封面／導航／提示／彈窗／焦點 | views／state／contrast及system-* |
| M4 | 5職業12分支與外觀、13母型283敵方、9寵物5神獸、10場景、動作／HUD／警告／特效 | art／hazard／preservation及聯絡表 |
| M5 | 十百連／少動態／事件、原碼保護、前後對照、同機效能、來源與可玩封裝 | event／state／comparison／performance／RUN／MANIFEST |

所有正式瀏覽器腳本執行無pageerror。37個核心函式與主要數值表SHA等於原始基準，doGacha僅增結果去向註記。沒有改掉率、公式、平衡、攻擊判定或付費。雨圈與衝撞只修正預警顯示以符合原判定。

## 未完整驗證／下一步

外網WebRTC／STUN、真實跨設備與觸控、長時間掛機／背景休眠、全部歷史玩家實檔，以及所有外觀／每幀／強化／套裝／夥伴交叉組合。相同HTML完全離線已通過；本環境政策阻擋直接fileURL。NET仍沿用本機帳號信任界線，不宣稱新防作弊服務。逐ID界線見VALIDATION。

後續依使用者對本輪的實際回饋修正，或針對上述項目補實機驗證；不要重新等待已定案風格確認。使用者尚未驗收本輪品質。

## 分批紀錄

以下保留本輪推進時的紀錄；其中「待完成」描述是當時狀態，已由上表與最新證據更新。

# 重新實作狀態

使用者判定 d1942ae 版本不符預期，未通過驗收；保留Git歷史，不作本輪基準。本輪從重新上傳的3625d38原始ZIP開始，game/source/baseline.html SHA256=63a018e13af27da20a7493918ecb3719faba09a1059a36fb6dd0da96529c09be。

M0：文件、原碼、樣板已重讀；建立原始來源與重做計畫。M1～M5進行中；不繼承前次測試結論。新證據目錄docs/reviews/redo。

本輪目標：原遊戲數值與完整玩法保留；依v0.4重新製作固定背包／比較／換裝行動的管理區、全頁共用UI、正式程序美術。原44SVG作參考，不以靜態圖替代動畫。公式、判定及攻擊幀保持基準。

## M1／M2 首批證據

已完成全新框架、固定管理區與原引擎接線；正式測試見docs/reviews/redo/core-results.json。三桌機尺寸的比較區／主行動均在視窗內，另測800/390寬無水平溢出；同G持續、按鈕／雙擊／卸下／原生強化、資源與冷卻保留、固定ID批次、新到貨DOM不變及重載通過。多人與全系統仍在本輪驗證，M3～M5未結案。

## M3／M4證據

本輪26節點與8個原養成分頁渲染通過；房主／訪客換裝、ACK、過期訊息與未知ID拒絕通過。角色5職業／12分支及外觀資料、283敵方、9寵物／5神獸、10場景聯絡表已產出（僅作資料映射，不代替遊玩驗收）。27個實際預警命中邊界演算與新顯示一致；原判定保持不變。映射見reviews/redo/ASSET-MAP.md。M5仍在執行。

## M5 專項修正與證據（封裝前）

已移除封面／大絕／遠征／秘境／畫面外指示的舊版光暈與斜切覆蓋，補齊三頭龍、蠍尾、樹葉、鬃毛、護盾／破防與蓄力提示。危險描邊維持在FX上層。離場後立即進養成不再被下一幀首頁覆寫；共用彈窗／轉蛋焦點有返回與Tab路由。

雙分頁新增實際房主掉落接收／換裝、已知主屬性偽造拒絕與清單裁剪測試；保留既有ID，後續UID避開已知對端物品，避免原本各端遞增UID碰撞。來源內含本機帳號信任限制，不宣稱防作弊。

state-results.json：真實fireShot／灼燒快照、換其他角色、套裝2件門檻、原升級補滿、DPR2／全螢幕HUD、結算一次性與下一關、存檔下載／檔案匯入、離線收益一次性通過。contrast-results.json：17正式頁共用文字，合成透明度後無低於各字級門檻的樣本；不包括Canvas文字的全域認證。效能與最終封裝仍在完成。
