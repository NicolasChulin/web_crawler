
from urlManager import hasNewUrl,addNewUrls
from pageDownloader import getPageContent
from pageParser import parseHtml
from application import saveValueCont
import json

def baiduBaike():
    newUrl = hasNewUrl()
    if not newUrl:
        return False

    pageCont = getPageContent(newUrl)
    pageParserCont = parseHtml(pageCont)
    # print(pageParserCont)
    # saveValueCont(pageParserCont['cont'])
    # addNewUrls(pageParserCont['urls'])
    # baiduBaike()


if __name__ == '__main__':
    url = 'http://baike.baidu.com/view/3898928.htm'
    addNewUrls([url])
    baiduBaike()
