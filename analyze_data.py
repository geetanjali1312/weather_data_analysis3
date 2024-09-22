import sqlite3
from datetime import datetime, timedelta
def query_data(start_date, end_date):
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT AVG(temperature), AVG(humidity)
        FROM weather
        WHERE timestamp BETWEEN ? AND ?
    ''', (start_date, end_date))
    result = cursor.fetchone()
    conn.close()
    return result
if __name__ == "__main__":
    # Fetch and store data as before
    
    # Example query
    end_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    start_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
    avg_temp, avg_humidity = query_data(start_date, end_date)
    print(f'Average Temperature: {avg_temp}, Average Humidity: {avg_humidity}')
