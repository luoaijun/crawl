# -*- encoding: utf-8 -*-
from html.parser import HTMLParser
from lxml import etree
from bs4 import BeautifulSoup
import uuid

list = {}


class Parser(HTMLParser):
    def __init__(self, base):
        HTMLParser.__init__(self)
        self.base = base

    def bParse(self, datas):
        soup = BeautifulSoup(datas, 'html.parser', from_encoding="utf8")  # 文档对象
        soup.encode('utf-8')

        for k in soup.find_all('a'):
            key = k.string
            if 'href' in (dict)(k.attrs):
                value = k['href']
                if "http" not in value: value = self.base + value
                if key is None: key = uuid.uuid4()
                list[key] = value
        return list

    def article_parse(self,data):
        tree = etree.HTML(data)
        if tree == None: return None
        if len(tree.xpath('//*[@id="mainBox"]/main/div[1]')) != 0:
            div = tree.xpath('//*[@id="mainBox"]/main/div[1]')[0]
            div_str = etree.tounicode(tree.xpath('//div')[0])
            return div_str
