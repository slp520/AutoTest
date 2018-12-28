import unittest
import requests
from common.common_sql_execution import SqlExecution

#还款申请单审核操作接口测试
class PaymentApplyTest (unittest.TestCase):


    def setUp(self):
        self.base_url = "http://10.0.4.66:61020/api/factoring/payment/apply/audit/acceptance"
        self.case_name = " "
        self.a = SqlExecution()
        i = self.a.get_value("SELECT  t.`principal_interest_biz_bill_no` FROM  `t_loan_order` t  "
                 "LEFT JOIN `t_loan_order_payment_apply_bill` t1    "
                 "ON t.`business_order_id` = t1.`business_order_id` "
                 "WHERE t.`status` = 9  "
                 "AND t.`audit_status` !=2 "
                 "AND t1.`sys_flag`=0 "
                 "AND t.`principal_interest_biz_bill_no` IS NOT NULL "
                 "GROUP BY t.`principal_interest_biz_bill_no`;")

        self.body_data = {"bizBillNo": i,
                          "auditStatus": 3,
                          "userId": 6,
                          "operatorName": "小木鸟"
                          }

        self.body_wrong_data = {"bizBillNo": 0,
                          "auditStatus": 3,
                          "userId": 6,
                          "operatorName": "小木鸟"
                          }

    def test_payemnt_apply(self):
        '''付款申请单审核通过流程校验'''
        r = requests.patch (self.base_url, data=self.body_data)
        result = r.json ()
        print (result)
        self.assertEqual(result["code"],-2)
        self.assertEqual(result["msg"],"更新订单申请请佣状态失败")

    def test_payemnt_apply_noparams(self):
        '''付款申请单审核无参数校验'''
        r = requests.patch (self.base_url)
        result = r.json ()
        print (result)
        self.assertEqual(result["code"],-2)
        self.assertEqual(result["msg"],"参数校验有误")


    def test_payemnt_apply_wrongparams(self):
        '''付款申请单审核错误参数校验'''
        r = requests.patch (self.base_url,data=self.body_wrong_data)
        result = r.json ()
        print (result)
        self.assertEqual(result["code"],-1)
        self.assertEqual(result["msg"],"未查询到对应的付款申请单")


if __name__ == "__main__":
    unittest.main
