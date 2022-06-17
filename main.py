# https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={API key}
import requests
import json
# import pprint

MEM_LAT = 35.143379
MEM_LONG = -90.052139
KC_LAT = 39.112700
KC_LONG = -94.626800
API_KEY = ""
CURRENT_WEATHER_FILE = "weather.json"
api_endpoint = f"https://api.openweathermap.org/data/2.5/onecall"
weather_params = {
    "lat": MEM_LAT,
    "lon": MEM_LONG,
    "exclude": "current,minutely,daily",
    "appid": API_KEY,
}
# print(api_endpoint)
response = requests.get(url=api_endpoint, params=weather_params)
response.raise_for_status()
data = response.json()

# pprint.pprint(data)

with open(CURRENT_WEATHER_FILE, 'w') as data_file:
    json.dump(data, data_file, indent=4)

hourly = data["hourly"][:12]
for hour in hourly:
    weather = hour["weather"]
    condition_code = weather[0]["id"]
    if int(condition_code) < 700:
        print("Bring an umbrella!")
        break

