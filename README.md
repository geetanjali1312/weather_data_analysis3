# weather_data_analysis

Title : Weather Data Aggregator and Analyzer

Git Repository: https://github.com/geetanjali1312/weather_data_analysis.git 
Requirements:
Python 3.x
API Key from a weather data provider (e.g., OpenWeatherMap)
Libraries Used:
requests, sqlite3, matplotlib, pandas

Scripts Description: 
There are 4 scripts used in the project
1.	database.py:  this script creates the database weather_data.db and table ‘weather’ using sqllite3 repo
2.	fetch_data.py : This script pulls the data (location, temperature, humidity and wind speed) from http://api.openweathermap.org and stores into database on regular time interval (60 seconds)
3.	analyze_data.py : The script analyzes the fetched metric data and calculates the average.
4.	visualize_data.py : This script shows the analyzed data into visual format using matplotlib library.

Run the Application:
1.	Run database.py, this will create weather_data.db file in the current folder where the python scripts are stored.
2.	Register for an API key from OpenWeatherMap, copy your api key in fetch_data.py. Run fetch_data.py – this stores the weather data into ‘weather’ table of ‘weather_data.db’ on regular time interval 
3.	Run analyze_data.py – this calculates the average of all the data present in database table from start time to end time.
4.	Finally, run the visualize_data.py to get the plot.
