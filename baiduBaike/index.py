
from baiduBaike import urlManager,pageDownloader,pageParser,application


def baiduBaike():
    newUrl = urlManager.hasNewUrl()
    if not newUrl:
        return False

    pageCont = pageDownloader.getPageContent(newUrl)
    pageParserCont = pageParser.parseHtml(pageCont)
    application.saveValueCont(pageParserCont['cont'])
    urlManager.addNewUrls(pageParserCont['urls'])
    # baiduBaike()


if __name__ == '__main__':
    url = 'http://baike.baidu.com/view/3898928.htm'
    urlManager.addNewUrls([url])
    baiduBaike()
