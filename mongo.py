from pymongo import MongoClient
import os

os.environ["MONGODB_URI"] = "mongodb://admin:admin12@ds159216.mlab.com:59216/videostats"
clientDB = MongoClient(os.environ["MONGODB_URI"])
db = clientDB.get_default_database()
statsColl = db.stats
