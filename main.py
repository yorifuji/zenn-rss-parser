
import json
import urllib

username='yorifuji'

params = urllib.urlencode({'username':username})
articles_json = json.loads(urllib.urlopen('https://api.zenn.dev/articles?%s' % params).read())['articles']

class Article:
  def __init__(self, json):
    self.id         = json['id']
    self.title      = json['title'].encode('utf-8')
    self.created_at = json['created_at'].encode('utf-8')
    self.published  = json['published']
    self.url        = 'https://zenn.dev/%s/articles/%s' % (username, json['slug'].encode('utf-8'))

articles = sorted(filter(lambda article: article.published, [Article(json) for json in articles_json]), key=lambda article: article.created_at)

print 'id,title,url,created_at'
for article in articles:
  print '%d,%s,%s,%s' % (article.id, article.title, article.url, article.created_at)
