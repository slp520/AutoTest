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


    def test_login_shop(self):
        # 点击验证码
        test_session = requests.session ()
        r = test_session.get(self.base_url_shop_login_code_apply)

        # 获取验证码
        picture_code = test_session.get(self.base_url_shop_login_code)

        result = picture_code.json ()
        print(result)
        code =  result['data']
        print(code)
        self.body_data = {
            "username":"新体验项目助理",
            "password": "Fdd123@@",
            "identifyCode": str(code) ,
            "keep": 1
        }
        r2 = test_session.post(self.base_url_shop_login,data=self.body_data)
        result = r2.json()
        print(result)
        return test_session

if __name__ =="__main__":
    unittest.main


