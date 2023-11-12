class UserInterface:
    def __init__(self, database, client):
        self.database = database
        self.client = client

    def get_user_input(self):
        try:
            lat = float(input('Enter valid lat: '))
            lon = float(input('Enter valid lon: '))
            return lat, lon
        except ValueError:
            print("Invalid value. lat and lon must be numeric.")
    def display_cities(self, cities):
        if cities:
            for city in cities:
                print(f"City: {city['city']}, Country Code: {city['country_code']}")
        else:
            print("No matching cities found in the database.")