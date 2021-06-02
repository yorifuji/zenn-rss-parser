import json
import feedparser # pip install feedparser
import datetime
import time
import sys

class Article:
  def __init__(self, json):
    self.title      = json['title']
    self.link       = json['link']
    self.published  = datetime.datetime.fromtimestamp(time.mktime(json['published_parsed'])+3600*9).isoformat() + "+09:00"

def parse(username):
  articles_json = feedparser.parse('https://zenn.dev/' + username + '/feed').entries
  return sorted([Article(json) for json in articles_json], key=lambda article: article.published)

if __name__=='__main__':
  if len(sys.argv) > 0:
    articles = parse(sys.argv[1])
    for article in articles:
      print(article.published, article.link, article.title, sep=',')
  else:
    print("Usage: main.py [username]")

