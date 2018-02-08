# coding: utf-8


import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, jjb_route_params


class UserMobileIsExists(unittest.TestCase):
    """判断手机号是否已经注册"""
    def setUp(self):
        self.result = None
        self.common_header = common_lib.get_common_header()
        self.url = "http://{0}/{1}".format(config.URL.JJB_URL, jjb_route_params.UserMobileIsExists.route)
        self.params = jjb_route_params.UserMobileIsExists.params

    def tearDown(self):
        print("UserMobileIsExists: ", self.result)

    def test_mobile_is_exists_yes(self):
        """已注册手机号 判断是否存在"""

        self.params["mobile"] = "13010000001"
        headers = common_lib.get_secret_header(self.url, self.common_header, self.params)
        req = requests.post(self.url, headers=headers, params=self.params)
        self.result = req.json()

        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")
        self.assertEqual(str(self.result["results"]), "1", msg="已注册手机号")

    def test_mobile_is_exists_no(self):
        """未注册手机号 判断是否存在"""
        self.params["mobile"] = "13010003827"
        headers = common_lib.get_secret_header(self.url, self.common_header, self.params)
        req = requests.post(self.url, headers=headers, params=self.params)
        self.result = req.json()

        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")
        self.assertEqual(str(self.result["results"]), "0", msg="已注册手机号")

    def test_mobile_with_12(self):
        """12位手机号 判断是否存在"""
        self.params["mobile"] = "130100000011"
        headers = common_lib.get_secret_header(self.url, self.common_header, self.params)
        req = requests.post(self.url, headers=headers, params=self.params)
        self.result = req.json()

        self.assertEqual(str(self.result["errorCode"]), "1", msg="errorCode")
        self.assertEqual(self.result["results"], None, msg="12位手机号")

    def test_mobile_with_10(self):
        """10位手机号 判断是否存在"""
        self.params["mobile"] = "1301000000"
        headers = common_lib.get_secret_header(self.url, self.common_header, self.params)
        req = requests.post(self.url, headers=headers, params=self.params)
        self.result = req.json()

        self.assertEqual(str(self.result["errorCode"]), "1", msg="errorCode")
        self.assertEqual(self.result["results"], None, msg="10位手机号")

    def test_mobile_with_none(self):
        """不填写手机号 判断是否存在"""
        self.params["mobile"] = ""
        headers = common_lib.get_secret_header(self.url, self.common_header, self.params)
        req = requests.post(self.url, headers=headers, params=self.params)
        self.result = req.json()

        self.assertEqual(str(self.result["errorCode"]), "3", msg="请求参数错误")


if __name__ == "__main__":
    unittest.main()
