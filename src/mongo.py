from dotenv import load_dotenv
import os
from pymongo.mongo_client import MongoClient

load_dotenv()
mongo_uri = os.getenv("MONGO_URI")

# Create a new client and connect to the server
cluster = MongoClient(mongo_uri)

#extract the main MangaShell database
mainDB = cluster["MangaShell"]

#extract the entires collection
entries = mainDB["entries"]

#for testing purposes
userID = 777

def get_entries_collection():
    return entries