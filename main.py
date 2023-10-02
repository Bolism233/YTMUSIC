import requests, json, pylast, re
from collections import defaultdict
from credentials import api_key, api_lastfm, api_secret

### Obtain User Playlist via link
""" playlist_link = input("Enter your playlist link: ") """
playlist_link = "https://youtube.com/playlist?list=PLTOXykx0lDH5nrxwnRBgH4d1ZbiBMUTPg&si=G9dV9bCgfphEYufK"
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
url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={playlist_id}&key={api_key}&maxResults=50"
response = requests.get(url)
data = response.json()
videos = data.get("items", [])
song_info = defaultdict(list)

for video in videos:
    snippet = video.get("snippet", {})
    video_title = snippet.get("title", "No Title")
    video_description = snippet.get("description", "No Description")
    video_id = video["snippet"]["resourceId"]["videoId"]

    """ print(f"Video Title: {video_title}") """
    parts = video_title.split(" - ")
    if len(parts) >= 2:
        artist_name = parts[0]
        song_name = parts[1]

        # Use re.sub to remove the matched text
        pattern = r'\[.*?\]|\(.*?\)'
        song_name = re.sub(pattern, '', song_name)

        ### store song into song_info
        song_info[artist_name].append(song_name)
        
    else:
        print("Title format not recognized.")


for artist_name, song_name in song_info.items():
    print(f"Artist Name: {artist_name}")
    print(f"Song Name: {song_name}")

for artist_name, song_name in song_info.items():
    if((len(song_name) > 1) and artist_name == "Ed Sheeran"):
        for song in song_name:
            print(f"Artist Name: {artist_name}, Song List: {song}")
            url = f'http://ws.audioscrobbler.com/2.0/?method=track.search&track={song}&artist={artist_name}&api_key={api_lastfm}&format=json'
            # Make the GET request
            response = requests.get(url)
            # Parse the JSON response
            data = response.json()
            # Extract information from the response
            try:
                if 'trackmatches' in data['results'] and 'track' in data['results']['trackmatches']:
                    # Get the first matching track
                    track = data['results']['trackmatches']['track'][0]
                    print(f"Track: {track['name']} by {track['artist']}")
                else:
                    print("Track not found.")
            except:
                print("not working")
    
    else:
        url = f'http://ws.audioscrobbler.com/2.0/?method=track.search&track={song_name}&artist={artist_name}&api_key={api_lastfm}&format=json'
        # Make the GET request
        response = requests.get(url)
        # Parse the JSON response
        data = response.json()
        # Extract information from the response
        try:
            if 'trackmatches' in data['results'] and 'track' in data['results']['trackmatches']:
                # Get the first matching track
                track = data['results']['trackmatches']['track'][0]
                print(f"Track: {track['name']} by {track['artist']}")
            else:
                print("Track not found.")
        except:
            print("not working")