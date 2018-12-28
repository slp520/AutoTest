import unittest
import requests
from interface.shop_login_test import ShopLoginTest
from interface.add_order_test import AddOrderTest


class PerformanceConfirTest (unittest.TestCase):

    def setUp(self):
        self.apply_url = "http://10.0.4.104:12010/pc/purchase/confirm/add "
        self.confir_url = "http://10.0.4.104:12010/pc/purchase/confirm/approve "
        self.case_name = " "
        # # 调用订单ID方法，获取订单ID
        # self.i = AddOrderTest ()
        # self.i.setUp ()
        # self.orderId = self.i.test_add_order ()
        # print (self.orderId)
        # 调用登录方法，获取登录session
        self.a = ShopLoginTest ()
        self.a.setUp ()
        self.testsession = self.a.test_login_shop ()
        # 定义参数
        self.head = {
            "userloginorgid": 3,
            "userloginuserid": 408899
        }
        self.apply_data = {"estateId": 54608, "orgId": 3,
                           "confirmUrls": ["https://fsxf.fangdd.com/xf/FodYak5jNF0ayLYIfPIdrgsOre3f.png"],
                           "applyCompany": "深圳市房多多网络科技有限公司", "developCompany": "1231212",
                           "cooperateStartTime": 1544444044707, "cooperateEndTime": 1546172047096,
                           "authorizer": "123123", "developerAuthorizedPerson": "132312",
                           "orderList": [{"orderId": 1491676, "projectId": 14673}]}
        self.confir_data = {"confirmId": 12332, "confirmStatus": 1, "confirmNote": "6777777", "confirmStandard": "1"}

    def test_performance_confir_apply(self):
        '''业绩确认申请'''
        r = self.testsession.post (self.apply_url, json=self.apply_data,headers=self.head)
        result = r.json ()
        print (result)

    # def test_performance_confir(self):
    #     '''业绩确认审核'''
    #     r = self.testsession.post (self.confir_url)
