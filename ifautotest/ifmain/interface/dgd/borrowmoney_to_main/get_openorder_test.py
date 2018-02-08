# coding=utf-8


import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, dgd_route_params


class GetOpenorder(unittest.TestCase):
    """获取未完成订单"""

    def setUp(self):
        self.result = None
        self.common_headers = common_lib.get_common_header(type="dgd")
        self.url = "http://{0}/{1}".format(config.URL.DGD_URL, dgd_route_params.GetOpenorder.route)
        self.params = dgd_route_params.GetOpenorder.params

    def tearDown(self):
        print("get_openorder: ", self.result)

    # @unittest.skip("无条件跳过")
    def test_get_openorder_no(self):
        """是否有未完成订单-无"""
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.post(self.url, headers=_headers, data=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        if config.Environment == "DEV":
            self.assertEqual(str(self.result["errorCode"]), "4", msg="无未完成订单 断言失败")
        elif config.Environment == "PRE":
            self.assertEqual(str(self.result["errorCode"]), "0", msg="无未完成订单 断言失败")


if __name__ == "__main__":
    unittest.main()
