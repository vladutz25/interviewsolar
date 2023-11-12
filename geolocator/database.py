import os
import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self,):
        self.conn = None

    def connect(self, db_path):
        try:
            self.conn = sqlite3.connect(db_path)
            self._create_table()
        except Error as error:
            print(error)
        

    def write(self, lat, lon, city, country):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO cities (latitude, longitude, city, country_code) VALUES (?, ?, ?, ?)",
                           (lat, lon, city, country))
            self.conn.commit()
        except Error as error:
            print(error)

    def _create_table(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS cities (
    lat REAL NOT NULL,
    lon REAL NOT NULL,
    city TEXT NOT NULL,
    country_code TEXT NOT NULL
)
''')
        except Error as error:
            print(error)
    
    def search_cities(self, lat, lon):
       cursor = self.conn.cursor()
       query = "SELECT name, country_code FROM cities WHERE latitude BETWEEN ? AND ? AND longitude BETWEEN ? AND ?"
       parameters = (lat - 0.03, lat + 0.03, lon - 0.03, lon + 0.03)
       cursor.execute(query, parameters)
       result = cursor.fetchall()
       return [{"city": row[0], "country_code": row[1]} for row in result]
    
    def close_conn(self):
        if self.conn:
            self.conn.close()
            self.conn = None
