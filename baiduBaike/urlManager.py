from libs.dblink import Pydb
from datetime import datetime

def hasNewUrl():
    db = Pydb()
    table = 'web_urls'
    count = db.get_count(table)
    if count['num'] >= 100:
        db.close()
        return False

    whered = {
        'is_crawler':'0'
    }
    newurl = bd.get_first_item(table,whered)
    if newurl:
        whered = {
            'id':newurl['id']
        }
        setd = {
            'is_crawler':'1'
        }
        bd.update(table,setd,whered)
        db.close()
        return newurl['url']
    else:
        db.close()
        return False


def addNewUrls(urls):
    db = Pydb()
    table = 'web_urls'
    for url in urls:
        whered={'url':url}
        is_exist = db.filter(table,whered)
        if is_exist:
            continue
        else:
            data = {
                'url':url,
                'created_at':datetime.now()
            }
            db.create(table,data)

    db.close()


