# -*- coding:utf-8 -*-
import requests
import unittest
from common.common_sql_execution import SqlExecution
from interface.add_order_test import AddOrderTest


# 订单准入审核接口
class AuditOrderTest (unittest.TestCase):

    def setUp(self):
        # 定义所有需要的URL链接
        self.base_url = "http://10.0.4.104:12008/ddxf/work/audit"
        self.case_name = " "
        # 获取订单Id
        # self.i = AddOrderTest ()
        # self.orderId = self.i.add_order ()
        #
        # # 获取佣金申请ID
        # self.a = SqlExecution()
        # self.businessId = self.a.get_value (
        #     "SELECT t.`apply_id` FROM `fdd_xfbp_factoring`.`commission_factoring` t WHERE t.`order_id`=%s" %self.orderId)
        #配置申请ID
        self.businessId = 300484
        # 定义请求参数
        self.body_data = {"remark": "小木鸟审核通过！", "auditStatus": 1, "processType": 17, "businessId": self.businessId, "pageNo": 0,
                          "pageSize": 10}

    def test_audit_order(self):
        '''订单准入审核'''
        self.body_data2 = {"password": "Fdd123@@", "username": "新体验项目助理"}
        self.base_url_app_login = "http://10.0.4.104:12008/ddxf/user/login"
        self.login = requests.post (self.base_url_app_login, json=self.body_data2)
        # 获取后台返回的token
        self.a = self.login.json ()['data']
        self.token = self.a['token']
        self.head = {"Content-Type": "application/json",
                     "version": "4.0.4",
                     "apiVersion": "4.0.4",
                     "platform": "iOS",
                     "deviceId": "A3D2498C-E831-4CCF-BC08-964CE5F0D9EF",
                     "platformVersion": "11.4",
                     "token": self.token,
                     "userId": "408899",
                     "ocUserId": "408899"
                     }
        i=0
        while i<3:
            self.r = requests.post(self.base_url,json=self.body_data,headers=self.head)
            self.result = self.r.json()
            print(self.result)
            i+=1

if __name__ == '__main__':
    unittest.mian
