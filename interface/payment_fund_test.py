import requests
import unittest
from common.common_sql_execution import SqlExecution


# 资金渠道还款单生成接口测试
class PaymentFundTest (unittest.TestCase):

    def setUp(self):
        self.base_url = "http://10.0.4.66:61020/api/factoring/payment/apply/bill/creation"
        self.case_name = ""
        #获取当前待生成还款单的请用单号
        self.a = SqlExecution ()
        i = self.a.get_value (
            "SELECT t.`business_order_id` FROM `t_loan_order` t WHERE t.`status`=3 AND t.`sys_flag`=0 AND t.`channel_id` != 4 AND t.`business_order_id` IS NOT NULL;")
        list = []
        list.append (i)
        #参数
        self.body_data = {"businessOrderIdList": list,
                          "billType": 1,
                          "userId": 6,
                          "operatorName": "小木鸟"
                          }

        self.body_nobusinessOrderIdList = {"billType": 1,
                                           "userId": 6,
                                           "operatorName": "小木鸟"
                                           }
        self.body_nobillType = {"businessOrderIdList": list,
                                "userId": 6,
                                "operatorName": "小木鸟"
                                }
        self.body_nooperatorName = {"businessOrderIdList": list,
                                    "billType": 1,
                                    "userId": 6
                                    }
        self.header = {"content-type": "application/json"}

    def test_payment_fund(self):
        '''正常传参流程验证'''
        r = requests.post (self.base_url, json=self.body_data)
        result = r.json ()
        print (result)
        self.assertEqual (result["code"], 0)

    def test_payment_fund_nobusinessorderid(self):
        '''不传请佣单号流程验证'''
        r = requests.post (self.base_url, json=self.body_nobusinessOrderIdList)
        result = r.json ()
        print (result)
        self.assertEqual (result["code"], -2)
        self.assertEqual (result["msg"], "请佣单号不能为空")

    def test_payment_fund_nobilltype(self):
        '''不传业务类型号流程验证'''
        r = requests.post (self.base_url, json=self.body_nobillType)
        result = r.json ()
        print (result)
        self.assertEqual (result["code"], -2)
        self.assertEqual (result["msg"], "单据类型不能为空")

    def test_payment_fund_nooperatorname(self):
        '''不传操作人姓名流程验证'''
        r = requests.post (self.base_url, json=self.body_nooperatorName)
        result = r.json ()
        print (result)
        self.assertEqual (result["code"], -2)
        self.assertEqual (result["msg"], "操作人名称不能为空")

    def test_payment_fund_nojson(self):
        '''不传参流程验证'''
        r = requests.post (self.base_url)
        result = r.json ()
        print (result)
        self.assertEqual (result["code"], 400)


if __name__ == "__main__":
    unittest.main
