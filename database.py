from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017/"

client = MongoClient(MONGO_URI)
print(client.list_database_names())

db = client['TelegramBot_DB']

def get_users_collection():
    return db["users"]

def get_chat_collection():
    return db["chat_history"]

def get_files_collection():
    return db["files"]
