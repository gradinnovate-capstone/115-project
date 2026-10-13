import json,re,urllib.request,concurrent.futures,html
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
mods=json.loads((ROOT/'content/modules.json').read_text())
sources={x[2]:x[0] for m in mods for x in m['sources']}
def fetch(url):
 req=urllib.request.Request(url,headers={'User-Agent':'115-project-source-verification','Accept':'application/vnd.github+json' if 'api.github.com' in url else 'text/html'})
 with urllib.request.urlopen(req,timeout=40) as r:return r.status,r.url,r.read().decode()
def norm(s):return re.sub(r'[^\w]','',html.unescape(s)).casefold()
def check(item):
 url,title=item
 try:
  if 'arxiv.org/abs/' in url:
   status,final,body=fetch(url)
   match=re.search(r'<meta\s+name=["\']citation_title["\']\s+content=["\'](.*?)["\']\s*/?>',body,re.I)
   if not match:raise ValueError('citation_title missing')
   official=html.unescape(match.group(1))
   return {'url':url,'http':status,'listed_title':title,'official_title':official,'match':title==official,'type':'paper'}
  if 'github.com/' in url:
   slug=url.split('github.com/',1)[1].strip('/')
   status,final,body=fetch('https://api.github.com/repos/'+slug);d=json.loads(body)
   return {'url':url,'http':status,'listed_title':title,'full_name':d['full_name'],'canonical_url':d['html_url'],'match':d['full_name'].casefold()==slug.casefold() and norm(title)==norm(d['full_name']),'archived':d['archived'],'description':d['description'],'type':'repo'}
  status,final,body=fetch(url)
  match=re.search(r'<title[^>]*>(.*?)</title>',body,re.S|re.I)
  return {'url':url,'http':status,'listed_title':title,'page_title':html.unescape(match.group(1)) if match else None,'type':'blog'}
 except Exception as e:return {'url':url,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:results=list(pool.map(check,sources.items()))
(ROOT/'source-check.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
for x in results:print(json.dumps(x,ensure_ascii=False))
