import mysql.connector
import requests
from datetime import datetime
from geopy.geocoders import Nominatim
import time

def init_db():
    conn = mysql.connector.connect(
        host='localhost', username='root', password='',
        database='weather_db'
    )
    return conn

def init_dbs():
    conn = mysql.connector.connect(
        host='localhost', username='root', password='',
        database='weather_db'
    )
    return conn




def store_weather_data_dbs(city, weather_data):
    connector = init_dbs()
    cursor = connector.cursor()
    query = '''INSERT INTO weather_db (city, temp, humidity, pressure, wind_speed, description)
        VALUES (%s, %s, %s, %s, %s, %s)'''
    cursor.execute(query, (city, weather_data['temp'], weather_data['humidity'],
                           weather_data['pressure'], weather_data['wind_speed'], weather_data['description']))
    connector.commit()
    connector.close()

  

def store_weather_data_days(city, weather_data):
    conn = init_db()
    cursor = conn.cursor()
    query = '''INSERT INTO weather_days (city, temp_day, temp_night, humidity, pressure, wind_speed, description, icon, date_time)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    for day_data in weather_data:
        cursor.execute(query, (city, day_data['temp_day'], day_data['temp_night'], day_data['humidity'],
                               day_data['pressure'], day_data['wind_speed'], day_data['description'], day_data['icon'], datetime.now()))
    conn.commit()
    conn.close()
    

def fetch_weather_data(city):
    try:
        geolocator = Nominatim(user_agent="Weather App")
        location = geolocator.geocode(city)
        
        api_key = '34579d925f013e6b7cd03e2cbbd78bbb'  # Replace with your OpenWeather API key
        api_url = f"https://api.openweathermap.org/data/2.5/onecall?lat={location.latitude}&lon={location.longitude}&units=metric&exclude=hourly&appid={api_key}"

        response = requests.get(api_url)
        json_data = response.json()
        
        current_weather = json_data.get('current', {})
        
        # Check if 'wind_speed' key exists in the current weather data
        if 'wind_speed' not in current_weather:
            print(f"Error: 'wind_speed' data not available for {city}")
            return
        
        weather_data = {
            'temp': current_weather.get('temp'),
            'humidity': current_weather.get('humidity'),
            'pressure': current_weather.get('pressure'),
            'wind_speed': current_weather.get('wind_speed'),
            'description': current_weather.get('weather', [{}])[0].get('description'),
            'icon': current_weather.get('weather', [{}])[0].get('icon')  # Extract 'icon' field
        }

        # Store current weather data in weather_db table
        store_weather_data_dbs(city, weather_data)
        
        # Store daily weather data in weather_days table
        daily_weather_data = []
        for day in json_data['daily']:
            day_data = {
                'temp_day': day['temp']['day'],
                'temp_night': day['temp']['night'],
                'humidity': day['humidity'],
                'pressure': day['pressure'],
                'wind_speed': day.get('wind_speed', 'N/A'),  # Handle missing 'wind_speed'
                'description': day['weather'][0]['description'],
                'icon': day['weather'][0]['icon']  # Added the icon key
            }
            daily_weather_data.append(day_data)
        
        store_weather_data_days(city, daily_weather_data)
        
        # Fetch data from weather_days table
        conn_days = init_db()
        cursor_days = conn_days.cursor()
        cursor_days.execute("SELECT * FROM weather_days WHERE city = %s", (city,))
        weather_data_days = cursor_days.fetchall()
        conn_days.close()
        
        # Fetch data from weather_db table
        conn_db = init_dbs()
        cursor_db = conn_db.cursor()
        cursor_db.execute("SELECT * FROM weather_db WHERE city = %s", (city,))
        weather_data_db = cursor_db.fetchall()
        conn_db.close()
        
        return weather_data_days, weather_data_db
        
    except Exception as e:
        print(f"Error fetching data for {city}: {e}")

def print_weather_data():
    conn = init_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM weather_days")
    rows = cursor.fetchall()
    print("Weather data from weather_days table:")
    for row in rows:
        print(row)
    conn.close()

    conn = init_dbs()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM weather_db")
    rows = cursor.fetchall()
    print("Weather data from weather_db table:")
    for row in rows:
        print(row)
    conn.close()


# List of cities to fetch weather data for
#cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix','Islamabad','Mexico','Rawalpindi','Lahore']
cities = ['Grasberg','oyu tolgoi','Virginia city','Centralia','Cerro de San Pedro','Bodie','Nevada gold mine']
# Fetch and store weather data for each city
for city in cities:
    fetch_weather_data(city)
    time.sleep(1)  # Add a delay to avoid hitting the rate limit

# Print weather data from the database
print_weather_data()