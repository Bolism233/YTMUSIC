import requests
from credentials import api_key

# Define your API key and the username of the random user you want to search for
username = '歪歪在吗Y'

# Make the API request to search for the user's playlists
url = f'https://www.googleapis.com/youtube/v3/search?q={username}&type=playlist&part=id&key={api_key}'
response = requests.get(url)
response2 = requests.get(url2)
# Parse the JSON response
data = response.json()

# Loop through the search results and print playlist IDs
for item in data['items']:
    if item['id']['kind'] == 'youtube#playlist':
        print(item['id']['playlistId'])

print(response2)



