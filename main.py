import json
import feedparser
import datetime
import time

class Article:
  def __init__(self, json):
    self.title      = json['title']
    self.link       = json['link']
    self.published  = datetime.datetime.fromtimestamp(time.mktime(json['published_parsed'])+3600*9).isoformat() + "+09:00"

username='yorifuji'
articles_json = feedparser.parse('https://zenn.dev/' + username + '/feed').entries
articles = sorted(filter(lambda article: article.published, [Article(json) for json in articles_json]), key=lambda article: article.published)

for article in articles:
  print(article.link, article.published, article.title, sep=',')
