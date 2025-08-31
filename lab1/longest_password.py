
from pathlib import Path
import json

content = Path('passwords.json').read_text(encoding='utf-8')
data = json.loads(content)

people = data['people']

longest = ""

for i in people:
    curr = i['password']
    if len(curr) > len(longest):
        longest = curr

print(len(longest))
