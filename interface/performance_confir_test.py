import unittest
import requests
from interface.shop_login_test import ShopLoginTest
from interface.add_order_test import AddOrderTest
import warnings


# 业绩确认接口
class PerformanceConfirTest (unittest.TestCase):

    def setUp(self):
        self.apply_url = "http://10.0.4.104:12010/pc/purchase/confirm/add"
        self.confir_url = "http://10.0.4.104:12010/pc/purchase/confirm/approve"
        self.case_name = " "
        warnings.simplefilter ("ignore", ResourceWarning)

        # 调用登录方法，获取登录session
        self.a = ShopLoginTest ()
        self.a.setUp ()
        self.testsession = self.a.login_shop ()


    def performance_confir_apply(self):
        '''业绩确认申请'''
        # 调用订单ID方法，获取订单ID
        self.i = AddOrderTest ()
        self.i.setUp ()
        self.orderId = self.i.add_order ()
        print (self.orderId)
        # 定义参数
        self.apply_data = {"estateId": 54608, "orgId": 3,
                           "confirmUrls": ["https://fsxf.fangdd.com/xf/FodYak5jNF0ayLYIfPIdrgsOre3f.png"],
                           "applyCompany": "深圳市房多多网络科技有限公司", "developCompany": "1231212",
                           "cooperateStartTime": 1544444044707, "cooperateEndTime": 1546172047096,
                           "authorizer": "123123", "developerAuthorizedPerson": "132312",
                           "orderList": [{"orderId": self.orderId, "projectId": 14673}]}
        self.r = self.testsession.post (self.apply_url, json=self.apply_data)
        self.result = self.r.json ()
        print (self.result)
        self.confirmId = self.result['data']
        return self.confirmId

    def test_performance_confir(self):
        '''业绩确认审核'''
        self.confir_data = {"confirmId": self.performance_confir_apply(), "confirmStatus": 1, "confirmNote": "小木鸟业绩确认操作",
                            "confirmStandard": "1"}
        r = self.testsession.post (self.confir_url, json=self.confir_data)
        result = r.json ()
        print (result)
        self.assertEqual(result['code'],200)
        self.assertEqual(result['success'],True)

