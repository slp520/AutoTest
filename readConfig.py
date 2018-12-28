import os
import codecs
import configparser

#当前目录
proDir = os.path.split(os.path.realpath(__file__))[0]
#在当前目录下加上配置文件的路径
configPath = os.path.join(proDir,"config.ini")


class ReadConfig:
    def __init__(self):
        fd = open(configPath)
        data = fd.read()


        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            print(data)
            file = codecs.open(configPath,"w")
            file.write(data)
            file.close()
        fd.close()
        #  实例化configParser对象
        self.cf = configparser.ConfigParser()

        #  读取config.ini文件
        self.cf.read(configPath)

    #  定义方法，获取config分组下指定name的值
    def get_email(self,name):
        value = self.cf.get("EMAIL",name)
        return value

    def get_http(self,name):
        value = self.cf.get("HTTP",name)
        return value

    def get_db(self,name):
        value = self.cf.get("DATABASE",name)
        return value
    def get_excel(self,name):
        value = self.cf.get("EXCEL",name)

if __name__ == '__main__':
    a = ReadConfig()
    a.__init__()
    a.get_email("mail_host")
