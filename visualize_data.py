import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

def visualize_data():
    conn = sqlite3.connect('weather_data.db')
    df = pd.read_sql_query('SELECT * FROM weather', conn)
    conn.close()

    # Convert timestamp to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    plt.figure(figsize=(14, 7))

    plt.subplot(2, 1, 1)
    plt.plot(df['timestamp'], df['temperature'], label='Temperature', color='red')
    plt.title('Temperature over Time')
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(df['timestamp'], df['humidity'], label='Humidity', color='blue')
    plt.title('Humidity over Time')
    plt.xlabel('Time')
    plt.ylabel('Humidity (%)')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Call the visualization function
visualize_data()
