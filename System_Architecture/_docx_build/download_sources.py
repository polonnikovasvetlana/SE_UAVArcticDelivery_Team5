from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from urllib.parse import urljoin
import requests, json, sys

ROOT = Path(__file__).resolve().parent
ROOT.mkdir(exist_ok=True)
URLS = {
 'flexrotor_page': 'https://www.airbus.com/en/products-services/helicopters/uas/u030-flexrotor',
 'flexrotor_pdf': 'https://mediaassets.airbus.com/pm_38_914_914595-i589qfifs1.pdf?fileName=airbus-flexrotor-brochure-for-land-and-maritime-operations.pdf',
 'ar3_page': 'https://www.tekever.com/ar3-evo/',
 'tango_page': 'https://www.elevonx.com/products/tango-vtol/',
 'tango_pdf': 'https://www.elevonx.com/wp-content/uploads/2025/05/ELVX_katalogA4_Tango_01.pdf',
 'ar3_pdf': 'https://www.tekever.com/wp-content/uploads/2026/03/TEKEVER_AR3EVO_AR3_Defence_2025_digital.pdf',
}
class Images(HTMLParser):
 def __init__(self): super().__init__(); self.items=[]
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if tag=='img': self.items.append({k:v for k,v in d.items() if k in ['src','alt','data-src','srcset']})
def get(item):
 name,url=item
 try:
  r=requests.get(url,timeout=30); r.raise_for_status()
  path=ROOT/(name+('.pdf' if '_pdf' in name else '.html'))
  path.write_bytes(r.content)
  if '_page' in name:
   parser=Images(); parser.feed(r.text)
   imgs=[i for i in parser.items if not any(x in i.get('src','').lower() for x in ['logo','icon','flag'])]
   print(name,json.dumps(imgs,ensure_ascii=False))
  else: print(name,len(r.content))
 except Exception as e: print(name,'ERROR',str(e))
if '--photos' in sys.argv:
 photos={
  'flexrotor': 'https://mediarenditions.airbus.com/PxPME7vRyqExXCFi4XL4Jp9RVwwV6Kn80Z2zWPZfNjw/resize?src=kpkp%3A%2F%2Fairbus%2F38%2F647%2F647451-x5g0m18lnj.jpg&w=780&h=520&poiX=50&poiY=50&el=false&t=fit',
  'ar3': 'https://www.tekever.com/wp-content/uploads/2026/02/AR3-Gallery1-scaled.jpg',
  'ar3_alt': 'https://www.tekever.com/wp-content/uploads/2026/02/20250805-_DSC0569_Youz-1-scaled.jpg',
  'tango': 'https://www.elevonx.com/wp-content/uploads/2025/11/ElevonX-Tango13.jpg',
 }
 def photo(item):
  name,url=item
  try:
   r=requests.get(url,timeout=25); r.raise_for_status(); (ROOT/(name+'.jpg')).write_bytes(r.content); print(name,len(r.content))
  except Exception as e: print(name,'ERROR',str(e))
 with ThreadPoolExecutor(max_workers=4) as pool: list(pool.map(photo,photos.items()))
 (ROOT/'photo_urls.json').write_text(json.dumps(photos,indent=2),encoding='utf-8')
else:
 with ThreadPoolExecutor(max_workers=6) as pool: list(pool.map(get,URLS.items()))
 (ROOT/'source_urls.json').write_text(json.dumps(URLS,indent=2),encoding='utf-8')
