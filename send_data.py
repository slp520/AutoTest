#!/usr/bin/python
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email import encoders
import pymysql
from sshtunnel import SSHTunnelForwarder
import xlwt
import os



class SendEveryDay:
    def sendemail(self, file_new):
        sender = 'jrfdd@fangdd.com'
        email_list = ['sunlinpeng@fangdd.com', 'huangwenquan@fangdd.com','gaoyufeng@fangdd.com']
        receiver = email_list
        mail_host = '10.50.50.66'
        username = "jrfdd@fangdd.com"
        password = "Jinrong@123"
        msg = MIMEMultipart ('related')
        msg['From'] = 'Tom<jrfdd@fangdd.com>'
        msg['To'] = "sunlinpeng@fangdd.com,huangwenquan@fangdd.com,gaoyufeng@fangdd.com"
        subject = '每日准入信息日报推送'
        msg['Subject'] = Header (subject, 'utf-8')

        # 构造正文
        # fp2 = open(file_new,'r',encoding="utf-8")
        # htmlcont = fp2.read()
        # print(type(htmlcont))
        # fp2.close()
        # msg.attach (MIMEText(htmlcont, 'html','utf-8'))
        msg.attach (MIMEText ('待准入日报详情，请查看附件!', 'plain', 'utf-8'))

        # 构造附件
        basename = os.path.basename (file_new)
        fp = open (file_new, 'rb')
        att = MIMEText (fp.read (), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att.add_header ('Content-Disposition', 'attachment', filename=('gbk', '', basename))
        encoders.encode_base64 (att)
        msg.attach (att)

        try:
            smtp = smtplib.SMTP ()
            smtp.connect (mail_host,port=587)
            smtp.login (username, password)
            smtp.sendmail (sender, receiver, msg.as_string ())
            smtp.quit ()
            print ("邮件发送成功")
        except smtplib.SMTPException as e:
            print (e)

    def get_data(self):
        self.server = SSHTunnelForwarder (
            ssh_address_or_host=('10.50.110.11', 22),
            ssh_username='sunlinpeng',
            ssh_password='1qaz@WSXpeng',
            remote_bind_address=('10.50.10.44', 3306)
        )
        # 启动服务
        self.server.start ()
        self.config = {
            'host': "10.50.10.44",
            'user': "xf_tc_s",
            'passwd': "bJytvVs2XxbR",
            'port': 3306,
            'db': "fdd_xfbp_commission"
        }

        # connect to DB 解析config
        self.db = pymysql.connect (host="127.0.0.1",
                                   user="xf_tc_s",
                                   passwd="bJytvVs2XxbR",
                                   port=self.server.local_bind_port,
                                   db="fdd_xfbp_commission")
        # create cursor
        self.cursor = self.db.cursor ()
        print ("Connect DB successfully!")

    def executeSQL(self, sql):
        # self.connectDB()
        # executing sql
        self.cursor.execute (sql)
        # executing by committing to DB
        self.db.commit ()
        return self.cursor

    def get_all(self, cursor):
        value = cursor.fetchall ()
        return value

    def get_one(self, cursor):
        value = cursor.fetchone ()
        return value

    def closeDB(self):
        self.db.close ()
        print ("Database closed!")

    def write_data(self, list):
        # 新建一个excel
        book = xlwt.Workbook ()
        # 添加一个sheet页
        sheet = book.add_sheet ("待准入情况日报")
        sheet.write (0, 0, "节点")
        sheet.write (0, 1, "branch_name")
        sheet.write (0, 2, "审核订单笔数")
        sheet.write (0, 3, "项目数")
        sheet.write (0, 4, "金额（分）")
        sheet.write (0, 5, "审核佣金笔数")
        row = 1
        for i in list:
            col = 0
            for j in i:
                sheet.write (row, col, j)
                col += 1
            row += 1
        if os.path.exists("待准入情况日报.xls") is True:
            os.remove ("待准入情况日报.xls")
        book.save ("待准入情况日报.xls")


if __name__ == '__main__':
    a = SendEveryDay ()
    a.get_data ()
    mysql = a.executeSQL (
        "SELECT IF(    t.`current_flow_node` = 'carrierFactoringSpecialistAudit',   '业务风控',    '金融风控'  ) AS '节点',  t1.`branch_name`,  COUNT(DISTINCT t.`order_id`) AS '审核订单笔数',  COUNT(DISTINCT t.`project_id`) AS '项目数',  SUM(t.`commission_amount`) AS '金额（分）',  COUNT(1)  AS '审核佣金笔数' FROM  `fdd_xfbp_commission`.`commission_factoring_detail` t   LEFT JOIN `fdd_xfbp_organization`.`org_branch` t1  ON t.`org_id` = t1.`branch_id` WHERE t.`current_flow_node` IN (    'carrierFactoringSpecialistAudit',    'financialRiskAudit'  )  AND t.`audit_status` = 0  AND t.`is_deleted` = 0  AND t.`org_id` <> 3 GROUP BY t.`current_flow_node`,  t.`org_id`; ")
    list = a.get_all (mysql)
    print (list)
    a.write_data (list)
    a.closeDB ()
    a.server.close ()
    file_new = "待准入情况日报.xls"
    a.sendemail (file_new)

