import json
with open('farger.json', 'r') as f:
    data = json.load(f)


colA = data['colA']
colB = data['colB']
rationB= data['rationB']

colA_R = colA // 1000000
colA_G = (colA // 1000) % 1000
colA_B = colA % 1000

colB_R = colB // 1000000
colB_G = (colB // 1000) % 1000
colB_B = colB % 1000


colC_R = round(colA_R * (1 - rationB) + colB_R * rationB)
colC_G = round(colA_G * (1 - rationB) + colB_G * rationB)
colC_B = round(colA_B * (1 - rationB) + colB_B * rationB)

colC = colC_R * 1000000 + colC_G * 1000 + colC_B

print(colC)
