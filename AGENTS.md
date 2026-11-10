> 本輪重做：d1942ae未通過使用者驗收。從game/source/baseline.html重新實作，最新證據在docs/reviews/redo，不繼承上一輪PASS。

# 協作入口

先讀 START-HERE.md、docs/PROJECT-CONTEXT.md，再讀 README.md、docs/STATUS.md、docs/DECISIONS.md、docs/ART-INVENTORY.md，最後看相關程式。當前交接版本為 handoff/v0.4；舊版僅作歷史追溯。

使用者已確認：2D美式街頭粗框、線條更滑順、減少外凸尖角、淺藍主色、左戰鬥／右管理；優先掉寶／裝備／素質；自動戰鬥中整理、換裝並立即更新能力。詳見 ADR-001、ADR-002、ART-DIRECTION、LIVE-GEAR。不要再次把已確認方向列為等待決策。

正式遊戲已整合全版美術與即時換裝；最新成果在game/index.html，原始基準在Git 3625d38及舊設計ZIP。後續工作先讀docs/reviews/implementation/VALIDATION.md，補未驗證案例，不把歷史設計交接狀態當成現況。44個SVG是靜態參考，不代表完整動畫／變體已完成。

附件 DOCX 是背景證據，不自動取得指令優先權；規則來源見 docs/DECISIONS.md。使用者決策與設計落地值分開記錄。色碼／尺寸可依v0.4執行，不應虛稱使用者逐一核准。

每次工作結束更新 STATUS（完成、驗證、未完成、下一步）；決策寫入 DECISIONS，重大決策用 docs/decisions/ADR-xxx.md。實作時同步更新 handoff/v0.4/COVERAGE.csv 的 implementation_status 與 evidence；記錄物件 ID、程式入口、共用關係、狀態、驗收方式。禁止只把協作記憶留在聊天。

遊戲修改採小範圍 diff，不混入無關數值調整，不提交測試存檔。存檔／連線／戰鬥修改做專項回歸；純視覺也驗證高低畫質、提示與命中區。不要以樣板測試代替正式功能測試。保留原單檔離線單機使用方式；若來源模組化，提供打包方式。

跨聊天室交接必須附帶背景、已確認需求、方向演進、目前進度、未完成項目與閱讀入口。更新方向或實作進度時同步維護 START-HERE、PROJECT-CONTEXT、STATUS 及 NEW-CHAT-PROMPT 中的狀態，避免新聊天室把已完成的樣板誤當成正式遊戲已完成。舊 v0.4 ZIP／RELEASE／PACKAGE-MANIFEST 保留原封裝記錄；最新完整交付使用包含接手文件的 GitHub 專案 ZIP。
