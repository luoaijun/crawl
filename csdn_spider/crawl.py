# -*- coding: utf-8 -*-
import urllib.request


class Crawl:
    def getHtml(self, url):
        response = urllib.request.urlopen(url)
        html = str(response.read().decode("utf-8","ignore"))
        return html

    def saveHtml(self, path, file_name, file_content):
        # 注意windows文件命名的禁用符，比如 /
        with open(path + file_name.replace('/', '_') + ".html", "w", encoding='utf-8') as f:
            # 写文件用bytes而不是str，所以要转码
            f.write(file_content)
