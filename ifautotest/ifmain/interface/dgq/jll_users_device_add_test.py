# coding=utf-8


import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, dgq_route_params


class JllUsersDeviceAdd(unittest.TestCase):
    """新建设备号信息"""

    def setUp(self):
        self.result = None
        self.common_headers = common_lib.get_common_header(type="dgq")
        self.url = "http://{0}/{1}".format(config.URL.DGQ_URL, dgq_route_params.JllUsersDeviceAdd.route)
        self.params = dgq_route_params.JllUsersDeviceAdd.params

    def tearDown(self):
        print("JllUsersDeviceAdd: ", self.result)

    # @unittest.skipUnless(config.Environment == "RES", "线上环境执行")
    def test_device_add_1(self):
        """新建设备号信息"""
        self.params["device_token"] = common_lib.get_random_device_token()
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.post(self.url, headers=_headers, data=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")

    # @unittest.skipUnless(config.Environment == "RES", "线上环境执行")
    def test_device_add_2_same_device_token(self):
        """新建设备号信息 相同的设备token"""
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.post(self.url, headers=_headers, params=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "10", msg="errorCode")


if __name__ == "__main__":
    unittest.main()
