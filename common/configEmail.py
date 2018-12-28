#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
from email import encoders
import base64
import readConfig as readConfig

#实例化一个参数
localReadConfig = readConfig.ReadConfig()
global mail_host,username,password,sender,receiver
#读取配置文件中的值
mail_host = localReadConfig.get_email("mail_host")
username = localReadConfig.get_email("mail_user")
password = localReadConfig.get_email("mail_pass")
sender = localReadConfig.get_email("sender")
value = localReadConfig.get_email ("receiver")
receiver = []
# get receiver list
for n in str (value).split ("/"):
    receiver.append (n)

def sendemail(file_new):
    # sender='13058019302@163.com'
    # email_list=['sunlinpeng@fangdd.com','339403375@qq.com']
    # receiver= email_list
    # mail_host='smtp.163.com'
    # username="13058019302@163.com"
    # password="520ainiyiwan"
    msg=MIMEMultipart('related')
    msg['From']='Tom<13058019302@163.com>'
    msg['To']="sunlinpeng@fangdd.com,339403375@qq.com"
    subject='接口自动化测试反馈'
    msg['Subject']=Header(subject,'utf-8')

    #构造正文
    # fp2 = open(file_new,'r',encoding="utf-8")
    # htmlcont = fp2.read()
    # print(type(htmlcont))
    # fp2.close()
    # msg.attach (MIMEText(htmlcont, 'html','utf-8'))
    msg.attach (MIMEText ('测试报告详情请查看附件!', 'plain', 'utf-8'))


    #构造附件
    basename = os.path.basename (file_new)
    fp=open(file_new,'rb')
    att = MIMEText(fp.read(),'base64','utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att.add_header('Content-Disposition', 'attachment', filename=('gbk', '', basename))
    encoders.encode_base64(att)
    msg.attach(att)

    try:
        smtp=smtplib.SMTP()
        smtp.connect(mail_host)
        smtp.login(username,password)
        smtp.sendmail(sender,receiver,msg.as_string())
        smtp.quit()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error:无法发送邮件！")

if __name__ == '__main__':
    # file_new = "C:\\Users\\33940\\Desktop\\bug统计.xlsx"
    print('这里不走才对的！！！')
    sendemail('C:\\Users\\33940\\Desktop\\bug.xlsx')
