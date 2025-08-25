
from pathlib import Path
import json

content = Path('bankdata.json').read_text(encoding='utf-8')
data = json.loads(content)

name = data['personalia']['navn']
value = data['konti'][0]['saldo']
value2 = data['konti'][1]['saldo']

sum_value = value + value2

print(f"{name} har {sum_value} kroner i innskudd")
