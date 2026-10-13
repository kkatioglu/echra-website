from pathlib import Path
from html.parser import HTMLParser
import hashlib
class Links(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.buttons=[]
 def handle_starttag(self,tag,attrs):
  attr=dict(attrs)
  if tag=='a':self.links.append(attr.get('href',''))
  if tag=='div' and 'store-badge' in attr.get('class',''):self.buttons.append(attr)
page=Path('index.html').read_text()
p=Links();p.feed(page)
assert len(p.buttons)==2
assert len(p.links)==6
assert all(k.startswith('/') and Path(k.lstrip('/')).is_file() for k in p.links)
assert 'Are you available?' in page
assert 'echra-logo.png' in page and 'approved-logo' in page
assert 'href="#"' not in page and 'PRIVATE PILOT' not in page
assert 'echra-logo.png' in Path('Dockerfile').read_text()
assert 'hero.css' in Path('Dockerfile').read_text()
assert not any(x in page.lower() for x in ['planet','sci-fi','moon','satellite'])
for x in ['terms','privacy','cookies','kvkk','delete-account','support']:
 assert (Path(x+'.html').read_text().count('<h2>')>=2)
print('STATIC ASSERTIONS PASS; original logo SHA256:',hashlib.sha256(Path('echra-logo.png').read_bytes()).hexdigest())
