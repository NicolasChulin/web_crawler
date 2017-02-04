from bs4 import BeautifulSoup

def parseHtml(html):
    htmls = BeautifulSoup(htmStr,'html.parser')
    conts = {
        'cont':{},
        'urls':[]
    }

    # title
    conts['cont']['title'] = htmls.title.string.replace('_百度百科','')

    # pic
    summary_pic = htmls.find(class_='summary-pic')
    conts['cont']['pic'] = summary_pic.find('img').src

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
    for i in range(len(items)/2):
        kv = {}
        kv['name'] = items[2*i].string
        kv['value'] = items[2*i+1].string
        conts['cont']['base_info'].append(kv)

    # new urls
    liss = htmls.find_all(class_='js-cardTitle')
    newUrls = []
    for l in liss:
        if l.contents[0].string.find('历史人物') > -1:
            zhixins = l.find_next_siblings(class_='zhixin-list')
            for item in zhixins.contents:
                url = item.find_all('a')[0].href
                newUrls.append(url)
    conts['urls'] = newUrls

    return conts







