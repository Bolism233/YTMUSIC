import requests, json, pylast, re
from collections import defaultdict
from credentials import api_key, api_lastfm, api_secret

def search(input_dict):

    for artist_name, song_names in input_dict.items():
        for song_name in song_names:
            if len(song_name) > 1:
                search_track(artist_name, song_name)
            else:
                search_track(artist_name, song_names)

def search_track(artist_name, song_name):
    limit = 1
    url = f'http://ws.audioscrobbler.com/2.0/?method=track.search&track={song_name}&artist={artist_name}&api_key={api_lastfm}&format=json&limit={limit}'
    
    response = requests.get(url)
    data = response.json()

    try:
        if 'trackmatches' in data['results'] and 'track' in data['results']['trackmatches']:
            track = data['results']['trackmatches']['track'][0]
            print(f"\nTrack: {track['name']} by {track['artist']}")

            art = track['artist']
            song = track['name']
            find_similar(art, song)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return []




def find_similar(art, song):
    limit = 1
    url = f'http://ws.audioscrobbler.com/2.0/?method=track.getsimilar&artist={art}&track={song}&api_key={api_lastfm}&format=json&limit={limit}'
    try:
        response = requests.get(url)
        data = response.json()
        if 'similartracks' in data and 'track' in data['similartracks']:
            similar_tracks = data['similartracks']['track'][0]['name']
            artist = data['similartracks']['track'][0]['artist']['name']
            print(f"Similar Track: {similar_tracks} + {artist}")
            return similar_tracks, artist
        # else:
            # print("Didn't find any result")
    except:
        print("Didn't find any result")
        return []
