import unittest
import requests


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

    def test_get_psyee(self):
        '''payee不为空'''
        r = requests.get(self.base_url,params={'enterpriseName':'罗媛测试公司'})
        result = r.json()
        print(result)
        self.assertEqual (result['code'], 0)
        self.assertEqual (result['msg'], '成功')

if __name__ == '__main__':
    unittest.main