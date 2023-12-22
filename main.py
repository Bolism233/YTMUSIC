import requests, json, pylast, re
from search import search
from collections import defaultdict
from credentials import api_key, api_lastfm, api_secret

### Obtain User Playlist via link
""" playlist_link = input("Enter your playlist link: ") """
playlist_link = "https://youtube.com/playlist?list=PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj&si=aoAUKa4pzPtanlDT"
parts = playlist_link.split("list=")

# Check if "list=" is found in the URL
if len(parts) == 2:
    playlist_id = parts[1]
    # Remove any additional parameters
    playlist_id = playlist_id.split("&")[0]

    # Now, playlist_id contains what comes after "list="
    print("Playlist ID:", playlist_id)
else:
    print("Invalid playlist link.")

### Obtain PlayList information via API
url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={playlist_id}&key={api_key}&maxResults=20"
response = requests.get(url)
data = response.json()
videos = data.get("items", [])
song_info = defaultdict(list)

for video in videos:
    snippet = video.get("snippet", {})
    video_title = snippet.get("title", "No Title")
    video_description = snippet.get("description", "No Description")
    video_id = video["snippet"]["resourceId"]["videoId"]

    # print(f"Video Title: {video_title}")
    parts = video_title.split(" - ")
    if len(parts) >= 2:
        artist_name = parts[0]
        song_name = parts[1]

        # Use re.sub to remove the matched text
        pattern = r'\[.*?\]|\(.*?\)'
        song_name = re.sub(pattern, '', song_name)

        ### store song into song_info
        song_info[artist_name].append(song_name)
        
    """ else:
        print("Title format not recognized.") """
        

#Obtain track info in lastfm
similar_songs = defaultdict(list) # storing similar songs info

search(song_info)

""" for artist_name, song_names in song_info.items():
    for song_name in song_names:
        if len(song_name) > 1:
            artist_name, song_name = search_track(artist_name, song_name)
        else:
            artist_name, song_name = search_track(artist_name, song_names) """
