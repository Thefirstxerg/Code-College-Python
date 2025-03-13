from pathlib import Path  # Import Path to handle file paths
import json  # Import JSON module to work with JSON data

import plotly.express as px  # Import Plotly Express for visualization

# Define the path to the earthquake data file
path = Path('eq_data/eq_data_30_day_m1.geojson')

# Read the file contents as a string using UTF-8 encoding
contents = path.read_text(encoding='utf-8')

# Convert the JSON string into a Python dictionary
all_eq_data = json.loads(contents)

# Extract the list of earthquakes from the dataset
all_eq_dicts = all_eq_data['features']

# Initialize empty lists to store earthquake magnitudes, longitudes, latitudes, and titles
mags, lons, lats, eq_titles = [], [], [], []

# Loop through each earthquake dictionary in the dataset
for eq_dict in all_eq_dicts:
    # Extract the earthquake magnitude
    mag = eq_dict['properties']['mag']
    
    # Extract the longitude and latitude from the coordinates list
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    
    # Extract the earthquake title (description)
    eq_title = eq_dict['properties']['title']
    
    # Append extracted values to their respective lists
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)

# Define the title for the visualization
title = 'Global Earthquakes'

# Create a scatter plot on a world map using Plotly Express
fig = px.scatter_geo(
        lat=lats,  # Use latitude values for positioning
        lon=lons,  # Use longitude values for positioning
        size=mags,  # Set the size of points based on earthquake magnitude
        title=title,  # Set the title of the plot
        color=mags,  # Color points based on their magnitude
        color_continuous_scale='Viridis',  # Use the Viridis color scale
        labels={'color':'Magnitude'},  # Label for the color bar
        projection='natural earth',  # Use the 'natural earth' map projection
        hover_name=eq_titles,  # Show earthquake titles on hover
    )

# Display the plot
fig.show()
