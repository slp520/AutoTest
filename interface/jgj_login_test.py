import requests
import unittest
import json

#登陆接口测试
class GetLoginTest(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://10.12.21.115:61021/jgj/api/user/login'
        self.smg_url = 'http://10.12.21.115:61021/jgj/api/user/smgsend'
        self.case_name = ''


    def test_login(self):
        '''登录正常流程校验'''
        body_login ={"captcha":"1234",
                "mobile":"13058019302",
                "password":"BxOqKRgGgnfbQp6kLhIdm8jlbMIT8xcK/WpFx0CzJIeSQHyhjrGjSGf4FmMlZ2pdJn9HgirwlClcKf1aHjPSAd9SkSe9Nztkk10L9G6aUDL84e1zKMjXRoeF3g3inkNtBZfkf8YYFUDdTydDulKNpIQRpZuHu83NnG7isr57tkBwg9/fVPIG6P7Irf/35TcH9/s2NeV7hyBCWuDn4Zt6ueaSVjdfJ8u6iklkaqsNpwLDizKPoqoNnaDc/MWGj4zlnqdJJpAxQroRZ8+1AMbsY6bpQTCyI7gQNoq4BCOfz/owRZNEUaaRi/cSMcMUKiJoDWUl/MBnFKx1QSxjGbsQLQ=="}
        body_smg = {
            "mobile":"13058019302",
            "type":"1"
        }
        header = {}
        r_smg = requests.post(self.smg_url,data=body_smg,headers=header)
        r = requests.post(self.base_url,data=body_login,headers=header)
        result = r.json()
        self.assertEqual(result['code'],'200')
        self.assertEqual(result['msg'],"一切正确，没有错误发生")

    def test_login_nomobile(self):
        '''登录手机号为空流程校验'''
        body_login = {"captcha": "1234",
                      "mobile": " ",
                      "password": "BxOqKRgGgnfbQp6kLhIdm8jlbMIT8xcK/WpFx0CzJIeSQHyhjrGjSGf4FmMlZ2pdJn9HgirwlClcKf1aHjPSAd9SkSe9Nztkk10L9G6aUDL84e1zKMjXRoeF3g3inkNtBZfkf8YYFUDdTydDulKNpIQRpZuHu83NnG7isr57tkBwg9/fVPIG6P7Irf/35TcH9/s2NeV7hyBCWuDn4Zt6ueaSVjdfJ8u6iklkaqsNpwLDizKPoqoNnaDc/MWGj4zlnqdJJpAxQroRZ8+1AMbsY6bpQTCyI7gQNoq4BCOfz/owRZNEUaaRi/cSMcMUKiJoDWUl/MBnFKx1QSxjGbsQLQ=="
                      }
        body_smg = {
            "mobile": "13058019302",
            "type": "1"
        }
        header = {}
        r_smg = requests.post (self.smg_url, data=body_smg, headers=header)
        r = requests.post (self.base_url, data=body_login, headers=header)
        result = r.json()
        print (result)
        self.assertEqual (result['code'], '40301')
        self.assertEqual (result['msg'], "参数缺失")



    def test_login_wrong_password(self):
        '''登录密码错误流程校验'''
        body_login = {"captcha": "1234",
                      "mobile": "13058019302",
                      "password": "Iz2vdNMIDMJHQVEYA6l+ULzwOwN/SVJXVLw+IMlZf7BeAHxZ5nSmMgC7dHPPxiksKq7qzzmoObEwtBFWeJrbH+TY7OSEEIuuFdB57NRFyvDTjSvufFHfOacqlMwIfuC5PYbqiyZmM9EiwDR+n8HF2shoFI0V0P+uiy+Taf0CD+qCcyFYQE7z49zOTYVjOm9kUfW88HNXlOBzlpsHTSJG1A8jOXCwglNGP1ZliXtiGd5tmB4W+E1HA4xU+xuoUO5hEXyqkM/kgXrUWHRDl7V/UROVsXo4aITpHon/ts5tlxdIqDytmIBgEV7dhCIOtpyux+uzCzohTV1p1vXMatOYhw=="
                      }
        body_smg = {
            "mobile": "13058019302",
            "type": "1"
        }
        header = {}
        r_smg = requests.post (self.smg_url, data=body_smg, headers=header)
        r = requests.post (self.base_url, data=body_login, headers=header)
        result = r.json()
        print (result)
        self.assertEqual (result['code'], '40352')
        self.assertEqual (result['msg'], "用户名或密码错误")

    def test_login_nocaptcha(self):
        '''登录验证码为空流程校验'''
        body_login = {"captcha": " ",
                      "mobile": "13058019302",
                      "password": "BxOqKRgGgnfbQp6kLhIdm8jlbMIT8xcK/WpFx0CzJIeSQHyhjrGjSGf4FmMlZ2pdJn9HgirwlClcKf1aHjPSAd9SkSe9Nztkk10L9G6aUDL84e1zKMjXRoeF3g3inkNtBZfkf8YYFUDdTydDulKNpIQRpZuHu83NnG7isr57tkBwg9/fVPIG6P7Irf/35TcH9/s2NeV7hyBCWuDn4Zt6ueaSVjdfJ8u6iklkaqsNpwLDizKPoqoNnaDc/MWGj4zlnqdJJpAxQroRZ8+1AMbsY6bpQTCyI7gQNoq4BCOfz/owRZNEUaaRi/cSMcMUKiJoDWUl/MBnFKx1QSxjGbsQLQ=="

                      }
        body_smg = {
            "mobile": "13058019302",
            "type": "1"
        }
        header = {}
        r_smg = requests.post (self.smg_url, data=body_smg, headers=header)
        r = requests.post (self.base_url, data=body_login, headers=header)
        result = r.json()
        print (result)
        self.assertEqual (result['code'], 40355)
        self.assertEqual (result['msg'], '验证码错误')

    def test_login_wrong_captcha(self):
        '''登录验证码错误流程校验'''
        body_login = {"captcha": "122122",
                      "mobile": "13058019302",
                      "password": "BxOqKRgGgnfbQp6kLhIdm8jlbMIT8xcK/WpFx0CzJIeSQHyhjrGjSGf4FmMlZ2pdJn9HgirwlClcKf1aHjPSAd9SkSe9Nztkk10L9G6aUDL84e1zKMjXRoeF3g3inkNtBZfkf8YYFUDdTydDulKNpIQRpZuHu83NnG7isr57tkBwg9/fVPIG6P7Irf/35TcH9/s2NeV7hyBCWuDn4Zt6ueaSVjdfJ8u6iklkaqsNpwLDizKPoqoNnaDc/MWGj4zlnqdJJpAxQroRZ8+1AMbsY6bpQTCyI7gQNoq4BCOfz/owRZNEUaaRi/cSMcMUKiJoDWUl/MBnFKx1QSxjGbsQLQ=="

                      }
        body_smg = {
            "mobile": "13058019302",
            "type": "1"
        }
        header = {}
        r_smg = requests.post (self.smg_url, data=body_smg, headers=header)
        r = requests.post (self.base_url, data=body_login, headers=header)
        result = r.json()
        print (result)
        self.assertEqual (result['code'], 40355)
        self.assertEqual (result['msg'], "验证码错误")


if __name__ == '__main__':
    print(11111111)