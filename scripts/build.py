from pathlib import Path
import json, html
ROOT=Path(__file__).resolve().parents[1]
modules=json.loads((ROOT/'content/modules.json').read_text())
e=html.escape
cards=[]
for i,m in enumerate(modules,1):
 sources=''.join(f'<li><a href="{e(url)}" target="_blank" rel="noopener noreferrer">{e(title)} ↗</a><small>{e(meta)}</small></li>' for title,meta,url in m['sources'])
 concepts=''.join(f'<li>{e(x)}</li>' for x in m['concepts'])
 cards.append(f'''<article class="module" id="{m['id']}" data-stage="{m['stage']}">
 <div class="module-heading"><span class="number">{i:02}</span><div><div class="meta">{m['stage']} · {m['level']}</div><h3>{m['title']}</h3><p class="subtitle">{m['subtitle']}</p></div></div>
 <p>{m['intro']}</p><p class="prereq"><strong>先備知識</strong>　{m['prereq']}</p>
 <h4>從原始資料開始</h4><ul class="sources">{sources}</ul>
 <details class="lesson"><summary>展開重點導讀 <span aria-hidden="true">＋</span></summary><div class="lesson-body"><h4>三個核心觀念</h4><ol>{concepts}</ol><div class="formula">{e(m['formula'])}</div><h4>閱讀路徑</h4><p>{m['reading']}</p><p class="pitfall"><strong>辨析</strong>　{m['pitfall']}</p></div></details></article>''')
nav=''.join(f'<a href="#{m["id"]}"><span>{i:02}</span>{m["title"]}</a>' for i,m in enumerate(modules,1))
page='''<!doctype html>
<html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="煉金實驗室 A.L.C.H.E.M.Y｜115 學年度大學生專題 AI 學習地圖：Attention、Transformer、nanoGPT、RAG、GraphRAG、LoRA、Agent、Decision Models 與 RSI。"><meta name="theme-color" content="#173f37"><title>煉金實驗室 A.L.C.H.E.M.Y · 115 學年度大學生專題學習地圖</title><link rel="stylesheet" href="assets/style.css"><script src="assets/app.js" defer></script></head>
<body><a class="skip" href="#main">跳到主要內容</a><header class="top"><a class="brand" href="#"><b>煉金實驗室</b> A.L.C.H.E.M.Y</a><nav aria-label="主要導覽"><a href="#curriculum">學習地圖</a></nav><span class="year">115 學年度 · 2026–2027</span></header>
<main id="main"><section class="hero"><div><div class="eyebrow"><span class="dot"></span> A.L.C.H.E.M.Y / 115 學年度大學生專題學習地圖</div><h1>從一篇論文，<br>走到你的 <em>大學生專題。</em></h1><p class="lead">讀懂模型、連接知識、設計行動。<br>探索 9 個主題，串起 AI 的核心概念。</p><a class="primary" href="#curriculum">探索地圖 <span>↗</span></a><p class="hero-note">原始論文 × 開源實作 × 繁體中文導讀</p></div><div class="map" aria-label="學習路徑：模型基礎、知識增強、Agent 決策"><span class="map-label">YOUR LEARNING PATH</span><div class="path-node"><b>01</b><div><strong>理解模型</strong><small>Attention → Transformer → nanoGPT</small></div></div><div class="path-node"><b>02</b><div><strong>連接知識</strong><small>RAG → GraphRAG → LoRA</small></div></div><div class="path-node"><b>03</b><div><strong>設計行動</strong><small>Agent → Decision Models → RSI</small></div></div><div class="map-bottom"><span>READ. BUILD. EVALUATE.</span><span>↗</span></div></div></section>
<section class="start-note"><h2>如何使用這份指南</h2><p>依模型基礎、知識增強、Agent 決策三個方向探索。選擇有興趣的主題，閱讀原始論文、開源實作與重點導讀。</p><p>資料核對：2026-10-13。論文年份以首次公開版本為主，必要時另註會議年份；repo 內容會更新，實作時請記錄 commit SHA。</p></section>
<section id="curriculum" class="curriculum"><aside><div class="sticky"><div class="eyebrow">THE CURRICULUM</div><h2>你的學習地圖</h2><p class="muted">循序讀，也可以從問題出發。</p><nav class="module-nav" aria-label="單元導覽">NAV</nav></div></aside><div class="lessons"><div class="filters"><label for="search">找一個概念，開始探索</label><input id="search" type="search" placeholder="搜尋主題、論文、關鍵字…"><div class="chips" role="group" aria-label="篩選學習階段"><button class="active" aria-pressed="true" data-filter="全部">全部</button><button aria-pressed="false" data-filter="模型基礎">模型基礎</button><button aria-pressed="false" data-filter="知識增強">知識增強</button><button aria-pressed="false" data-filter="Agent 決策">Agent 決策</button></div><p id="result-count" role="status">顯示 9 個單元</p></div>CARDS<p id="empty" hidden>找不到符合的單元，試試其他關鍵字或選擇「全部」。</p></div></section>
</main><footer><a class="brand" href="#">煉金實驗室 / A.L.C.H.E.M.Y</a><p>煉金實驗室 · 115 學年度大學生專題學習資料</p><p>導讀為教學整理；論文、程式與商標之權利屬原作者。請由各單元連結閱讀原文。</p></footer><noscript><p>JavaScript 未啟用：論文連結與導讀仍可閱讀；搜尋與篩選需啟用 JavaScript。</p></noscript></body></html>'''
(ROOT/'docs/index.html').write_text(page.replace('NAV',nav).replace('CARDS','\n'.join(cards)))
(ROOT/'docs/.nojekyll').touch()
print(f'Built {len(modules)} modules')
