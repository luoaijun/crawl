# -*- coding: utf-8 -*-
import urllib.request
import uuid
from data_spider.parse import Parser
from data_spider.crawl import Crawl
import configparser

cf = configparser.ConfigParser()
cf.read("setting.ini")
aurl = cf.get("jianshu","base_url")
url = {}
crawl = Crawl()
html = crawl.getHtml(aurl,"utf-8")
crawl.saveHtml("C:\\work\\data\\HTML\\", "jianshu", str(html))
parse = Parser(aurl)
blist = parse.bParse(html)
list = dict((key, value) for key, value in blist.items() if len(str(key)) < 5)
content = {}


def getUrl(list, rex):
    result = []
    for key, value in list.items():
        ahtml = crawl.getHtml(value,"UTF-8")
        crawl.saveHtml("C:\\work\\data\\HTML\\base\\", str(uuid.uuid4()), str(ahtml))
        rList = Parser(aurl).bParse(ahtml)
        list = dict((key, value) for key, value in rList.items() if rex in str(value))
        result.append(list)  # 每个链接页面中包含的链接
    return result


def getAirtle(ulist):
    for list in ulist:
        for key, value in list.items():
            aparse = Parser(aurl)
            airtleHtml = crawl.getHtml(value,"utf-8")
            crawl.saveHtml("C:\\work\\data\\HTML\\content\\", str(uuid.uuid4()), str(airtleHtml))
            context = aparse.article_parse(airtleHtml)
            if context != None:
                content[key] = context


def run():
    getAirtle(getUrl(list, cf.get("jianshu","filter")))


if __name__ == '__main__':
    run()
