# coding=utf-8


import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, dgd_route_params


class GetMyinfo(unittest.TestCase):
    """拉取个人信息"""

    def setUp(self):
        self.result = None
        self.common_headers = common_lib.get_common_header(type="dgd")
        self.url = "http://{0}/{1}".format(config.URL.DGD_URL, dgd_route_params.MyInfo.route)
        self.params = dgd_route_params.MyInfo.params

    def tearDown(self):
        print("get_myinfo: ", self.result)

    # @unittest.skip("无条件跳过")
    def test_get_myinfo(self):
        """拉取个人信息失败用例"""
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.get(self.url, headers=_headers, params=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "4", msg="拉取个人信息 断言失败")


if __name__ == "__main__":
    unittest.main()
