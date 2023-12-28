from pymongo import MongoClient

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

def insert_data(singer, songTitle):
    collection.insert_one({'singer':singer, 'songTitle': songTitle})

# Retrieve all documents in the collection
# for doc in collection.find():
def delete_data(singer):
    collection.delete_many({'singer': singer})
#     print(doc)

# Close the connection
# client.close()
