from bs4 import BeautifulSoup
import requests


def parseResurse(url):


r = requests.get(url)

data = r.decode('utf-8')


soup = BeautifulSoup(data, 'html.parser')

name = soup.findAll('span', {'id': 'eow-title'})
likes = soup.findAll('span', {'title': 'Мне понравилось'})
dislikes = soup.findAll('span', {'title': 'Мне не понравилось'})
views_ = soup.findAll('div', {'class': 'watch-view-count'})
comments = 'null'
subscribers = soup.findAll('span', {'class': ' yt-subscriber-count'})
print()
