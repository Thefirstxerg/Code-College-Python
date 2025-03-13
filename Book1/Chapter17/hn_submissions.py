from operator import itemgetter  # Importing itemgetter to help sort dictionaries by a specific key.
import requests  # Importing the requests library to make HTTP requests.

# Define the URL to fetch the list of top stories from Hacker News.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'

# Make an API call to get the top stories.
r = requests.get(url)
print(f"Status code: {r.status_code}")  # Print the HTTP response status code to check if the request was successful.

# Convert the JSON response into a Python list of story IDs.
submission_ids = r.json()

# Create an empty list to store dictionaries containing article details.
submission_dicts = []

# Loop through the first 30 story IDs (to limit the number of API calls and data processed).
for submission_id in submission_ids[:30]:
    # Construct the URL to fetch details of each story using its unique ID.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    
    # Make an API request for each individual story.
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")  # Print the status code for each request to check if it's successful.
    
    # Convert the JSON response into a Python dictionary.
    response_dict = r.json()
    
    # Create a dictionary to store relevant details about each submission.
    submission_dict = {
        'title': response_dict['title'],  # Extract the title of the submission.
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",  # Construct the Hacker News discussion link.
        'comments': response_dict.get('descendants', 0),  # Get the number of comments (default to 0 if missing).
    }
    
    # Add the submission dictionary to the list.
    submission_dicts.append(submission_dict)

# Sort the list of dictionaries by the number of comments in descending order.
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Loop through each sorted submission and print the details.
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")  # Print the title of the article.
    print(f"Discussion link: {submission_dict['hn_link']}")  # Print the Hacker News discussion link.
    print(f"Comments: {submission_dict['comments']}")  # Print the number of comments.