import json
from urllib.request import Request, urlopen
import configparser
import requests
cf = configparser.ConfigParser()
cf.read("setting.ini")
api = cf.get("ip", "api")


def getIP():
    # 代理IP获取数据Api
    url = api
    print(url)
    # 包装头部
    firefox_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    # 构建请求
    ll=requests.get(url,"utf-8").text
    # 获取数据

    # 转换成字符串
    return ll
