#导入pymysql的包
import pymssql
import threading


class query(object):
    def __init__(self):
        self.conn = self.get_connect()

    def demo(self, year: int) -> list:

        try:
            sql="SELECT MAX(m.CustomerSysNo) ,m.Status, item.ProductSysNo,SUM(item.Quantity) FROM  IPP3.dbo.SO_Master m WITH ( NOLOCK ) " \
                "INNER JOIN IPP3.dbo.SO_CheckShipping c WITH(NOLOCK) ON c.SOSysNo=m.SysNo " \
                "LEFT JOIN IPP3.dbo.SO_Item item WITH(NOLOCK) ON item.SOSysNo = m.SysNo " \
                "LEFT JOIN IPP3.dbo.Product p  WITH(NOLOCK) ON p.SysNo=item.ProductSysNo " \
                "WHERE c.IsPhoneOrder NOT IN(5,15) AND item.ProductType <>3   AND p.Status>0  AND YEAR(m.OrderDate)="+str(year)+" " \
                "GROUP BY item.ProductSysNo,m.Status"

            self.conn.execute(sql)
            data = self.conn.fetchall()
            return data
            # cur.close()#关闭游标
            # conn.close()#释放数据库资源
        except Exception as e:
            print("查询失败:" + e)

    def get_connect(self):
        """ 
            获取连接信息 
            返回: conn.cursor() 
            """
        # if not self.db:
        #    raise(NameError,"没有设置数据库信息")
        self.conn = pymssql.connect(
            host='10.10.6.115',
            port="1435",
            user='bigdatateam',
            password='Kjt.com',
            database='IPP3',
            charset='UTF-8')
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, "连接数据库失败")
        else:
            return cur


if __name__ == '__main__':
    q = query()
    data = q.demo()
    for order in data:
        print(order[0])