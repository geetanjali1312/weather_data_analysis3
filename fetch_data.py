import requests
import time
import sqlite3
from database import setup_database

API_KEY = '63f524001711740e474f963bf0e998df'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def fetch_weather_data(location):
    params = {
        'q': location,
        'appid': API_KEY,
        'units': 'metric'  # Get temperature in Celsius
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data

if __name__ == "__main__":
    location = 'solapur'
    while True:
        weather_data = fetch_weather_data(location)
        print(weather_data)  # For debugging
        time.sleep(5)  # Fetch every minutes

def insert_weather_data(location, temperature, humidity, wind_speed):
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO weather (location, temperature, humidity, wind_speed)
        VALUES (?, ?, ?, ?)
    ''', (location, temperature, humidity, wind_speed))
    conn.commit()
    conn.close()

# Update the fetch loop
if __name__ == "__main__":
    setup_database()  # Set up the database once
    location = 'solapur'
    while True:
        weather_data = fetch_weather_data(location)
        if 'main' in weather_data:
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']
            insert_weather_data(location, temperature, humidity, wind_speed)
        time.sleep(5)

