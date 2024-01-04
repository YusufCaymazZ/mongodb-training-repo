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
"""new_account = {
    "acc_holder" : "Linus Torvalds",
    "acc_id":"MD3948284",
    "acc_type":"checking",
    "balance":43587934,
    "last_updated":datetime.datetime.utcnow(),
}

result = accounts_collection.insert_one(new_account)

document_id = result.inserted_id
print(f"_id of inserted document : {document_id}")

# Query by ObjectId
#document_to_find = {"_id": ObjectId(document_id)}
"""
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
# Filter
select_accounts = {"balance": { "$gte" : 100}}

# Update 
set_field = {"$set" : {"balance" : 200}}

# Write an expression that adds a 'minimum_balance' field to each savings acccount and sets its value to 100.
result = accounts_collection.update_many(select_accounts, set_field)

print("Documents matched: " + str(result.matched_count))
print("Documents updated: " + str(result.modified_count))
pprint.pprint(accounts_collection.find_one(select_accounts))



client.close