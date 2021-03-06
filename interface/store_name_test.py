import unittest
import requests

#门店信息接口校验
class GetStoreTest(unittest.TestCase):


    def setUp(self):
        self.base_url = "http://10.0.4.66:61020/api/common/stores"
        self.case_name = ''

    def test_get_store_name_null(self):
        '''name参数为空'''
        r = requests.get(self.base_url,params={'storeName':'' })
        result = r.json()
        print(result)
        self.assertEqual(result['code'],0)
        self.assertEqual(result['msg'],'成功')

    def test_get_store_name(self):
        '''name不为空'''
        r = requests.get(self.base_url,params={'storetName':'上海暨邦房地产咨询有限公司'})
        result = r.json()
        print (result)
        self.assertEqual (result['code'], 0)
        self.assertEqual (result['msg'], '成功')

    def test_get_nostore_name(self):
        '''无参数校验'''
        r = requests.get(self.base_url)
        result = r.json()
        print (result)
        self.assertEqual (result['code'], 0)
        self.assertEqual (result['msg'], '成功')

if __name__ == '__main__':
    unittest.main