# -*- coding:utf-8 -*-
import requests
import unittest
from interface.add_order_test import AddOrderTest

# 订单转签约接口
class OrderSigningTest (unittest.TestCase):

    def setUp(self):
        # 定义所有需要的URL链接
        self.base_url = "http://10.0.4.104:12008/ddxf/order"
        self.base_url_app_login = "http://10.0.4.104:12008/ddxf/user/login"
        self.i = AddOrderTest()
        self.i.setUp()
        self.orderId = self.i.add_order()
        self.base_url_signing = "http://10.0.4.104:12008/ddxf/order/deal/status/%s" % self.orderId
        self.case_name = " "

        # 定义请求参数
        self.body_data = {"password": "Fdd123@@", "username": "新体验项目助理"}

    def login_app(self):
        '''登录多多新房APP'''
        self.login = requests.post (self.base_url_app_login, json=self.body_data)
        # 获取后台返回的token
        self.a = self.login.json ()['data']
        self.token = self.a['token']
        return self.token

    def test_signing_test(self):
        '''签约操作流程'''
        self.head = {"Content-Type": "application/json",
                     "version": "4.0.4",
                     "apiVersion": "4.0.4",
                     "platform": "iOS",
                     "deviceId": "A3D2498C-E831-4CCF-BC08-964CE5F0D9EF",
                     "platformVersion": "11.4",
                     "token": self.login_app (),
                     "userId": "408899",
                     "ocUserId": "408899"
                     }

        self.body_data_signing = {"actionType": 2, "buildingNo": "A栋", "contractAmount": 20000000,
                                  "contractArea": "66.00", "eventTime": 1546072646199, "flatId": 125512,
                                  "houseId": 54608, "houseNo": "111", "houseResourceId": 33698,
                                  "orderAttachmentInput": {
                                      "contractImgUrls": ["https://fsupload.fangdd.net/image/U-ie650sSoCPrBNhhZs3RPvXIJY.jpg"],
                                      "custIdCardImgUrls": [], "otherUrls": [],
                                      "subcribeImgUrls": ["https://fsupload.fangdd.net/image/ipIorj4aQ-WnzaNlP7H6dOQNovM.jpg"],
                                      "subcribeReceiptImgUrls": [], "type": 20 },
                                  "orderNote": "小木鸟的签约操作", "packageId": 501438,"orderType":2,
                                  "predictTime": 1540224000000, "salesAmount": 10000000, "unitNo": "1227001"
                                  }
        self.r = requests.post (self.base_url_signing,json=self.body_data_signing,headers=self.head)
        result = self.r.json()
        print (result)
        self.assertEqual(result['code'],200)


if __name__ == '__main__':
    unittest.mian
