import spider
from mongo import statsColl
import os
import datetime
from flask import abort


def findById(id):
    res = statsColl.find_one({"id": id})
    return res


def save(data):
    data["date"] = datetime.datetime.utcnow()
    try:
        statsColl.insert(data)
        return "saved"
    except NameError:
        abort(500)


def startCrawling(url):
    return spider.scrapyYoutube(url)
