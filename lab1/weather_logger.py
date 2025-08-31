import requests
import json
import pathlib as Path

with open ("weather_log.json", "r") as f:
    weatherData = json.load(f)

url = "https://api.met.no/weatherapi/nowcast/2.0/complete?lat=60.3894&lon=5.33"
response = requests.get(url, headers={"User-Agent": "no.uib.ii.inf100"})
data = response.json()

air_temp = data['properties']['timeseries'][0]['data']['instant']['details']['air_temperature']
air_time = data['properties']['timeseries'][0]['time']

print(air_temp)
print(air_time)

data = {
    "time": air_time,
    "air_temp": air_temp
}
weatherData.append(data)

with open ("weather_log.json", "w") as f:
    json.dump(weatherData, f, indent=4)