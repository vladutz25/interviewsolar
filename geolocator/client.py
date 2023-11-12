import requests
import os


class Client:
    def __init__(self, api_key):
        self._api_key = api_key
        self.base_url = "http://api.openweathermap.org/geo/1.0/reverse"

    def get(self, lat, lon):
        try:
            params = {
                'lat': lat,
                'lon': lon,
                'limit': 10,
                'appid': self._api_key
            }
            response = requests.get(self.base_url, params=params)
            if response.status_code == 200:
                data = response.json()
                return [{"name": row["name"], "country_code": row["country"]} for row in data]
            else:
                print("API request failed")
                return None
        except Exception as e:
            print("Request failed: ", e)
            return None
