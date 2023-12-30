import requests
from constants import Settings


URL = "https://api.travelpayouts.com/aviasales/v3/prices_for_dates"

origin = "MOW"
destination = "LED"
depart_date = "2024-01-10"
return_date = ""
currency = "rub"
sorting = "price"
token = Settings.API_TOKEN

params = {
    "origin": origin,
    "destination": destination,
    "depart_date": depart_date,
    "return_date": return_date,
    "currency": currency,
    "sorting": sorting,
    "token": token,
}
headers = {
    # "User-Agent": "*",
    "Content-Type": "application/json",
    # "Accept-Encoding": "gzip, deflate",
}

response: dict = requests.get(URL, headers=headers, params=params).json()

values = response.get('data')

for _, price in enumerate(values):
    print(price['origin_airport'], price['destination_airport'], price['departure_at'], price['price'])

# print(response.get('data'))
