import os
import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self,):
        self.connection = None

    def connect(self, db_path):
        try:
            self.connection = sqlite3.connect(db_path)
            self._create_table()
        except Error as error:
            print(error)
        

    def write(self, latitude, longitude, city, country):
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO geolocation (latitude, longitude, city, country_code) VALUES (?, ?, ?, ?)",
                           (latitude, longitude, city, country))
            self.connection.commit()
        except Error as error:
            print(error)

    def _create_table(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS geolocation (
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    city TEXT NOT NULL,
    country_code TEXT NOT NULL
)
''')
        except Error as error:
            print(error)
    
    def search_cities(self, latitude, longitude):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM geolocation WHERE latitude=? AND longitude=?", (latitude, longitude))
            rows = cursor.fetchall()
            return rows  
        except Error as error:
            print(error)
    
    def close_connection(self):
        if self.connection:
            self.connection.close()
