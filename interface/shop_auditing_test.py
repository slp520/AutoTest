import requests
import unittest
from common.common_login import Login

#获取经纪门店信息接口测试
class GetShopTest(unittest.TestCase):

    def setUp(self):

        self.base_url = "http://10.12.21.115:61021/jgj/api/factoring/queryStoreAuditing?pageIndex=1"
        self.case_name = " "
        a = Login ()
        self.b = a.get_session ()

    def test_shop_info(self):
        '''正常传参测试'''
        r = self.b.get(self.base_url,params={"storeId":"80145602"})
        result = r.json()
        print(result)
        self.assertEqual(result['code'],0)
        self.assertEqual(result['msg'],'成功')

    def test_shop_info_noparams(self):
        '''不传参测试'''
        r = self.b.get(self.base_url)
        result = r.json()
        print(result)
        self.assertEqual(result['code'],0)
        self.assertEqual(result['msg'],'成功')



if __name__ == '__main__':
    unittest.main