from pathlib import Path
import json
r=Path(__file__).resolve().parents[1]
d=json.loads((r/'data/portfolio.json').read_text())
(r/'data/portfolio.js').write_text('window.PORTFOLIO = '+json.dumps(d,ensure_ascii=False)+';\n')
geo=json.loads((r/'data/rdc-provinces.geojson').read_text())
features=[]
for f in geo['features']:
 polys=f['geometry']['coordinates']
 if f['geometry']['type']=='Polygon':polys=[polys]
 paths=[]
 for poly in polys:
  for ring in poly:
   paths.append('M'+' L'.join(f'{(p[0]-12)*33:.1f},{(6-p[1])*33:.1f}' for p in ring)+' Z')
 features.append(dict(name=f['properties']['province'],path=' '.join(paths)))
(r/'data/map.js').write_text('window.PROVINCES = '+json.dumps(features,ensure_ascii=False)+';\n')
print('Browser data synchronized')
