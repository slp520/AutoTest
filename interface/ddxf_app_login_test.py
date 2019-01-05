# -*- coding:utf-8 -*-
import requests
import unittest


# 多多新房登录接口
class DdxfLoginTest (unittest.TestCase):

    def setUp(self):
        # 定义所有需要的URL链接
        self.base_url_app_login = "http://10.0.4.104:12008/ddxf/user/login"
        self.case_name = " "

    def test_login_app(self):
        '''登录多多新房APP'''
        self.body_data2 = {"password": "Fdd123@@", "username": "新体验项目助理"}
        self.login = requests.post (self.base_url_app_login, json=self.body_data2)
        result = self.login.json()
        self.assertEqual(result['code'],200)
        # 获取后台返回的token
        self.a = self.login.json ()['data']
        self.token = self.a['token']
        return self.token




if __name__ == '__main__':
    unittest.mian
