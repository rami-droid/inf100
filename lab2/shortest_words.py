import json

with open("shortest_words.json", "r") as f:
    data = json.load(f)

words = data["words"]

shortest = None

for word in words:
    if shortest is None or len(word) < len(shortest):
        shortest = word
    elif len(word) == len(shortest):
        shortest += ", " + word

print(shortest)

