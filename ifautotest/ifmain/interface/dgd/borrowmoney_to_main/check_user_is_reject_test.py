# coding=utf-8


import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, dgd_route_params


class CheckUserIsReject(unittest.TestCase):
    """检查用户是否被拒"""

    def setUp(self):
        self.result = None
        self.common_headers = common_lib.get_common_header(type="dgd")
        self.url = "http://{0}/{1}".format(config.URL.DGD_URL, dgd_route_params.CheckUserIsReject.route)
        self.params = dgd_route_params.CheckUserIsReject.params

    def tearDown(self):
        print("check_user_is_reject: ", self.result)

    # @unittest.skip("无条件跳过")
    def test_check_user_is_reject(self):
        """检查用户是否被拒"""
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.post(self.url, headers=_headers, data=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")


if __name__ == "__main__":
    unittest.main()
