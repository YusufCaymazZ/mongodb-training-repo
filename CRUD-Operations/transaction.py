import os

from dotenv import load_dotenv
from pymongo import MongoClient

"""
load_dotenv()
URI = os.environ("URI")
"""
client = MongoClient("mongodb+srv://username:psswrd@train.vxtmeeb.mongodb.net/?retryWrites=true&w=majority")

def callback(
    session,
    transfer_id=None,
    account_id_receiver = None,
    account_id_sender = None,
    transfer_amount = None
):
    accounts_collection = session.client.bank.new_accounts

    transfer_collection = session.client.bank.transfers

    transfer = {
        "transfer_id" : transfer_id,
        "to_account" : account_id_receiver,
        "from_account" : account_id_sender,
        "amount" : {"$numberDecimal" : transfer_amount},
    }

    accounts_collection.update_one({
        "account_id" : account_id_sender},
        {"$inc" : {"balance" : -transfer_amount},
        "$push":{"transfer_complete":transfer_id},
        },
        session=session,
    )

    accounts_collection.update_one({
        "account_id" : account_id_receiver},
        {"$inc" : {"balance" : transfer_amount},
        "$push":{"transfer_complete":transfer_id},
        },
        session=session,
    )

    transfer_collection.insert_one(transfer, session=session)
    print("transaction succesful")

    return

def callback_wrapper(s):
    callback(
        s,
        transfer_id="TR218721873",
        account_id_receiver="MD393445345",
        account_id_sender="MD393445345",
        transfer_amount=100,
    )

with client.start_session() as session:
    session.with_transaction(callback_wrapper)

client.close()