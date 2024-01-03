import pymongo
import datetime
import os

from dotenv import load_dotenv
from pymongo import MongoClient

#load_dotenv()
#uri = os.environ["uri"]

client = MongoClient("mongodb+srv://yuscaymaz:psswrd@train.vxtmeeb.mongodb.net/?retryWrites=true&w=majority")

db = client.bank

accounts_collection = db.accounts_collection

new_account = {
    "acc_holder" : "Linus Torvalds",
    "acc_id":"MD3948284",
    "acc_type":"checking",
    "balance":43587934,
    "last_updated":datetime.datetime.utcnow(),
}

result = accounts_collection.insert_one(new_account)

document_id = result.inserted_id
print(f"_id of inserted document : {document_id}")

client.close