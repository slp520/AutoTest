import requests
import unittest

#佣金基本信息查看接口测试
class GetCommisoinTest(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://10.0.4.66:61020/api/commission/"
        self.case_name = " "

    def test_commision_info(self):
        '''带佣金ID参数case'''
        programId = "2125441"
        r = requests.get(self.base_url+programId)
        result = r.json()
        print(result)
        self.assertEqual(result["code"],0)
        self.assertEqual(result["msg"],'成功')

    def test_commision_noID(self):
        '''无佣金ID参数case'''
        programId = " "
        r = requests.get(self.base_url+programId)
        result = r.json()
        print(result)
        self.assertEqual(result["code"],400)
        self.assertEqual(result["msg"],'Value for programId cannot be null')

    def test_commision_others(self):
        '''佣金ID参数其他字符case'''
        programId = "QWWAS"
        r = requests.get (self.base_url + programId)
        result = r.json ()
        print (result)
        self.assertEqual (result["code"], 400)
        self.assertEqual (result["msg"], 'Failed to convert value of type \'java.lang.String\' to required type \'java.lang.Long\'; nested exception is java.lang.NumberFormatException: For input string: "QWWAS"')

if __name__ == "__main__":
    unittest.main