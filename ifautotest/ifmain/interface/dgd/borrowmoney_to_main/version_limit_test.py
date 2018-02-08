# coding=utf-8


import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, dgd_route_params


class VersionLimit(unittest.TestCase):
    """借钱版本限制"""

    def setUp(self):
        self.result = None
        self.common_headers = common_lib.get_common_header()
        self.url = "http://{0}/{1}".format(config.URL.DGD_URL, dgd_route_params.VersionLimit.route)
        self.params = dgd_route_params.VersionLimit.params

    def tearDown(self):
        print("version_limit: ", self.result)

    def test_version_limit_more_than(self):
        """获取的版本 > 用户当前版本"""
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.post(self.url, headers=_headers, data=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")
        self.assertEqual(self.result["errorStr"], "ok", "errorStr")


if __name__ == "__main__":
    unittest.main()
