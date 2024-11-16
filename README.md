# Weather App GUI 🌦️

## Overview

The **Weather App** is a desktop application built using Python and the Tkinter library. The app fetches and displays the current weather and a 7-day weather forecast for a given city, along with its timezone and geographic coordinates (latitude and longitude). The app uses data from the OpenWeather API and integrates a database (MySQL) to store and update weather data.

## Features

- **Current Weather Information**: Displays temperature, humidity, pressure, wind speed, and description for the specified city.
- **7-Day Weather Forecast**: Shows the daily forecast for the upcoming 7 days, including day/night temperatures and weather icons.
- **Timezone Display**: Shows the local timezone of the city.
- **Geographic Coordinates**: Displays the latitude and longitude of the city.
- **Clock**: Shows the current local time for the selected city.
- **Database Integration**: Allows weather data to be fetched from and stored in a MySQL database.
- **Error Handling**: Provides error messages if there are issues with data fetching or database operations.

## Modules Used

- **Tkinter**: GUI library for creating the desktop application.
- **Geopy**: To fetch geographic coordinates (latitude and longitude) of the city.
- **TimezoneFinder**: To determine the timezone of the city.
- **Requests**: To fetch data from the OpenWeather API.
- **Pytz**: To handle timezone conversion.
- **MySQL Connector**: To interact with the MySQL database.
- **Pillow**: To handle image display for weather icons.

## How to get started


**Step 1:** download the zip file and extract the file in the C:/ folder after extraction you will get this folder "Weather-App"
Set Up the Database
Run the database.sql in file to create the necessary tables and database structure.

**Step 2:** open the folder and populate the database with initial data by running the insert.py script. 
before running add the host and password attribute values at line 9 and 16 of the file. also do this for the main.py file at line 267.
also ensure all the above mentioned modules are installed.

**Step 3:** Finally, launch the Weather App by running the main.py file.

  
## Functionality

- **Search City**: Users can input a city name, and the app will fetch the weather data for that city.
- **Weather Data Update**: The app updates weather data for the city in the database and displays it in the GUI.
- **Weather Forecast**: Fetches and displays a 7-day weather forecast for the specified city.
- **Database Operations**: The app allows for updating, deleting, and clearing weather data from the database.

## Database Structure

The app uses a MySQL database with the following tables:
1. **weather_db**: Stores the current weather information (temperature, humidity, pressure, wind speed, description) for each city.
2. **weather_days**: Stores the 7-day weather forecast data (day temperature, night temperature, weather icon) for each city.

  
## How to Use

1. **Input a City**: Type the name of the city into the search bar.
2. **View Current Weather**: The app will display the current weather for that city, including temperature, humidity, pressure, wind speed, and description.
3. **View 7-Day Forecast**: The app will display the forecast for the next 7 days, including temperatures and weather icons.
4. **View Timezone & Coordinates**: The app shows the local timezone and the geographic coordinates of the selected city.
5. **Manage Weather Data**: You can update, delete, or clear weather data stored in the database for a city.

## Notes

- **API Key**: An OpenWeather API key is required for fetching weather data. Replace the `api_key` variable in the code with your own valid key.
- **Database Setup**: Ensure that the MySQL database is correctly set up with the necessary tables (`weather_db` and `weather_days`) for the app to work.
- The database can set up by using the sql file.
