from pymongo import MongoClient
import os

print(os.environ['FLASK_ENV'])

if os.environ['FLASK_ENV'] == 'prodaction':
    uri = os.environ["MONGODB_URI"]
if os.environ['FLASK_ENV'] == 'development':
    uri = os.environ["MONGODB_URI_DEV"]
if os.environ['FLASK_ENV'] == 'test':
    uri = os.environ["MONGODB_URI_TEST"]

clientDB = MongoClient(uri)
db = clientDB.get_default_database()
statsColl = db.stats
