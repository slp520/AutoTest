from common.configDB import MyDB

#执行SQL查询结果接口
class SqlExecution:

    def get_value(self,mysql):
        data = MyDB ()
        global j, i
        data.connectDB ()
        # 获取当前节点为待金融风控审核的业务单据号
        cursor = data.executeSQL (mysql)
        j = data.get_all (cursor)
        list = []
        for a in j:
            list.append (a[0])
        i = list[0]
        return i
        data.closeDB ()