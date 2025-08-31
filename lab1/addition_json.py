import json

with open("addisjon.json", "r") as file:
    data = json.loads(file.read())

num1 = data["tall1"]
num2 = data["tall2"]
sum = int(num1) + int(num2)
print(f"Summen av tallene er {sum}")

