# coding=utf-8


import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, dgd_route_params


class GetParams(unittest.TestCase):
    """获取参数"""

    def setUp(self):
        self.result = None
        self.common_headers = common_lib.get_common_header(type="dgd")
        self.url = "http://{0}/{1}".format(config.URL.DGD_URL, dgd_route_params.GetParams.route)
        self.params = dgd_route_params.GetParams.params

    def tearDown(self):
        print("get_params: ", self.result)

    # @unittest.skip("无条件跳过")
    def test_get_params(self):
        """获取参数"""
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.post(self.url, headers=_headers, data=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="获取参数 断言失败")


if __name__ == "__main__":
    unittest.main()
