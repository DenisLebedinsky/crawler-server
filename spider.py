from bs4 import BeautifulSoup
import requests
import re
import uuid


def scrapyYoutube(url):


	r = requests.get(url)
	data = r.text.encode("utf-8")
	soup = BeautifulSoup(data, 'html.parser')
	id = uuid.uuid4()
	name = soup.find('span', {'id': 'eow-title'}).getText().strip()
	likes = soup.find('button', {'class': 'like-button-renderer-like-button'}
										).find('span', {'class', 'yt-uix-button-content'}).getText()
	unlikes = soup.find('button', {'class': 'like-button-renderer-dislike-button'}
											).find('span', {'class', 'yt-uix-button-content'}).getText()
	viewsText = soup.find('div', {'class': 'watch-view-count'}).getText()
	views = int(''.join(x for x in viewsText if x.isdigit()))
	subscribers = soup.find(
			'span', {'class': 'yt-subscription-button-subscriber-count-branded-horizontal'}).getText()
	result = {'id': id, 'name': name, 'likes': likes,
				'unlikes': unlikes, 'views': views, 'subscribers': subscribers}

	return result
