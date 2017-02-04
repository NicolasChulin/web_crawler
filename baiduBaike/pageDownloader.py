
import requests


def getPageContent(url):
    response = requests.get(url)
    return response.text
