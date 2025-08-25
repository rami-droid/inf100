
from pathlib import Path
import json

content = Path('bankdata.json').read_text(encoding='utf-8')
data = json.loads(content)

name = data['personalia']['navn']
value = data['konti'][0]['saldo']

print(f"{name} har {value} kroner i innskudd")
