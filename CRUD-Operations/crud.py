import pymongo
import datetime
import os
from bson import ObjectId
import pprint
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
uri = os.environ["uri"]

client = MongoClient(uri)

db = client.bank

accounts_collection = db.accounts_collection
#INSERTING
new_accounts = [{
    "acc_holder" : "Linus Torvalds",
    "acc_id":"MD393445345",
    "acc_type":"checking",
    "balance":1500,
    "last_updated":datetime.datetime.utcnow(),
},
{
    "acc_holder" : "Linuz Torvalds",
    "acc_id":"MD393445284",
    "acc_type":"checking",
    "balance":1750,
    "last_updated":datetime.datetime.utcnow(),
},
{
    "acc_holder" : "Linux Torvalds",
    "acc_id":"MD393447884",
    "acc_type":"checking",
    "balance":2500,
    "last_updated":datetime.datetime.utcnow(),
},
{
    "acc_holder" : "Linux Torvalds",
    "acc_id":"MD393447884",
    "acc_type":"checking",
    "balance":2500,
    "last_updated":datetime.datetime.utcnow(),
},
]

result = accounts_collection.insert_many(new_accounts)

document_ids = result.inserted_ids

print("# of documents inserted: " + str(len(document_ids)))
print(f"_ids of inserted documents: {document_ids}")


# Query by ObjectId
#document_to_find = {"_id": ObjectId(document_id)}

#FINDING
"""documents_to_find2 = {"balance": {"$gt": 4700}}


# Write an expression that retrieves the document matching the query constraint in the 'accounts' collection.
result = accounts_collection.find_one(documents_to_find2)

num_docs = 0
for document in result:
    num_docs += 1
    pprint.pprint(result)
    print()

print("# of documents found: " + str(num_docs))"""

#UPDATING
"""# Filter
select_accounts = {"balance": { "$gte" : 100}}

# Update 
set_field = {"$set" : {"balance" : 200}}

# Write an expression that adds a 'minimum_balance' field to each savings acccount and sets its value to 100.
result = accounts_collection.update_many(select_accounts, set_field)

print("Documents matched: " + str(result.matched_count))
print("Documents updated: " + str(result.modified_count))
pprint.pprint(accounts_collection.find_one(select_accounts))
"""
#DELETE
"""# Filter for accounts with balance less than $2000
documents_to_delete = {"balance": {"$gt": 1600}}

# Search for sample document before delete
print("Searching for sample target document before delete: ")
pprint.pprint(accounts_collection.find_one(documents_to_delete))

# Write an expression that deletes the target accounts.
result = accounts_collection.delete_many(documents_to_delete)

# Search for sample document after delete
print("Searching for sample target document after delete: ")
pprint.pprint(accounts_collection.find_one(documents_to_delete))

print("Documents deleted: " + str(result.deleted_count))
"""
client.close()