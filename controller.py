import os
import datetime
from flask import jsonify
from flask import abort
import spider
from mongo import statsColl


def getList(args):
    try:
        page = int(args.get('page'))
        per = int(args.get('per'))
        if not (page > -1 and per > 0):
            raise Exception('not found')
        skip = 0
        if page > 0:
            skip = page * per

        data = []

        for item in statsColl.find().skip(skip).limit(per).sort("date"):
            data.append({
                "id": item['id'],
                "name": item['name'],
                "likes": item['likes'],
                "dislikes": item['dislikes'],
                "views": item['views'],
                "subscribers": item['subscribers'],
                "published": item['published'],
                "url": item['url']
            })

        total = statsColl.find().count()

        res = {
            "data": data,
            "page": page,
            "per": per,
            "total": total
        }
    except NameError:
        res = {}
    return res


def findById(id):
    try:
        data = statsColl.find_one({"id": id})
        res = {
            "id": id,
            "name": data['name'],
            "likes": data['likes'],
            "dislikes": data['dislikes'],
            "views": data['views'],
            "subscribers": data['subscribers'],
            "published": data['published'],
            "url": data['url']
        }
    except:
        res = {}
    return res


def save(data):
    data["date"] = datetime.datetime.utcnow()
    try:
        statsColl.insert(data)
        return "saved"
    except NameError:
        abort(500)


def startCrawling(url):
    try:
        res = spider.scrapyYoutube(url)
    except NameError:
        res = {}
    return res
