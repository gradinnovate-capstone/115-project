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

本機成品已完成，尚未推送或部署。最新發佈嘗試可讀取組織，但建立 `gradinnovate-capstone/115-project` 時收到 GitHub HTTP 403：

> You need admin access to the organization before adding a repository to it.

請由有權限的管理員建立 repo 並授予 PAT 存取，或調整組織／PAT 的建立 repo 權限。之後執行 README 的發佈命令，並另行確認 Pages build 與線上 HTTP 狀態。不要把預定網址視為已上線網址。
