# coding=utf-8


import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, jjb_route_params


result = None


class Guest(unittest.TestCase):
    """首次打开获取临时账号"""

    def setUp(self):
        self.result = None
        self.common_headers = common_lib.get_common_header()
        self.url = "http://{0}/{1}".format(config.URL.JJB_URL, jjb_route_params.Guest.route)
        self.params = jjb_route_params.Guest.params

    def tearDown(self):
        print("Guest: ", self.result)
        global result
        result = self.result

    def test_guest_with_success(self):
        """无参数，第一次打开app直接请求"""
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)

        req = requests.post(self.url, headers=_headers, data=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")
        self.assertEqual(self.result["errorStr"], "ok", "errorStr")


if __name__ == "__main__":
    unittest.main()
