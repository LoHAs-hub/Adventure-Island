> 最新：使用者拒絕上一輪d1942ae，現在從新上傳原始ZIP重做。舊完成／驗證敘述屬前次未通過嘗試；本輪以docs/STATUS及reviews/redo為準。

# 冒險島後續協作入口

接續既有遊戲，不重做新遊戲。先讀 START-HERE → docs/PROJECT-CONTEXT → AGENTS → STATUS／DECISIONS → docs/reviews/implementation/VALIDATION.md、ASSET-MAP.md及COVERAGE.csv。

本輪已將淺藍漫畫風、左右管理、掉落／裝備／素質與戰鬥中即時換裝套進正式game/index.html，並完成共用系統頁、世界／角色／夥伴繪圖及事件演出整合。核心正式測試、雙分頁同步、舊存檔比對、聯絡表與前後截圖均在reviews/implementation。原始SHA基準不再是目前game檔案；以Git3625d38或保留設計ZIP取用。

後續重點是補VALIDATION的部分／未驗證案例：外網WebRTC／完整重連、全部強化入口與同幀進化升級、飛行投射物／DoT、逐招碰撞、完整存檔匯入匯出UI、所有歷史實檔與多設備長時間效能。不要把抽樣或資料聯絡表當成逐幀全驗收。

風格、主色及左右布局已定案；正式公式／掉率／攻擊時序不自行調整。保持Git work分支及Harness更新，使用已授權遠端；不需重新詢問風格。原IMPLEMENTATION_PROMPT保留為本次完整需求規格。
