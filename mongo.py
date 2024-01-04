from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
import requests
from credentials import *

username = 'rootuser'
password = 'rootpass'
hostname = 'localhost'  # or use the Docker Machine IP if you're using Docker Machine
port = 27017

# Construct the connection string
conn_str = f"mongodb://{username}:{password}@{hostname}:{port}/?authSource=admin"
# Connect to MongoDB
# Replace these with the credentials and hostname from your Docker Compose setup
client = MongoClient(conn_str)
# Specify the database to use
db = client['testdb']
# Specify the collection to use
collection = db['testcollection']

collection.delete_many({})

# Iterate through the cursor and print information about each index
# indexes = collection.list_indexes()
# for index in indexes:
#     print(index)
    # only needs to be created once
# collection.drop_index()
# collection.create_index([("compositeKey", 1)], unique=True)
def get_all_tracks(artist, page_number):
    print(page_number)
    song_url = f"http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist={artist}&api_key={api_lastfm}&limit=3250&page={page_number}&format=json"
    response = requests.get(song_url).json()
    tracks = [track['name'] for track in response['toptracks']['track']]
    return response, tracks

def insert_data(artist, songTitle):
    try:
        collection.insert_one({'compositeKey': artist+ "-" + songTitle, 'artist': artist, 'songTitle': songTitle})
    except DuplicateKeyError as e:
        print(f"Duplicate songs {e}")
# Lame way of avoiding duplicates
# if collection.find_one({"artist": artist, "songTitle": songTitle}):
#     print("This song already exists for the artist.")
#     pass
# else:
#     # Insert the new song for the artist
#     collection.insert_one({'artist':artist, 'songTitle': songTitle})

def delete_data(singer):
    collection.delete_many({'artist': singer})


def delete_all():
    collection.delete_many({})

# client.close()
