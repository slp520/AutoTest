# -*- coding:utf-8 -*-
import requests
import unittest


class AddOrderTest (unittest.TestCase):

    def setUp(self):
        #定义所有需要的URL链接
        self.base_url = "http://10.0.4.104:12008/ddxf/order"
        self.base_url_app_login = "http://10.0.4.104:12008/ddxf/user/login"
        self.base_url_shop_login = "http://10.0.4.104:9015/account/login.json"
        self.base_url_shop_login_code_apply = "http://10.0.4.104:9015/account/gen_identify_code_image.json"
        self.base_url_shop_login_code = "http://10.0.4.104:9015/account/query_identity_code.json"
        self.case_name = " "
        self.iphone = "13333336666"
        #登录多多新房APP
        self.body_data2 = {"password": "Fdd123@@", "username": "新体验项目助理"}
        login = requests.post (self.base_url_app_login, json=self.body_data2)
        #获取后台返回的token
        a = login.json()['data']
        token = a['token']
        #定义请求参数
        self.body_data = {"projectId": 14673, "predictTime": 1540262437000, "custMobile": self.iphone, "houseId": 54608,
                          "dealStatus": 2, "orderTime": 1540262437000, "pageSize": 10, "pageNo": 0, "packageId": 501432,
                          "contractArea": "66", "custName": "李四", "contractAmount": 20000000, "salesAmount": 10000000,
                          "orderAttachmentInput": {"otherUrls": [], "custIdCardImgUrls": [],
                                                   "subcribeReceiptImgUrls": [],
                                                   "subcribeImgUrls": [
                                                       "https://fsupload.fangdd.net/image/pIorj4aQ-WnzaNlP7H6dOQNovM.jpg"]
                                                   }
                          }
        self.head = {"Content-Type": "application/json",
                     "version": "4.0.4",
                     "apiVersion": "4.0.4",
                     "platform": "iOS",
                     "deviceId": "A3D2498C-E831-4CCF-BC08-964CE5F0D9EF",
                     "platformVersion": "11.4",
                     "token": token,
                     "userId": "408899",
                     "ocUserId": "408899"
                     }

    def test_add_order(self):
        #录入订单操作
        r = requests.post (self.base_url, json=self.body_data, headers=self.head)
        result = r.json ()
        #获取录入成功后的订单ID
        i = result['data']
        orderId = i['orderId']
        print(orderId)
        #返回订单ID
        return orderId


