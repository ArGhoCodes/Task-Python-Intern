# Visualizing Temperature Data with Matplotlib

## Overview

This project demonstrates how to visualize daily temperature variations over time using a line plot. The temperature data is read from a CSV file and plotted using `matplotlib`, with annotations to mark the highest and lowest temperatures.

---

## Features

- **Line Plot**: Visualizes temperature changes over time, showing daily temperature variations.
- **Annotations**: Marks the highest and lowest temperatures on the plot with labels.
- **Date Handling**: Correctly interprets the date format for the x-axis in the plot.

---

## Prerequisites

1. **Python**: Ensure Python 3.8 or higher is installed.
2. **Dependencies**: Install the required Python libraries using the following command:
   ```bash
   pip install matplotlib pandas
   ```

### Sample CSV Data

The CSV file containing the temperature data should be structured as follows:

```
csv

date,temperature
2024-10-01,22
2024-10-02,21
2024-10-03,23
2024-10-04,19
2024-10-05,25
2024-10-06,18
```

### Script Usage

Download the CSV file containing the temperature data.

Run the script to generate the line plot.

Running the Script

Save the script as temperature_plot.py and run the following command in your terminal:

```
python temperature_plot.py

```

### Code Explanation

1. Reading the Data:
   The script uses pandas to read the CSV file and loads the temperature data into a DataFrame.
   It ensures that the date column is correctly parsed as a date using pandas.to_datetime().

2. Plotting the Data:
   The script uses matplotlib to generate a line plot where the x-axis represents the dates and the y-axis represents the temperature values.
   It ensures that the dates are correctly formatted on the x-axis for proper readability.
3. Annotations:
   The script identifies the highest and lowest temperature points and annotates them on the plot with the respective dates.

### Handling Missing or NaN Values

If the dataset contains missing or NaN values in the temperature column, they can be handled in the following ways:

Remove Rows with Missing Data: You can remove rows with missing data using:

```
data = data.dropna(subset=['temperature'])

```

Fill Missing Data: If you prefer to fill missing values, you can use the fillna() method:

```
data['temperature'] = data['temperature'].fillna(method='ffill')

```

### Expected Output

The output will be a line plot showing the temperature variations over time. The plot will also contain annotations for the highest and lowest temperatures:

Line Plot: Displays temperature changes over the specified dates.

Annotations: Marks the highest and lowest temperatures with arrows and text annotations.

### License

This project is licensed under the MIT License.
