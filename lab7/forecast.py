import requests, json
URL = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=60.3913&lon=5.3221"

def weather_in_bergen_next_hour():
    res = requests.get(URL)
    data = res.json()
    symbol_code = data["properties"]["timeseries"][0]["data"]["next_1_hours"]["summary"]["symbol_code"]
    return symbol_code

print(weather_in_bergen_next_hour())

