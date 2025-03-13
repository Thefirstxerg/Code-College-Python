import requests  # Import the requests module to make HTTP requests
import json  # Import the JSON module to work with JSON data

# Define the URL for the API call (Hacker News item endpoint)
url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"

# Make an HTTP GET request to the API and store the response
r = requests.get(url)

# Print the status code of the response (200 means successful)
print(f"Status code: {r.status_code}")

# Convert the response JSON content into a Python dictionary
response_dict = r.json()

# Format the JSON dictionary as a nicely indented string
response_string = json.dumps(response_dict, indent=4)

# Print the formatted JSON response to explore its structure
print(response_string)
