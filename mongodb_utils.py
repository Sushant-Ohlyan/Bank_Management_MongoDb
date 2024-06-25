from pymongo import MongoClient

# MongoDB's connection setup for local instance
client = MongoClient("mongodb://localhost:27017/")  # Replace with your local MongoDB URI

# Specify the database name
db = client["bank"]  # Replace with your database name

# Specify the collection name
account_collection = db["accounts"]


def get_account_collection():
    return account_collection


def close_connection():
    client.close()
