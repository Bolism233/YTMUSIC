import requests
import json
from credentials import api_key

### Obtain User Playlist
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

""" for video in videos:
    snippet = video.get("snippet", {})
    video_title = snippet.get("title", "No Title")
    video_description = snippet.get("description", "No Description")
    video_id = video["snippet"]["resourceId"]["videoId"]

    print(f"Video Title: {video_title}")
    print(f"Video ID: {video_id}")
    print("\n") """

if "items" in data:
    video_info = data["items"][0]["snippet"] ### 0 is the video order
    video_title = video_info["title"]
    
    # Split the video title based on common patterns (e.g., " - " for song name and artist name)
    parts = video_title.split(" - ")
    
    if len(parts) >= 2:
        artist_name = parts[0]
        song_name = parts[1]
        
        print(f"Artist Name: {artist_name}")
        print(f"Song Name: {song_name}")
    else:
        print("Title format not recognized.")
else:
    print("Video not found or API key is invalid.")


""" # Serializing json
json_object = json.dumps(videos, indent=4)
 
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
 """

print(video_title)
# Now, you can work with the 'data' variable to access the video information within the playlist.
