from bs4 import BeautifulSoup
import requests
import re


def scrapyYoutube(url):

    r = requests.get(url)
    data = r.text.encode("utf-8")
    soup = BeautifulSoup(data, 'html.parser')
    
    name = soup.find('span', {'id': 'eow-title'}).getText().strip()

    likes = soup.find('button', {'class': 'like-button-renderer-like-button'}
                      ).find('span', {'class', 'yt-uix-button-content'}).getText()

    dislikes = soup.find('button', {'class': 'like-button-renderer-dislike-button'}
                         ).find('span', {'class', 'yt-uix-button-content'}).getText()

    viewsText = soup.find('div', {'class': 'watch-view-count'}).getText()

    views = int(''.join(x for x in viewsText if x.isdigit()))

    subscribers = soup.find(
        'span',
        {'class': 'yt-subscription-button-subscriber-count-branded-horizontal'}).getText()

    publishedFull = soup.find(
        'strong', {'class': 'watch-time-text'}).getText()

    try:
        published = publishedFull.split('on').pop().strip()
    except Exception:
        published = publishedFull

    result = {
              'url': url,
              'name': name,
              'likes': likes,
              'dislikes': dislikes,
              'views': views,
              'subscribers': subscribers,
              'published': published
              }

    return result
