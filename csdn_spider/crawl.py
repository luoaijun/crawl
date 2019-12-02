# -*- coding: utf-8 -*-
import urllib.request
import requests
from io import BytesIO
import gzip


class Crawl:
    def getHtml(self, url, code):
        html = requests.get(url)
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
