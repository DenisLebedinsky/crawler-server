import pymongo
import os

os.environ["MONGODB_URI"] = "mongodb://admin:admin123@ds159216.mlab.com:59216/videostats"

db = pymongo.MongoClient(os.environ["MONGODB_URI"])

collstats = db["stats"]
