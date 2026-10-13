# 地圖版更新 — 2026-10-13

依使用者要求，移除週次、閱讀進度、localStorage、互動練習、作業與評量；保留九主題、來源與重點導讀。下方是初版歷史檢查，涉及已移除功能的項目不再適用。

# 驗證紀錄 — 2026-10-13

- 已透過 arXiv、官方／作者 GitHub、Anthropic 官方文章核對 14 個唯一來源。
- 9 個單元、18 題檢核題；HTML IDs 無重複，所有內部錨點與本機資源存在。
- Python 編譯、JavaScript 語法檢查通過；本機 HTTP 回傳 200。
- 瀏覽器確認：搜尋 LoRA 顯示 1 個單元，知識增強篩選顯示 3 個單元，無匹配字詞顯示空結果提示。
- 勾選 Attention 後進度為 1/9，重新載入仍為 1/9；重設後為 0/9。
- 原生 details 可由鍵盤展開。390px 手機視窗沒有水平溢出。
- Attention 練習 τ=1 時輸出 14.25，遮罩第三位置後輸出 12.69，第三位置權重為 0。
- 未執行教材要求的模型訓練／研究實驗；這些是學生實作任務，不是本網站聲稱完成的研究結果。

## 發佈狀態

更新後的 PAT 已成功建立並推送 `gradinnovate-capstone/115-project`，GitHub Pages 已設定為 main 分支的 /docs。

- Repository：https://github.com/gradinnovate-capstone/115-project
- Pages：https://gradinnovate-capstone.github.io/115-project/

每次 push 後需等待 Pages build 完成；部署狀態以 GitHub Pages 與線上網站為準。
