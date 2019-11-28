# -*- coding: utf-8 -*-
import urllib.request
import uuid

from csdn_spider.parse import Parser
from csdn_spider.crawl import Crawl

aurl = "https://www.csdn.net"

crawl = Crawl()
html = crawl.getHtml(aurl)
crawl.saveHtml("C:\\work\\data\\HTML", aurl, str(html))
parse = Parser(aurl, html)
blist = parse.bParse()
content = {}


def spider(list):
    for key, value in list.items():
        ahtml = crawl.getHtml(value)
        crawl.saveHtml("C:\\work\\data\\HTML\\base\\", str(uuid.uuid4()), str(ahtml))
        aparse = Parser(aurl, ahtml)
        context = aparse.article_parse()
        if context != None:
            content[key] = context
            crawl.saveHtml("C:\\work\\data\\HTML\\content\\", str(uuid.uuid4()), str(context))
        # yield spider(rList)


if __name__ == '__main__':
    spider(blist)
