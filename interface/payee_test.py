import unittest
import requests

#测试收款方信息接口
class GetPayeeTest(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://10.0.4.66:61020/api/common/enterprises"
        self.case_name= ''


    def test_get_payee_null(self):
        '''payee参数为空'''
        r = requests.get(self.base_url,params={'payee':'' })
        result = r.json()
        print(result)
        self.assertEqual(result['code'],0)
        self.assertEqual(result['msg'],'成功')

    def test_get_payee(self):
        '''payee不为空'''
        r = requests.get(self.base_url,params={'enterpriseName':'罗媛测试公司'})
        result = r.json()
        print(result)
        self.assertEqual (result['code'], 0)
        self.assertEqual (result['msg'], '成功')

    def test_get_payee_noparams(self):
        '''payeew无参数case'''
        r = requests.get(self.base_url)
        result = r.json()
        print(result)
        self.assertEqual(result['code'],0)
        self.assertEqual(result['msg'],'成功')

    def test_get_payee_wrong(self):
        '''payee参数错误'''
        r = requests.get(self.base_url,params={'payee':'qewwqeew' })
        result = r.json()
        print(result)
        self.assertEqual(result['code'],0)
        self.assertEqual(result['msg'],'成功')

if __name__ == '__main__':
    unittest.main



