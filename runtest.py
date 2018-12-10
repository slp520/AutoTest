#coding=utf-8
import time
import HTMLTestRunner
import unittest
import os
from send_email import sendemail

# def send_mail(file_new):
#     sender = '13058019302@163.com'
#     email_list = ['sunlinpeng@fangdd.com', '339403375@qq.com']
#     receiver = email_list
#     mail_host = 'smtp.163.com'
#     username = "13058019302@163.com"
#     password = "520ainiyiwan"
#
#     msg = MIMEMultipart ('related')
#     msg.attach (MIMEText ('日报详情请查看附件!', 'plain', 'utf-8'))
#     msg['From'] = '13058019302@163.com'
#     msg['To'] = ['sunlinpeng@fangdd.com', '339403375@qq.com']
#     subject = '日报'
#     msg['Subject'] = Header (subject, 'utf-8')
#
#     # 构造附件
#     basename = os.path.basename (file_new)
#     fp = open (file_new, 'rb')
#     att = MIMEText (fp.read (), 'base64', 'utf-8')
#     att["Content-Type"] = 'application/octet-stream'
#     att.add_header ('Content-Disposition', 'attachment', filename=('gbk', '', basename))
#     encoders.encode_base64 (att)
#     msg.attach (att)
#     # #定义正文
#     # f = open(file_new, 'rb')
#     # mail_body = f.read()
#     # f.close()
#     # msg=MIMEText(mail_body,_subtype='html',_charset='utf-8')
#     # #定义标题
#     # msg['Subject']=u"自动化报告"
#     # #定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
#     # msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
#
#     # try:
#     smtp=smtplib.SMTP()
#     smtp.connect('smtp.163.com')
#     smtp.login(username,password)
#     smtp.sendmail(sender,receiver,msg.as_string())
#     smtp.quit()
#     print("邮件发送成功")
#     # except smtplib.SMTPException:
#     #     print("Error:无法发送邮件！")


#======查找测试报告目录，找到最新生成的测试报告文件====
def send_report(testreport):
    result_dir = testreport
    lists = os.listdir (result_dir)
    lists.sort (key=lambda fn: os.path.getmtime (result_dir + "\\" + fn))
    # print (u'最新测试生成的报告： '+lists[-1])
    # 找到最新生成的文件
    file_new = os.path.join (result_dir, lists[-1])
    print(file_new)
    # 调用发邮件模块
    sendemail(file_new)

#================将用例添加到测试套件===========
def creatsuite():
    testunit = unittest.TestSuite()
    # 定义测试文件查找的目录
    test_dir = './interface'
    # 定义测试文件查找的目录
    discover = unittest.defaultTestLoader.discover (test_dir, pattern='*_test.py',top_level_dir=None)
    print(discover)
    # discover 方法筛选出来的用例，循环添加到测试套件中
    for test_case in discover:
        testunit.addTests(test_case)
    return testunit
    print(testunit)



if __name__ == "__main__":
    now = time.strftime ("%Y-%m-%d %H_%M_%S")
    testreport = 'D:\\AutoTest\\report\\'
    filename = testreport + now + '_result.html'
    fp = open (filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner (stream=fp, title=u'自动化报告', description=u'用例执行情况：')

    alltestnames = creatsuite ()
    runner.run (alltestnames)
    fp.close ()
    send_report(testreport)