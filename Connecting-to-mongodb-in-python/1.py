import os

from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient

load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]
# Create a new client and connect to the server
client = MongoClient(MONGODB_URI)

for dbname in client.list_database_names():
    print(dbname)


client.close()