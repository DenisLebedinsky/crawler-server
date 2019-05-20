from mongo import colStats
import os

def save(data):
	newDoc = {"url": "https: // habr.com/ru/post/328800/", "likes":"65", "dislikes":"12", "comments":"5"}
	return colStats.insert_one(newDoc)
	
	
def findOne(url):
		return colStats.find({"url":url})

def create_projectDirectory(directory):
	if not os.path.exist(directory)
	os.makedirs(directory)


def crawler(project_name, url):
		queue = project_name+ '/queue.txt'
		crawled = project_name + '/crawled.txt'
		if not os.path.isfile(queue):
			write_file(queue, url)
			if not os.path.isfile(crawled):
				write_file(crawled, '')

#create new file 
def write_file(path, data):
	f = open(path, w)
	f.write(data)
	f.close
