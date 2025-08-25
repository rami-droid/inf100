import json

try:
    with open("data.json", "r") as file:
        data = json.loads(file.read())
        num1 = data["num1"]
        num2 = data["num2"]
        sum = int(num1) + int(num2)
        print(sum)
except Exception as e:
    print(e)
    raise
