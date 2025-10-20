from pathlib import Path

def snippet_1():
    print(f"current working dir: {Path.cwd()}") # ~/uib/inf100/lab6/pres3/snippets.py

    print(f"Home: {Path.home()}") # /home/rami

def snippet_2(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)

# Navn,Alder,Land
# Ola,17,Norge
# Kari,16,Sverige
