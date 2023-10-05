import requests, json, pylast, re
from collections import defaultdict
from credentials import api_key, api_lastfm, api_secret

def search_track(artist_name, song_name):
    limit = 1
    url = f'http://ws.audioscrobbler.com/2.0/?method=track.search&track={song_name}&artist={artist_name}&api_key={api_lastfm}&format=json&limit={limit}'
    
    response = requests.get(url)
    data = response.json()

    try:
        if 'trackmatches' in data['results'] and 'track' in data['results']['trackmatches']:
            track = data['results']['trackmatches']['track'][0]
            print(f"Track: {track['name']} by {track['artist']}")

            art = track['name']
            song = track['artist']
            find_similar(art, song)
        else:
            print("Wrong")
            return None
    except Exception as e:
        # print(f"An error occurred: {str(e)}")
        return None




def find_similar(art, song):
    limit = 1
    url = f'http://ws.audioscrobbler.com/2.0/?method=track.getsimilar&artist={art}&track={song}&api_key={api_lastfm}&format=json&limit={limit}'
    response = requests.get(url)
    data = response.json()
    
    try:
        if 'similartracks' in data and 'track' in data['similartracks']:
            similar_tracks = data['similartracks']['track'][0]
            print(similar_tracks)
            return similar_tracks  # Returns a list of similar songs
    except Exception as e:
        return f"An error occurred: {str(e)}"
