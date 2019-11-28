# -*- encoding: utf-8 -*-
from html.parser import HTMLParser
from lxml import etree
from bs4 import BeautifulSoup
import uuid

list = {}


class Parser(HTMLParser):
    def __init__(self, base, data):
        HTMLParser.__init__(self)
        self.base = base
        self.data = data

    def bParse(self):
        soup = BeautifulSoup(self.data, 'html.parser', from_encoding="utf8")  # 文档对象
        soup.encode('utf-8')

        for k in soup.find_all('a'):
            key = k.string
            if 'href' in str(k):
                value = k['href']
                if "http" not in value: value = self.base + value
                if key is None: key = uuid.uuid4()
                list[key] = value
        return list

    def article_parse(self):
        tree = etree.HTML(self.data)
        if tree == None: return None
        if len(tree.xpath('//article')) != 0:
            div = tree.xpath('//article')[0]
            div_str = etree.tounicode(tree.xpath('//div')[0])
            return div_str
