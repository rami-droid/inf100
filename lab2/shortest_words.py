import json

with open("shortest_words.json", "r") as f:
    data = json.load(f)

words = data["words"]

shortest = None

min_len = min(len(word) for word in words)

for word in words:
    if len(word) == min_len:
        print(word)