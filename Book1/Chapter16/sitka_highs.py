from pathlib import Path  # Import the Path class to handle file paths
import csv  # Import the CSV module to read CSV files
from datetime import datetime  # Import datetime to work with date formatting

import matplotlib.pyplot as plt  # Import the matplotlib library for data visualization

# Define the path to the CSV file containing weather data
path = Path('weather_data/sitka_weather_07-2021_simple.csv')

# Read the file and split it into lines
lines = path.read_text().splitlines()

# Create a CSV reader object to parse the file content
reader = csv.reader(lines)

# Read the first line from the file, which contains the column headers
header_row = next(reader)

# Initialize empty lists to store dates and high temperatures
dates, highs = [], []

# Loop through the remaining rows in the CSV file
for row in reader:
    # Convert the date string from the CSV into a datetime object
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    
    # Convert the high temperature from a string to an integer
    high = int(row[4])
    
    # Append the date and high temperature to the respective lists
    dates.append(current_date)
    highs.append(high)

# Print the list of high temperatures to check the extracted values
print(highs)

# Create a plot using the 'seaborn' style for better visuals
plt.style.use('seaborn-v0_8')

# Create a figure and an axis object for the plot
fig, ax = plt.subplots()

# Plot the high temperatures as a red line
ax.plot(dates, highs, color='red')

# Set the title of the graph with a larger font size
ax.set_title("Daily High Temperatures, 2021", fontsize=24)

# Label the x-axis (empty label but formatted)
ax.set_xlabel('', fontsize=16)

# Auto format the dates on the x-axis for better readability
fig.autofmt_xdate()

# Label the y-axis
ax.set_ylabel("Temperature (F)", fontsize=16)

# Adjust the size of tick labels on both axes
ax.tick_params(labelsize=16)

# Display the plot
plt.show()