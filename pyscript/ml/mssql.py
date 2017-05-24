# -*- coding: utf-8 -*-

import pymssql
import configparser


class mssql(object):

    def __init__(self):
        cf = configparser.ConfigParser()
        cf.read("app.conf")
        self.host = cf.get("mssql_database", "host")
        self.user = cf.get("mssql_database", "user")
        self.pwd = cf.get("mssql_database", "pwd")
        self.db = cf.get("mssql_database", "db")

    def getConnect(self):
        """ 
        得到连接信息 
        返回: conn.cursor() 
        """
        # if not self.db:
        #    raise(NameError,"没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, timeout=5,
                                    login_timeout=2, charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, "连接数据库失败")
        else:
            return cur

            ##验证数据库连接

    def verifyConnection(self):
        try:
            if self.host == '':
                return False
            conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, timeout=1,
                                   login_timeout=1, charset="utf8")
            return True
        except:
            return False

    def execQuery(self, sql):
        """ 
        执行查询语句 
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段 
        """
        cur = self.getConnect()
        cur.execute(sql)
        resList = cur.fetchall()
        # resList = cur.description
        # 查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def execNonQuery(self, sql):
        """ 
        执行非查询语句 
        调用示例： 
            cur = self.getConnect() 
            cur.execute(sql) 
            self.conn.commit() 
            self.conn.close() 
        """
        cur = self.getConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

    def execStoreProduce(self, sql):
        """ 
        执行查询语句 
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段 

        调用示例： 

        """
        cur = self.getConnect()
        cur.execute(sql)
        resList = cur.fetchall()
        self.conn.commit()
        # 查询完毕后必须关闭连接
        self.conn.close()
        return resList



