import requests
import json
import pylast
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
song_info = {}

for video in videos:
    snippet = video.get("snippet", {})
    video_title = snippet.get("title", "No Title")
    video_description = snippet.get("description", "No Description")
    video_id = video["snippet"]["resourceId"]["videoId"]

    print(f"Video Title: {video_title}")
    """ print(f"Video ID: {video_id}") """
    parts = video_title.split(" - ")
    if len(parts) >= 2:
        artist_name = parts[0]
        song_name = parts[1]
        print(f"Artist Name: {artist_name}")
        print(f"Song Name: {song_name}")

        ### store song into song_info
        song_info.update({song_name: artist_name})
        
    else:
        print("Title format not recognized.")
    print("\n")

""" print("Song Info: \n")
for key,value, in song_info.items():
    print(f"{key}, {value}") """

network = pylast.LastFMNetwork(api_key=api_lastfm, api_secret=api_secret)

# Replace with the artist and song names you're interested in
artist_name = "Justin Bieber"
song_title = "What do you Mean"

url = f'http://ws.audioscrobbler.com/2.0/?method=track.search&track={song_title}&artist={artist_name}&api_key={api_lastfm}&format=json'

# Make the GET request
response = requests.get(url)

# Parse the JSON response
data = response.json()

# Extract information from the response
tracks = data['results']['trackmatches']['track']

for track in tracks:
    print(f"Track: {track['name']} by {track['artist']}")


""" # Search for the artist
artist_results = network.search_for_artist(artist_name)

if artist_results:
    # Get the first artist from the search results
    artist = artist_results[0]

    # Retrieve a list of the artist's tracks
    tracks = artist.get_top_tracks()

    # Find the desired song in the list of tracks
    for track in tracks:
        if track.title.lower() == song_title.lower():
            # Get the top tags (genres) associated with the track
            tags = track.get_top_tags()
            if tags:
                genres = [tag.item.name for tag in tags]
                print(f"Genres for '{song_title}' by {artist_name}: {', '.join(genres)}")
            else:
                print("Genre information not available for this song.")
            break
    else:
        print(f"'{song_title}' by {artist_name} not found in top tracks.")
else:
    print(f"Artist '{artist_name}' not found.")
 """


# Now, you can work with the 'data' variable to access the video information within the playlist.
