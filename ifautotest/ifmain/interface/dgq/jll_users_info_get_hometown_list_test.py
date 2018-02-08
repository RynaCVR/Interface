# coding=utf-8


import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, dgq_route_params


class JllUsersInfoGetHomeTownList(unittest.TestCase):
    """我的老乡列表"""

    def setUp(self):
        self.result = None
        self.common_headers = common_lib.get_common_header(type="dgq")
        self.url = "http://{0}/{1}".format(config.URL.DGQ_URL, dgq_route_params.JllUsersInfoGetHomeTownList.route)
        self.params = dgq_route_params.JllUsersInfoGetHomeTownList.params

    def tearDown(self):
        print("JllUsersInfoGetHomeTownList:\n ", self.result)

    # @unittest.skipUnless(config.Environment == "RES", "线上环境执行")
    def test_user_change_moible(self):
        """我的老乡列表"""
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.get(self.url, headers=_headers)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")
