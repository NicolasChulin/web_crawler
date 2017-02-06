import requests


def getPageContent(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    response = requests.get(url,headers=headers,timeout=10)
    response.encoding = 'utf8'
    return response.text
