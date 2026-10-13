# 115 學年度學習網站設計

使用繁體中文，服務具 Python 與基本機器學習概念的專題學生。

使用者指定 GitHub Pages，採 buildless HTML/CSS/JS；Python 僅用於把單元 JSON 編譯成可直接閱讀的 HTML。不需要伺服器或第三方 CDN。比起 SPA，靜態 HTML 可在 JavaScript 不可用時閱讀全部核心內容；比起純 README，提供篩選與本機學習進度。

九單元分成模型基礎、知識增強、Agent 決策三階段。RSI 定義為 Recursive Self-Improvement；decision model 依使用者確認涵蓋 agent 決策與推理及 Decision Transformer。

介面採暖白、深綠與淡綠，雙欄桌面導覽、單欄手機版面。語意化 heading、label、原生 details、鍵盤 focus 與減少動態效果。進度儲存失败時提示使用者且不妨礙閱讀。

驗證涵蓋來源對應、靜態資源與錨點、JS 語法、搜尋／篩選、localStorage 進度保存、互動 softmax 和手機版面。

發佈目標為 main 的 /docs。GitHub PAT 不納入版本控管。若組織拒絕存取，保留可發佈成品並回報精確阻礙。
