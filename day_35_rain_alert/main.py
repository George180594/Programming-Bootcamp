import requests
api_key="96f5b9c718da8fa6f7111ecdc713a846"
OWN_Endpoit= "https://api.openweathermap.org/data/2.5/forecast"

MY_LAT=-27.142080
MY_LONG=-48.899730

weather_params = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "appid": api_key,
        "cnt":4,
    }

response = requests.get(OWN_Endpoit, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
will_rain= False
for hour_data in weather_data["list"]:
    condition_code=(hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain=True
if will_rain:
    print("Bring an Umbrella")

