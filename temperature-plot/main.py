import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import numpy as np

# File name
CSV_FILE = "temperature-plot/data.csv"

def plot_temperature_variations(csv_file):
    # Read data
    data = pd.read_csv(csv_file)

    # **1. Ensure correct interpretation of the date format**
    # Convert 'date' column to datetime format
    try:
        data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d', errors='coerce')
    except Exception as e:
        print(f"Error in date conversion: {e}")
        return

    # **2. Handle missing or NaN values**
    # Drop rows where 'date' or 'temperature' is NaN
    initial_len = len(data)
    data = data.dropna(subset=['date', 'temperature'])
    final_len = len(data)

    if final_len < initial_len:
        print(f"Removed {initial_len - final_len} rows with missing or invalid data.")

    # Convert temperature to numeric in case of non-numeric values
    data['temperature'] = pd.to_numeric(data['temperature'], errors='coerce')

    # Drop rows where 'temperature' is NaN after conversion
    data = data.dropna(subset=['temperature'])

    # Identify highest and lowest temperatures
    max_temp_row = data.loc[data['temperature'].idxmax()]
    min_temp_row = data.loc[data['temperature'].idxmin()]

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(data['date'], data['temperature'], label="Temperature", color="blue", marker="o")

    # Mark the highest temperature
    plt.annotate(
        f"{max_temp_row['temperature']}°C on {max_temp_row['date'].date()}",
        xy=(max_temp_row['date'], max_temp_row['temperature']),
        xytext=(max_temp_row['date'], max_temp_row['temperature'] + 2),
        arrowprops=dict(facecolor='green', shrink=0.05),
        fontsize=10,
        color="green"
    )

    # Mark the lowest temperature
    plt.annotate(
        f"{min_temp_row['temperature']}°C on {min_temp_row['date'].date()}",
        xy=(min_temp_row['date'], min_temp_row['temperature']),
        xytext=(min_temp_row['date'], min_temp_row['temperature'] - 3),
        arrowprops=dict(facecolor='red', shrink=0.05),
        fontsize=10,
        color="red"
    )

    # **Format the x-axis for readable date labels**
    plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    plt.gcf().autofmt_xdate()

    # Labels and title
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title("Daily Temperature Variations")
    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.tight_layout()
    plt.show()

# Call the function
plot_temperature_variations(CSV_FILE)
