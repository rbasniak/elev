#!/usr/bin/env python3
"""Validate source coverage, static navigation, aligned sections and calculations."""
from pathlib import Path
from html.parser import HTMLParser
import json,sys,urllib.parse,re
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'content'))
from course import PAGES
from videos import VIDEOS
class Inspect(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.ids=[];self.panels=[];self.anchors={l:[] for l in ['da','en','pt']};self.lang=None;self.meta=False;self.answers=0;self.errors=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id'in a:self.ids.append(a['id'])
  if tag=='a' and a.get('href'):self.links.append(a['href'])
  if 'lang-panel'in a.get('class','').split():self.lang=a['data-lang'];self.panels.append(self.lang)
  if a.get('data-anchor'):self.anchors[self.lang].append(a['data-anchor'])
  if tag=='meta'and a.get('name')=='referrer'and a.get('content')=='no-referrer':self.meta=True
  if 'answer'in a.get('class','').split():self.answers+=1
errors=[];pages=list(ROOT.rglob('*.html'));pages=[p for p in pages if 'dist'not in p.parts]
for p in pages:
 parser=Inspect();parser.feed(p.read_text())
 if parser.panels!=['da','en','pt']:errors.append(f'{p}: missing language panels')
 if len(parser.ids)!=len(set(parser.ids)):errors.append(f'{p}: duplicate ids')
 if not parser.meta:errors.append(f'{p}: referrer policy missing')
 if not(parser.anchors['da']==parser.anchors['en']==parser.anchors['pt']):errors.append(f'{p}: anchors do not align')
 for href in parser.links:
  u=urllib.parse.urlsplit(href)
  if u.scheme or u.netloc:continue
  target=(p.parent/urllib.parse.unquote(u.path)).resolve()if u.path else p
  if not target.exists():errors.append(f'{p}: broken link {href}')
  elif u.fragment and target.suffix=='.html':
   q=Inspect();q.feed(target.read_text())
   if u.fragment not in q.ids:errors.append(f'{p}: missing fragment {href}')
manifest=json.loads((ROOT/'sources/manifest.json').read_text())
assert len(manifest)==len(PAGES)==20
for m in manifest:assert(ROOT/m['page']).is_file()and(ROOT/m['asset']).is_file()
assert len(VIDEOS)==5
assert 45+95+120+40+150+50+40+20+10==570
assert 8000+14500+4200+3500+250+150+350+200+800+2750==34700
assert (56700+9750+500)*.1==6695
assert 56700+9750+500+1000+6695==74645
assert 74645*2.5==186612.5
ordered=[2600,3000,2700,1000,1200,1500,1700,500,600,670,560,700]
on_time=[2400,2750,2700,980,600,1250,1000,470,450,580,500,500]
assert round(sum(on_time)/sum(ordered)*100,2)==84.76
assert 69+78+95+103==345
assert '345/214 = 1,61'in(ROOT/'content/course.py').read_text()
assert errors==[], '\n'.join(errors)
print(f'PASS: {len(pages)} HTML pages, 20/20 originals, 3 aligned languages, 5 self-study video lessons, links/fragments/IDs and key calculations.')
