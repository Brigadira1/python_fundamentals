import requests

MY_LAT = 42.6605234
MY_LON = 23.2888404
API_KEY = "659171337177595d96e17fdf29493918"

params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
}

data = requests.get("https://api.openweathermap.org/data/3.0/onecall", params=params)
data.raise_for_status()

response = data.json()

