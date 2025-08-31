import json
import math
import pathlib as Path

with open ("points.json", "r") as f:
    data = json.load(f)

feat1 = data['features'][0]['geometry']['coordinates']
feat2 = data['features'][1]['geometry']['coordinates']

def haversine(lon1, lat1, lon2, lat2):
    return 2 * 6371000 * math.asin(math.sqrt((math.sin((math.radians(lat2) - math.radians(lat1)) / 2)) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * (math.sin((math.radians(lon2) - math.radians(lon1)) / 2)) ** 2))

print(haversine(feat1[0], feat1[1], feat2[0], feat2[1]))