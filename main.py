import requests
import json
from twilio.rest import Client

api_endpoit = "https://api.openweathermap.org/data/2.5/forecast"
api_key = ""


weather_params = {
    "lat": 47.142269,
    "lon":23.875731,
    "appid": api_key,
    "cnt" : 4
}


response = requests.get(api_endpoit, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for every_hour in weather_data["list"]:
    condtion_code = every_hour["weather"][0]["id"]
    if int(condtion_code) < 700:
        will_rain = True

if will_rain:
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_='',
    body='it is going to rain today',
    to=''
    )
    print(message.sid)


