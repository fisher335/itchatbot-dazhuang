#coding=utf-8
import requests
import json
# from tornado.escape import json_decode

__name__ = 'v2ex'


def test(data, msg=None, bot=None):
    if 'v2ex' in data and '话题' in data and '最新' in data:
        return True
    return False


def respond(data, msg=None, bot=None):
    res = requests.get("http://www.v2ex.com/api/topics/latest.json")
    topics = json.loads(res.text)
    articles = []
    i = 0
    while i < 10:
        article = dict()
        article['title'] = topics[i]['title']
        article['url'] = topics[i]['url']
        if i == 0:
            article['picurl'] = 'http://openoceans.de/img/v2ex_logo_uranium.png'
        else:
            article['picurl'] = ''
        article['description'] = topics[i]['content_rendered'][0:100]
        articles.append(article)
        i += 1
    return articles
