# -*- coding: utf-8 -*-
import urllib.request
import requests
from io import BytesIO
import gzip
import json
from data_spider.api import getIP

proxy = getIP()


class Crawl:
    def getHtml(self, url, code):
        dict = json.loads(proxy)
        html = requests.get(url, dict, timeout=1000)
        html.encoding = code
        return html.text

    def getHtml2(self, url, code):
        req_one = urllib.request.Request(url)
        res_one = urllib.request.urlopen(req_one)
        response = res_one.read()
        if isinstance(response, bytes):
            response = response.decode(code)
        html = str(response.decode(code))
        # buff = BytesIO(html)
        # f = gzip.GzipFile(fileobj=buff)
        # res = f.read().decode('utf-8')
        return html

    def saveHtml(self, path, file_name, file_content):
        # 注意windows文件命名的禁用符，比如 /
        with open(path + file_name.replace('/', '_') + ".html", "w", encoding='utf-8') as f:
            # 写文件用bytes而不是str，所以要转码
            f.write(file_content)
