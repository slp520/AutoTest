import pymysql
import readConfig as readConfig
from common.Log import MyLog as Log


#实例化一个参数
localReadConfig = readConfig.ReadConfig()

class MyDB:
    #定义全部变量
    global host, username, password, port, database, config
    #调用get_db方法取出host下同
    host = localReadConfig.get_db("host")
    username = localReadConfig.get_db("username")
    password = localReadConfig.get_db("password")
    port = localReadConfig.get_db("port")
    database = localReadConfig.get_db("database")
    config = {
        'host': str(host),
        'user': username,
        'passwd': password,
        'port': int(port),
        'db': database
    }

    # def __init__(self):
        # self.log = Log.get_log()
        # self.db = None
        # self.cursor = None

    def connectDB(self):
        try:
            # connect to DB 解析config
            self.db = pymysql.connect(**config)
            # create cursor
            self.cursor = self.db.cursor()
            print("Connect DB successfully!")
        except ConnectionError as ex:
            print("数据库配置文件报错")
            # self.logger.error(str(ex))

    def executeSQL(self, sql):
        # self.connectDB()
        # executing sql
        self.cursor.execute(sql)
        # executing by committing to DB
        self.db.commit()
        return self.cursor

    def get_all(self, cursor):
        value = cursor.fetchall()
        return value

    def get_one(self, cursor):
        value = cursor.fetchone()
        return value

    def closeDB(self):
        self.db.close()
        print("Database closed!")

if __name__== '__main__':
    a = MyDB()
    print("第一遍")
    a.connectDB()
    cursor = a.executeSQL("SELECT  t.`principal_interest_biz_bill_no` FROM  `t_loan_order` t  "
                 "LEFT JOIN `t_loan_order_payment_apply_bill` t1    "
                 "ON t.`business_order_id` = t1.`business_order_id` "
                 "WHERE t.`status` = 9  "
                 "AND t.`audit_status` !=2 "
                 "AND t1.`sys_flag`=0 "
                 "AND t.`principal_interest_biz_bill_no` IS NOT NULL "
                 "GROUP BY t.`principal_interest_biz_bill_no`;")
    j = a.get_all(cursor)
    for i in  j :
        print(i[0])

    a.closeDB()