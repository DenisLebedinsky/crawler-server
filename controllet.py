from mongo import collstats
import os
import crawler


def save(data):

    return colStats.insert_one(newDoc)


def findOne(url):
    return colStats.find({"url": url})


def create_projectDirectory(directory):
    if not os.path.exist(directory)
    os.makedirs(directory)


def startCrawling(project_name, url):
    crawler(url)

# create new file


def write_file(path, data):
    f = open(path, w)
    f.write(data)
    f.close
