class UserInterface:
    def __init__(self, database, client):
        self.database = database
        self.client = client

    def get_user_input(self):
        try:
            latitude = float(input('Enter valid latitude: '))
            longitude = float(input('Enter valid longitude: '))
            return latitude, longitude
        except ValueError:
            print("Invalid value. Latitude and longitude must be numeric.")
    def display_cities(self, cities):
        if cities:
            for city in cities:
                print(f"City: {city['city']}, Country Code: {city['country_code']}")
        else:
            print("No matching cities found in the database.")