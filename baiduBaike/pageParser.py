from bs4 import BeautifulSoup

def parseHtml(html):
    htmls = BeautifulSoup(html,'html.parser')
    conts = {
        'cont':{}
    }

    # title
    conts['cont']['title'] = htmls.title.string.replace('_百度百科','')


    # pic
    summary_pic = htmls.find(class_='summary-pic')
    img = summary_pic.find('img')
    conts['cont']['pic'] = img['src']

    # lemma-summary
    lemma_summary = htmls.find(class_='lemma-summary')
    items = lemma_summary.find_all(class_='para')
    summary = ''
    for item in items:
        strs = item.stripped_strings
        for s in strs:
            summary += s
    conts['cont']['summary'] = summary

    # base-info
    baseinfos = htmls.find(class_='basic-info')
    items = baseinfos.find_all(class_='basicInfo-item')
    conts['cont']['base_info']=[]
    num = len(items)//2
    for i in range(num):
        kv = {}
        kv['name'] = get_string(items[2*i].stripped_strings)
        kv['value'] = get_string(items[2*i+1].stripped_strings)
        conts['cont']['base_info'].append(kv)

    # new urls
    liss = htmls.find(class_='zhixin-box')
    # print(liss['data-newlemmaid'])

    # liss = htmls.find_all(class_='zhixin-group')
    # newUrls = []
    # for l in liss:
    #     h6 = l.find('h6')
    #     if h6.contents[0].string.find('历史人物') > -1:
    #         zhixins = h6.find_next_siblings(class_='zhixin-list')
    #         for item in zhixins.contents:
    #             url = item.find_all('a')[0]['href']
    #             newUrls.append(url)
    # conts['urls'] = newUrls

    return conts


def get_string(strs):
    summary = ''
    for s in strs:
        summary += s
    return summary.replace('\xa0','')







