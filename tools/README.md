# 工具版本辨識

目前正式來源建置：build_redesign.cjs（Node --expose-internals），來源為game/source/baseline.html＋game/redesign。check_syntax.py檢查生成HTML。

本輪驗證：test_redesign_core/network/events/states/views/preservation/art/hazards/contrast/performance.cjs、trace_redesign.cjs、capture_redesign_comparison.cjs。環境與步驟見docs/reviews/redo/VALIDATION；效能腳本單獨執行。

目前封裝工具：build_redesign_release.py。build_release.py保留相容入口，轉交目前工具。

check_game/check_network/check_visuals等check_*.cjs、prepare_baseline及record_live_trace是前次嘗試／設計階段的工具，沒有作為本輪通過依據。verify_handoff檢查設計交接結構，不能代替正式功能驗證。
