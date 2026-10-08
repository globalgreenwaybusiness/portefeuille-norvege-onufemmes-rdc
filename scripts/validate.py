"""Validate public portfolio data and local assets, without network dependencies."""
from pathlib import Path
from html.parser import HTMLParser
from decimal import Decimal
import json,re
root=Path(__file__).resolve().parents[1]
d=json.loads((root/'data/portfolio.json').read_text())
assert len(d['agreements'])==22
assert len({a['id'] for a in d['agreements']})==22
assert len(d['partners'])==len({p['id'] for p in d['partners']})
for a in d['agreements']:
 assert a['partner'] in {p['id'] for p in d['partners']}
 assert a['start']<=a['end']
 assert a['currency']=='USD'
assert sum(Decimal(str(a['value'])) for a in d['agreements'] if not a['multi'])==Decimal('787262')
assert sum(Decimal(str(a['value'])) for a in d['agreements'] if a['multi'])==Decimal('1761279.74')
assert len([a for a in d['agreements'] if a['multi']])==7
for r in d['results']:assert r['source'] in {s['id'] for s in d['sources']}
assert json.loads((root/'data/portfolio.js').read_text().removeprefix('window.PORTFOLIO = ').strip().removesuffix(';'))==d
class Check(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.refs=[];self.links=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='img':assert a.get('alt'),a
  for k in ['src','href']:
   if k in a:self.links.append(a[k])
  if 'for' in a:self.refs.append(a['for'])
c=Check();c.feed((root/'index.html').read_text())
assert len(c.ids)==len(set(c.ids)),'Duplicate HTML id'
for s in c.refs:assert s in c.ids,s
for s in c.links:
 if s.startswith('#'):assert s[1:] in c.ids,s
 elif not re.match(r'^(https?:|data:|mailto:)',s):assert (root/s).is_file(),s
assert len(json.loads((root/'data/rdc-provinces.geojson').read_text())['features'])==26
allowed_agreement_fields={'id','partner','title','start','end','value','currency','multi','phase','source'}
for a in d['agreements']:
 assert set(a)==allowed_agreement_fields, 'Unexpected non-public field'
print('PASS: 22 agreements, funding attribution, sources, data parity, local assets, anchors, map and public data fields')
