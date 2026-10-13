# 煉金實驗室 A.L.C.H.E.M.Y — 115 學年度大學生專題學習地圖

繁體中文 AI 專題學習指南。115 學年度對應 2026–2027。

## 內容

學習地圖包含 9 個主題：

1. Attention：scaled dot-product attention 與 multi-head attention
2. Transformer / LLM：Attention Is All You Need、GPT-3
3. nanoGPT：訓練、驗證與生成
4. RAG：檢索與生成分開評估
5. GraphRAG：實體關係、社群摘要與全局問題
6. LoRA：低秩參數更新
7. Learn Claude Code：shareAI-lab 社群教學 repo 與 agent harness
8. Decision Models: Jev / TypeSafe
9. RSI：Darwin Gödel Machine

每個地圖節點包含原始來源、核心概念與閱讀路徑。
網站提供文字搜尋與主題篩選；不含進度追蹤、週次安排、互動練習或評量表。

## 編輯與預覽

無第三方前端依賴，不需要 npm 安裝。

```sh
python3 scripts/build.py
python3 -m http.server 8115 --bind 127.0.0.1 --directory docs
```

開啟 http://127.0.0.1:8115 。內容維護於 `content/modules.json`；HTML 由 `scripts/build.py` 產生；樣式與互動位於 `docs/assets/`。

## GitHub Pages 發佈

Repo：`gradinnovate-capstone/115-project`。
網站：`https://gradinnovate-capstone.github.io/115-project/`。

GitHub Pages 使用 **Deploy from a branch → main → /docs**。所有資源使用相對路徑，支援 project Pages 子路徑。每次更新需重新產生並提交 `docs/index.html`，push 後由 Pages 建置。

初次發佈可執行：

```sh
python3 scripts/publish.py --token-file /path/to/capstone-pat.env
```

腳本確認組織存取、必要時建立公開 repo、推送已提交的內容並設定 Pages。PAT 不會寫入 Git remote 或專案檔案；使用一般 push，不會 force push。需具備對應的 repository 建立／管理、Contents 與 Pages 權限，並符合組織的 token 政策。若要使用既有私人 repo，腳本不會變更可見性，Pages 是否可用取決於 GitHub 方案與組織設定。

發佈後請確認 Pages build 成功、網站回傳 HTTP 200，並開啟線上頁面。HTTP API 成功設定不等於部署完成。

## 來源與授權

來源核對日期：2026-10-13。來源連結與文獻年份保留於單元內容；repo 內容可能持續變動。導讀與實作為本課程整理，未複製論文全文或上游程式。原論文、程式、商標的權利及授權依原作者規定。實驗設定與評分比例屬教學建議，非原論文聲明。
