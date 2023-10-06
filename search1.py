import requests, json, pylast, re
from collections import defaultdict
from credentials import api_key, api_lastfm, api_secret

def search(input_dict):
    similar_songs_dict = defaultdict(list)

    for artist_name, song_names in input_dict.items():
        for song_name in song_names:
            if len(song_name) > 1:
                similar_tracks = search_track(artist_name, song_name)
                if similar_tracks:
                    similar_songs_dict[artist_name].extend(similar_tracks)

    return similar_songs_dict

def search_track(artist_name, song_name):
    limit = 5  # You can adjust the limit as needed
    url = f'http://ws.audioscrobbler.com/2.0/?method=track.getsimilar&artist={artist_name}&track={song_name}&api_key={api_lastfm}&format=json&limit={limit}'

    try:
        response = requests.get(url)
        data = response.json()
        similar_tracks = []

        if 'similartracks' in data and 'track' in data['similartracks']:
            for track in data['similartracks']['track']:
                similar_tracks.append(track['name'])
                
        return similar_tracks
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return []
