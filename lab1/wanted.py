from pathlib import Path
import json

content = Path("wanted.json").read_text(encoding="UTF-8")
data = json.loads(content)

print(f"length: {data['total']}")
print(f" name: {data['items'][1]['title']}\n {data['items'][1]['description']}")
