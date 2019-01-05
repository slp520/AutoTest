import requests
import unittest
from time import sleep

class ShopLoginTest (unittest.TestCase):

    def setUp(self):
        # 定义所有需要的URL链接
        self.base_url_shop_login = "http://10.0.4.104:9015/account/login.json"
        self.base_url_shop_login_code_apply = "http://10.0.4.104:9015/account/gen_identify_code_image.json"
        self.base_url_shop_login_code = "http://10.0.4.104:9015/account/query_identity_code.json"
        self.case_name = " "


    def login_shop(self):
        # 点击验证码
        self.test_session = requests.session ()
        self.r = self.test_session.get(self.base_url_shop_login_code_apply)

        # 获取验证码
        self.picture_code = self.test_session.get(self.base_url_shop_login_code)

        self.result = self.picture_code.json ()
        print(self.result)
        self.code =  self.result['data']
        print(self.code)
        self.body_data = {
            "username":"新体验项目助理",
            "password": "Fdd123@@",
            "identifyCode": str(self.code) ,
            "keep": 1
        }
        self.r2 = self.test_session.post(self.base_url_shop_login,data=self.body_data)
        self.result = self.r2.json()
        print(self.result)
        return self.test_session

if __name__ =="__main__":
    unittest.main


