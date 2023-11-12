import requests


class Client:
    def __init__(self, api_key):
        self._api_key = api_key
        self.base_url = "http://api.openweathermap.org/geo/1.0/direct"

    def get(self, latitude, longitude):
        try:
            params = {
                'q': f"{city_name}, {country_code}",
                'limit': 10,
                'appid': self._api_key
            }
            response = requests.get(self.base_url, params=params)
            if response.status_code = 200:
                data = response.json()
                return data
            else:
                print("API request failed")
                return None
        except requests.Request Exception as e:
            print("Request failed: ", e)
            return None
