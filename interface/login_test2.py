import requests
import unittest
import json

class GetLoginTest(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://10.12.21.115:61021/jgj/api/user/login'
        self.smg_url = 'http://10.12.21.115:61021/jgj/api/user/smgsend'
        self.case_name = ''


    def test_login(self):
        '''登录正常流程校验'''
        body_login ={"captcha":"1234",
                "mobile":"13058019302",
                "password":"BxOqKRgGgnfbQp6kLhIdm8jlbMIT8xcK/WpFx0CzJIeSQHyhjrGjSGf4FmMlZ2pdJn9HgirwlClcKf1aHjPSAd9SkSe9Nztkk10L9G6aUDL84e1zKMjXRoeF3g3inkNtBZfkf8YYFUDdTydDulKNpIQRpZuHu83NnG7isr57tkBwg9/fVPIG6P7Irf/35TcH9/s2NeV7hyBCWuDn4Zt6ueaSVjdfJ8u6iklkaqsNpwLDizKPoqoNnaDc/MWGj4zlnqdJJpAxQroRZ8+1AMbsY6bpQTCyI7gQNoq4BCOfz/owRZNEUaaRi/cSMcMUKiJoDWUl/MBnFKx1QSxjGbsQLQ=="
}
        body_smg = {
            "mobile":"13058019302",
            "type":"1"
        }
        header = {}
        r_smg = requests.post(self.smg_url,data=body_smg,headers=header)
        r = requests.post(self.base_url,data=body_login,headers=header)
        result = r.text
        print(result)
        self.assertEqual(result['code'],200)
        self.assertEqual(result['msg'],'一切正确，没有错误发生')

if __name__ == '__main__':
    unittest.main