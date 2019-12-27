from os import path

import requests
import os
utl = 'https://www.jianshu.com/p/a276983ec20d'
url = 'https://www.oschina.net/p/diboot'
csdn = 'https://blog.csdn.net/stormdony/article/details/79828842'
proxy = {'https': '180.122.224.209:9999'}

def run(proxy,url):
    try:
        print("proxy:{}".format(proxy))
        s = requests.Session()
        proxies = proxy
        header = {
            "Host": "www.xxx.com",
            "Referer": "http://www.xxx.com/xxx.html?199",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"

        }
        ret = s.get(url=url)
        rc = ret.content.decode("utf-8")
        print(rc)
    except:
        pass

if __name__ == '__main__':
    import os

    d = path.dirname(__file__)  # 返回当前文件所在的目录
    parent_path = os.path.dirname(d)  # 获得d所在的目录,即d的父级目录
    parent_path = os.path.dirname(parent_path)  ##获得parent_path所在的目录即parent_path的父级目录

