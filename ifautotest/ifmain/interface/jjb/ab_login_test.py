
import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, jjb_route_params


result = None


class MobileLogin(unittest.TestCase):
    """登录接口用例"""
    def setUp(self):
        self.result = None
        self.common_header = common_lib.get_common_header()
        self.url = "http://{0}/{1}".format(config.URL.JJB_URL, jjb_route_params.MobileLogin.route)
        self.params = jjb_route_params.MobileLogin.params

    def tearDown(self):
        print("login: ", self.result)
        global result
        result = self.result

    def test_login_correct_mobile_correct_password(self):
        """正确手机号正确密码"""
        self.params["mobile"] = "13010000001"
        self.params["password"] = "e10adc3949ba59abbe56e057f20f883e"
        _headers = common_lib.get_secret_header(self.url, self.common_header, self.params)
        req = requests.post(self.url, headers=_headers, params=self.params)
        self.result = req.json()
        self.assertEqual(str(self.result["errorCode"]), "0", "手机号登录成功 校验失败")

    def test_login_correct_mobile_fail_password(self):
        """正确手机号错误密码"""
        self.params["mobile"] = "18134413794"
        self.params["password"] = "e10adc3949ba59abbe56e057f20f8832"    # e ==> 2
        _headers = common_lib.get_secret_header(self.url, self.common_header, self.params)
        req = requests.post(self.url, headers=_headers, params=self.params)
        self.result = req.json()
        self.assertEqual(str(self.result["errorCode"]), "115", "登录失败，账号或密码错误")

    def test_login_correct_mobile_fail_Ten_password(self):
        """正确手机号5位密码"""
        self.params["mobile"] = "18134413794"
        self.params["password"] = "827ccb0eea8a706c4c34a16891f84e7b"
        _headers = common_lib.get_secret_header(self.url, self.common_header, self.params)
        req = requests.post(self.url, headers=_headers, params=self.params)
        self.result = req.json()
        self.assertEqual(str(self.result["errorCode"]), "115", "登录失败，账号或密码错误")

    def test_login_fail_Ten_mobile_correct_password(self):
        """10位手机号正确密码 登录"""
        self.params["mobile"] = "1813441379"
        self.params["password"] = "e10adc3949ba59abbe56e057f20f883e"
        _headers = common_lib.get_secret_header(self.url, self.common_header, self.params)
        req = requests.post(self.url, headers=_headers, params=self.params)
        self.result = req.json()
        self.assertEqual(str(self.result["errorCode"]), "1", "请使用正确格式的手机号码")

    def test_login_fail_Twelve_mobile_correct_password(self):
        """12位手机号正确密码 登录"""
        self.params["mobile"] = "181344137941"
        self.params["password"] = "e10adc3949ba59abbe56e057f20f883e"
        _headers = common_lib.get_secret_header(self.url, self.common_header, self.params)
        req = requests.post(self.url, headers=_headers, params=self.params)
        self.result = req.json()
        self.assertEqual(str(self.result["errorCode"]), "1", "请使用正确格式的手机号码")


class QQLogin(unittest.TestCase):
    """QQ登录"""
    def setUp(self):
        self.result = None
        self.common_header = common_lib.get_common_header()
        self.url = "http://{0}/{1}".format(config.URL.JJB_URL, jjb_route_params.QQLogin.route)
        self.params = jjb_route_params.QQLogin.params

    def tearDown(self):
        print("login: ", self.result)
        global result
        result = self.result

    def test_login_success(self):
        """QQ登录成功"""
        _headers = common_lib.get_secret_header(self.url, self.common_header, self.params)
        req = requests.post(self.url, headers=_headers, params=self.params)
        self.result = req.json()
        self.assertEqual(str(self.result["errorCode"]), "0", "QQ登录成功 校验失败")


if __name__ == "__main__":
    unittest.main()
