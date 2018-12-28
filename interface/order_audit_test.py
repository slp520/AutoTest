import unittest
import requests
from common.common_sql_execution import SqlExecution


# 商户门店信息审核接口测试
class OrderAuditTest (unittest.TestCase):

    def setUp(self):
        self.base_url = "http://10.0.4.66:61020/api/order/apply/acceptance"
        self.case_name = " "
        self.a = SqlExecution ()
        i = self.a.get_value (
            "SELECT t.`program_id` FROM `t_order_apply` t WHERE t.`audit_status`=0 AND t.`sys_flag`=0 AND t.`channel_id`IS NULL;")


        print(i)
        self.body_data = {"programId": i,
                          "userId": 6,
                          "operatorName": "小木鸟",
                          "channelId": 4,
                          "remark":"接口测试自动审核"

                          }
        self.body_nodata = {
                          "userId": 6,
                          "operatorName": "小木鸟",
                          "channelId": 4,
                          "remark":"接口测试自动审核"

                          }

        self.body_nouserId = {"programId": i,
                          "operatorName": "小木鸟",
                          "channelId": 4,
                          "remark":"接口测试自动审核"

                          }


    def test_order_audit(self):
        '''门店审核正常流程测试'''
        r = requests.patch (self.base_url, data=self.body_data)
        result = r.json ()
        print(result)
        self.assertEqual(result["code"],0)
        self.assertEqual(result["msg"],"成功")

    def test_Order_audit_nodata(self):
        '''无参数流程测试'''
        r = requests.patch (self.base_url)
        result = r.json ()
        print (result)
        self.assertEqual (result["code"], -2)
        self.assertEqual (result["msg"], "参数校验有误")

    def test_Order_audit_noOrderid(self):
        '''无门店ID流程测试'''
        r = requests.patch (self.base_url,data=self.body_nodata)
        result = r.json ()
        print (result)
        self.assertEqual (result["code"], -2)
        self.assertEqual (result["msg"], "参数校验有误")

    def test_Order_audit_nouserId(self):
        '''无操作人ID流程测试'''
        r = requests.patch (self.base_url,data=self.body_nouserId)
        result = r.json ()
        print (result)
        self.assertEqual (result["code"], -2)
        self.assertEqual (result["msg"], "参数校验有误")

if __name__=="__main__":
    unittest.main