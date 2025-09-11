import json

with open("longest_word.json", "r", encoding="utf-8") as f:
    data = json.load(f)

words = data["words"]

longest = None

for word in words:
    if longest is None or len(word) > len(longest):
        longest = word

print(longest)
