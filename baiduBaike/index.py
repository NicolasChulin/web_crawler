
from baiduBaike import urlManager,pageDownloader,pageParser,application


def baiduBaike():

    if not urlManager.hasNewUrl():
        return
    newUrl = urlManager.getNewUrl()
    pageCont = pageDownloader.getPageContent(newUrl)
    pageParserCont = pageParser.parseHtml(pageCont)
    application.saveValueCont(pageParserCont['cont'])
    urlManager.addNewUrls(pageParserCont['urls'])
    baiduBaike()


if __name__ == '__main__':
    url = 'https://www.baidu.com'
    urlManager.addNewUrls(url)
    baiduBaike()
