import requests
from pathlib import Path
import json

# Hent en tilfeldig vits
resp = requests.get('https://official-joke-api.appspot.com/random_joke')
data = resp.json()

# Skriv ut intro og vitsens setup
print("Her kommer en tilfeldig vits!")
setup = data['setup']
print(setup)

input("Trykk enter for svaret...")

# Skriv ut punchline
punchline = data['punchline']
print(punchline)

# Spør brukeren om vurdering
rating = input("Hva synes du om vitsen? Skriv latteren din: ")  # f. eks. hahaha
laughter = len(rating)
print("Du syns vitsen var", laughter, "/ 10")

# TODO: Lagre vitsen i en JSON-fil
save_filename = "joke.json"

data = {
    "setup": setup,
    "punchline": punchline,
    "rating": laughter
}
with open (save_filename, "w") as f:
    json.dump(data, f, indent=4)