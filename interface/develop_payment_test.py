# -*- coding:utf-8 -*-
import unittest
from interface.shop_login_test import ShopLoginTest
import warnings


# 开发商回款接口
class DevelopPaymentOrderTest (unittest.TestCase):

    def setUp(self):
        # 定义所有需要的URL链接
        self.base_url = "http://10.0.4.104:12010/pc/receipt/ticket"
        self.base_url_confirm = "http://10.0.4.104:12010/pc/receipt/ticket/status"
        # 配置回款金额
        self.orderId = 1491737
        self.actualAmount = 70000
        self.receiptAmount = 70000
        self.case_name = " "
        warnings.simplefilter ("ignore", ResourceWarning)
        # 调用登录方法，获取登录session
        self.a = ShopLoginTest ()
        self.a.setUp ()
        self.testsession = self.a.login_shop ()
        # 定义请求参数
        self.body_data = {"orgId": 3, "estateId": 54608,
                          "ticketAttaches": ["https://fsxf.fangdd.com/xf/FjHGYbva-qzx0W86tGX3AQ2aYCGL.jpg"],
                          "ticketType": 0, "receiptWay": "4", "payerType": "2", "paymentDirection": "0", "receiptAmount"
                          : self.receiptAmount, "paymentTime": 1545464886943, "ticketDetails": [
                {"orderType": 2, "receiptType": "2", "orderId": self.orderId, "actualAmount": self.actualAmount}]
                          }

    def develop_payment_apply(self):
        '''开发商回款'''
        self.r = self.testsession.post (self.base_url, json=self.body_data)
        self.result = self.r.json ()
        self.devticketId = self.result['data']
        print (self.devticketId)
        return self.devticketId

    def test_devrlop_payment_confirm(self):
        '''确认开发商回款操作'''
        self.body_confirm = {"ticketId": self.develop_payment_apply(), "ticketStatus": 2, "receiptAmount": self.receiptAmount,
                                  "ticketAttaches": ["https://fsxf.fangdd.com/xf/Fn4ZXoTrnMHpNS6PeobCEpefGoec.png"],
                                  "ticketInvoices": [],
                                  "ticketNote": ""}
        self.r2 = self.testsession.put (self.base_url_confirm,json=self.body_confirm)
        self.result = self.r2.json ()
        print (self.result)
        self.assertEqual(self.result['code'],200)


if __name__ == '__main__':
    unittest.mian
