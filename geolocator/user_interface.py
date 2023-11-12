class UserInterface:
    def __init__(self, database, client):
        self.database = database
        self.client = client

    def get_user_input(self):
        try:
            langitude = float(input('Enter valid latitude'))
            longitude = float(input('Enter valid longitude'))
            return latitude, longitude
        except ValueError:
            print("Invalid value. Latitude and longitude must be numeric.")
