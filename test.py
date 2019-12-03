import requests

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

    run(proxy,utl)