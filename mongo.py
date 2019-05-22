from pymongo import MongoClient
import os


clientDB = MongoClient(os.environ["MONGODB_URI"])
db = clientDB.get_default_database()
statsColl = db.stats
