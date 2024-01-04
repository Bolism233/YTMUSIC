import requests, json, pylast, re
from search import search
from mongo import *
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
pl_url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={playlist_id}&key={api_key}&maxResults=20"
response = requests.get(pl_url)
data = response.json()
videos = data.get("items", [])
song_info = defaultdict(list)

for video in videos:
    snippet = video.get("snippet", {})
    video_title = snippet.get("title", "No Title")
    video_description = snippet.get("description", "No Description")
    video_id = video["snippet"]["resourceId"]["videoId"]
    # delete_all()
    # print(f"Video Title: {video_title}")
    parts = video_title.split(" - ")
    if len(parts) >= 2:
        artist_name = parts[0]
        song_name = parts[1]
        page_number = 1
        print(artist_name)
        # Store top tracks of that singer to database
        track_info, tracks = get_all_tracks(artist_name, 1)
        total_pages = int(track_info['toptracks']['@attr']['totalPages']) # number of total pages
        # do the 1st page
        if 'toptracks' in track_info and 'track' in track_info['toptracks']:
            tracks = [track['name'] for track in track_info['toptracks']['track']]
            for track in tracks:
                insert_data(artist_name, track)
            else:
                print('No tracks found.')

        for x in range(2, total_pages+1):
            # x is the current page number
            track_info, tracks = get_all_tracks(artist_name, x)
            if 'toptracks' in track_info and 'track' in track_info['toptracks']:
                tracks = [track['name'] for track in track_info['toptracks']['track']]
                for track in tracks:
                    insert_data(artist_name, track)
                else:
                    print('No tracks found.')

        # Use re.sub to remove the matched text
        pattern = r'\[.*?\]|\(.*?\)'
        song_name = re.sub(pattern, '', song_name)

        ### store song into song_info
        song_info[artist_name].append(song_name)
        
    """ else:
        print("Title format not recognized.") """
        

#Obtain track info in lastfm
similar_songs = defaultdict(list) # storing similar songs info

# search(song_info)

