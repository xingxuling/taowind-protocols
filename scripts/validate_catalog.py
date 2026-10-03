#!/usr/bin/env python3
"""Validate the documentation catalog only; no network and no runtime tests."""
import json, pathlib, re
root=pathlib.Path(__file__).resolve().parents[1]
def read(name): return json.loads((root/'registry'/name).read_text())
d=read('domains.json'); p=read('protocols.json'); s=read('sources.json'); i=read('implementations.json')
assert [x['id'] for x in d['domains']]==[f'P{n:02d}' for n in range(16)]
assert sum(x['roadmapStatus']=='partial' for x in d['domains'])==14
assert [x['id'] for x in d['domains'] if x['roadmapStatus']=='not_implemented']==['P12','P14']
assert d['normativePromotion'] is False
assert len(p['protocols'])==6 and len({x['id'] for x in p['protocols']})==6
assert {x['id'] for x in i['entries']}=={'OPP','TINP'}
ids={x['id'] for x in s['sources']}
for x in d['domains']:
 assert x['statusSource'] in ids
 assert (root/'domains'/f"{x['id']}.md").is_file()
for x in s['sources']:
 assert re.fullmatch('[0-9a-f]{40}',x['commit'])
 assert re.fullmatch('[0-9a-f]{40}',x['gitBlobSha'])
 assert x['commit'] in x['url']
count=0
for f in root.rglob('*.md'):
 for target in re.findall(r'\]\(([^)]+)\)',f.read_text()):
  if '://' in target or target.startswith('#'):continue
  assert (f.parent/target.split('#')[0]).exists(),(f,target)
  count+=1
print(f'PASS: 16 domains; 6 protocols; 2 implementations; {len(ids)} locked sources; {count} local links')
print('Scope: catalog structure only. Protocol runtime tests and live external URL checks were not run.')
