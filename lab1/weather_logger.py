import requests

url = "https://api.met.no/weatherapi/nowcast/2.0/complete?lat=60.3894&lon=5.33"
response = requests.get(url, headers={"User-Agent": "no.uib.ii.inf100"})
data = response.json()

air_temp = data['properties']['timeseries'][0]['data']['instant']['details']['air_temperature']

print(air_temp)


