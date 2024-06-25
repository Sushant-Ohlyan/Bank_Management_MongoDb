# account_manager.py

from bson import ObjectId
from mongodb_utils import get_account_collection


def add_account(name, balance):
    account_collection = get_account_collection()
    account_collection.insert_one({"name": name, "balance": balance})


def list_accounts():
    account_collection = get_account_collection()
    for account in account_collection.find():
        print(f"ID: {account['_id']}, Name: {account['name']} and Balance: ${account['balance']}")


def update_account(account_id, new_name, new_balance):
    account_collection = get_account_collection()
    account_collection.update_one({'_id': ObjectId(account_id)}, {"$set": {"name": new_name, "balance": new_balance}})


def delete_account(account_id):
    account_collection = get_account_collection()
    account_collection.delete_one({"_id": ObjectId(account_id)})