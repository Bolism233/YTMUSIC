from pymongo import MongoClient

# Replace these with the credentials and hostname from your Docker Compose setup
username = 'rootuser'
password = 'rootpass'
hostname = 'localhost'  # or use the Docker Machine IP if you're using Docker Machine
port = 27017


# Construct the connection string
conn_str = f"mongodb://{username}:{password}@{hostname}:{port}/?authSource=admin"

# Connect to MongoDB
client = MongoClient(conn_str)

# Specify the database to use
db = client['testdb']

# Specify the collection to use
collection = db['testcollection']

# Insert a document
# collection.insert_one({'singer': 'Ed Sheeran', 'songTitle': "Castle on the Hill"})
# collection.insert_one({'singer': 'Ed Sheeran', 'songTitle': "Perfect"})
# collection.insert_one({'singer': 'JB', 'songTitle': "Perfect"})
# collection.insert_one({'singer': 'JB', 'songTitle': "Perfect"})

# Retrieve all documents in the collection
for doc in collection.find():
    # collection.delete_many({'singer':'Ed Sheeran'})
    print(doc)

# Close the connection
client.close()
