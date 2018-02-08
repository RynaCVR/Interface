# coding=utf-8


import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, dgd_route_params


class IsCreate(unittest.TestCase):
    """判断是否可以创建"""

    def setUp(self):
        self.result = None
        self.common_headers = common_lib.get_common_header(type="dgd")
        self.url = "http://{0}/{1}".format(config.URL.DGD_URL, dgd_route_params.IsCreate.route)
        self.params = dgd_route_params.IsCreate.params

    def tearDown(self):
        print("is_create: ", self.result)

    # @unittest.skip("无条件跳过")
    def test_is_create(self):
        """判断是否可以创建"""
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.get(self.url, headers=_headers, params=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="判断是否可以创建订单 断言失败")


if __name__ == "__main__":
    unittest.main()
