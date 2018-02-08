# coding: utf-8


import unittest
import requests

from ifautotest.ifmain.common import config, common_lib, jjb_route_params

result = None


class C_Mobile_Register(unittest.TestCase):
    """手机号注册"""

    def setUp(self):
        self.result = None
        self.common_header = common_lib.get_common_header()
        self.url = "http://{0}/{1}".format(config.URL.JJB_URL, jjb_route_params.MobileRegister.route)
        self.params = jjb_route_params.MobileRegister.params

    def tearDown(self):
        print("register: ", self.result)
        global result
        result = self.result

    @unittest.skip("无条件跳过")
    def test_register_with_success(self):
        """手机号成功注册"""
        self.params["mobile"] = "13010008238"
        _headers = common_lib.get_secret_header(self.url, self.common_header, self.params)
        req = requests.post(self.url, headers=_headers, params=self.params)
        self.result = req.json()
        self.assertEqual(str(self.result["errorCode"]), "0", "手机号注册成功")

    def test_register_with_mobile_exist(self):
        """验证码错误"""
        self.params["mobile"] = "13010000001"
        _headers = common_lib.get_secret_header(self.url, self.common_header, self.params)
        req = requests.post(self.url, headers=_headers, params=self.params)
        self.result = req.json()
        self.assertEqual(str(self.result["errorCode"]), "126", "手机号已注册")

    def test_register_with_mobile_Nine(self):
        """手机号10位"""
        self.params["mobile"] = "1813441379"
        _headers = common_lib.get_secret_header(self.url, self.common_header, self.params)
        req = requests.post(self.url, headers=_headers, params=self.params)
        self.result = req.json()
        self.assertEqual(str(self.result["errorCode"]), "1", "未使用正确格式的手机号码")

    def test_register_with_mobile_Eleven(self):
        """手机号12位"""
        self.params["mobile"] = "181344137944"
        _headers = common_lib.get_secret_header(self.url, self.common_header, self.params)
        req = requests.post(self.url, headers=_headers, params=self.params)
        self.result = req.json()
        self.assertEqual(str(self.result["errorCode"]), "1", "未使用正确格式的手机号码")


class D_QQRegister(unittest.TestCase):
    """QQ注册"""
    def setUp(self):
        self.result = None
        self.common_header = common_lib.get_common_header()
        self.url = "http://{0}/{1}".format(config.URL.JJB_URL, jjb_route_params.QQRegister.route)
        self.params = jjb_route_params.QQRegister.params

    def tearDown(self):
        print("QQRegister: ", self.result)
        global result
        result = self.result

    def test_qq_register_success(self):
        """QQ注册成功"""
        self.params["qq_openid"] = self.common_header["Requesttime"]
        _headers = common_lib.get_secret_header(self.url, self.common_header, self.params)
        req = requests.post(self.url, headers=_headers, params=self.params)
        self.result = req.json()
        self.assertEqual(str(self.result["errorCode"]), "0", "QQ注册成功 校验失败")


if __name__ == "__main__":
    unittest.main()
