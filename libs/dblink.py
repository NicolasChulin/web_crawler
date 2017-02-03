import pymysql
from web_crawler import setting


class Pydb(object):

    def __init__(self,db_name=None):
        self.connect(db_name)
        super(Pydb,self).__init__(db_name)

    def get_config(self,db_name=None):
        return {
            'host': setting.HOST,
            'port': setting.PORT,
            'user': setting.USER,
            'passwd': setting.PASSWORD,
            'db':db_name if db_name else setting.NAME,
            'charset':'utf8mb4',
            'cursorclass':pymysql.cursors.DictCursor
        }

    def connect(self,db_name=None):
        config = self.get_config(db_name)
        self.conn = pymysql.connect(**config)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def create(self,data,tb_name):
        keys=[]
        values=[]
        for k,v in data.items():
            keys.append(k)
            values.append(v)
        sql="INSERT INTO %s (%s) VALUES (%s)" % (tb_name,','.join(keys),','.join(values))
        self.cursor.execute(sql)

    def update(self,setd,whered,tb_name):
        sets = []
        wheres = []
        for k,v in setd.items():
            sets.append("%s='%s'" % (k,v))
        for k,v in whered.items():
            wheres.append("%s='%s'" % (k,v))

        sql="UPDATE %s SET %s WHERE %s" % (tb_name,','.join(sets),' and '.join(wheres))
        self.cursor.execute(sql)

    def delete(self,whered,db_name):
        wheres = []
        for k,v in whered.items():
            wheres.append("%s='%s'" % (k,v))

        sql="DELETE FROM %s WHERE %s" % (tb_name,' and '.join(wheres))
        self.cursor.execute(sql)






