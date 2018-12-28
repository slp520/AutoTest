import requests
import unittest
from common.common_sql_execution import SqlExecution

#还款单付款流程接口测试
class PayTest (unittest.TestCase):

    def setUp(self):

        # 获取当前待生成还款单的请用单号
        self.a = SqlExecution ()
        i = self.a.get_value (
            "SELECT t.`payment_id` FROM `fdd_finance_operation_server`.`t_payment` t  WHERE  t.payment_status=0 AND t.`fee_type`=1;")
        self.body_data = {"paymentId": str(i),
                          "userId": 6,
                          "userName": "小木鸟",
                          "paymentChannel":90,
                          "paymentType": 1,
                          "paymentMethod": 1,
                          "paymentAccount": "12323213",
                          "paymentAccountName": "小木鸟银行",
                          "paymentBank": "小木鸟支行",
                          "referenceNo": "12321321123"
                          }
        paymentId = i
        self.base_url = "http://10.0.4.66:61020/api/payments/" + str(paymentId) + "/payAction"
        self.case_name = ""

    def test_pay(self):
        '''正常付款成功接口测试'''
        r = requests.post (self.base_url, data=self.body_data)
        result = r.json ()
        print (result)
        self.assertEqual(result["code"],0)
        self.assertEqual(result["msg"],"成功")

    def test_pay_nodata(self):
        '''付款无参数传输接口测试'''
        r = requests.post (self.base_url)
        result = r.json ()
        print (result)
        self.assertEqual(result["code"],-2)
        self.assertEqual(result["msg"],"参数校验有误")

if __name__ == "__main__":
    unittest.main