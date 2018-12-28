import requests

#cookie or session 登录方式
class Login:

    def __init__(self):
        self.base_url = 'http://10.12.21.115:61021/jgj/api/user/login'
        self.smg_url = 'http://10.12.21.115:61021/jgj/api/user/smgsend'
        self.body_login = {"captcha": "1234",
                      "mobile": "13058019302",
                      "password": "BxOqKRgGgnfbQp6kLhIdm8jlbMIT8xcK/WpFx0CzJIeSQHyhjrGjSGf4FmMlZ2pdJn9HgirwlClcKf1aHjPSAd9SkSe9Nztkk10L9G6aUDL84e1zKMjXRoeF3g3inkNtBZfkf8YYFUDdTydDulKNpIQRpZuHu83NnG7isr57tkBwg9/fVPIG6P7Irf/35TcH9/s2NeV7hyBCWuDn4Zt6ueaSVjdfJ8u6iklkaqsNpwLDizKPoqoNnaDc/MWGj4zlnqdJJpAxQroRZ8+1AMbsY6bpQTCyI7gQNoq4BCOfz/owRZNEUaaRi/cSMcMUKiJoDWUl/MBnFKx1QSxjGbsQLQ=="}
        self.body_smg = {
            "mobile": "13058019302",
            "type": "1"
        }
        self.header = {}


    def get_session(self):

        test_session = requests.session()
        r_smg = requests.post (self.smg_url, data=self.body_smg, headers=self.header)
        login = test_session.post(self.base_url, data=self.body_login, headers=self.header)
        return test_session

    def get_cookie(self):

        r_smg = requests.post (self.smg_url, data=self.body_smg, headers=self.header)
        r = requests.post (self.base_url, data=self.body_login, headers=self.header)
        result = r.json ()
        cookie = r.cookies
        return cookie

if __name__ == "__main__":
    a = Login()
    a.get_cookie ()
