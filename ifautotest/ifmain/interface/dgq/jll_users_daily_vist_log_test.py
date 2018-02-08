# coding=utf-8


import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, dgq_route_params


class JllUsersDailyVistLogList(unittest.TestCase):
    """用户地理位置 访问日志列表"""

    def setUp(self):
        self.result = None
        self.common_headers = common_lib.get_common_header(type="dgq")
        self.url = "http://{0}/{1}".format(config.URL.DGQ_URL, dgq_route_params.JllUsersDailyVistLogList.route)
        self.params = dgq_route_params.JllUsersDailyVistLogList.params

    def tearDown(self):
        print("JllUsersDailyVistLogList:\n ", self.result)

    # @unittest.skipUnless(config.Environment == "RES", "线上环境执行")
    def test_daily_vist_log_list(self):
        """用户地理位置 访问日志列表"""
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.get(self.url, headers=_headers, params=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")


class JllUsersDailyVistLogAdd(unittest.TestCase):
    """用户地理位置 新增 每日访问日志"""

    def setUp(self):
        self.result = None
        self.common_headers = common_lib.get_common_header(type="dgq")
        self.url = "http://{0}/{1}".format(config.URL.DGQ_URL, dgq_route_params.JllUsersDailyVistLogAdd.route)
        self.params = dgq_route_params.JllUsersDailyVistLogAdd.params

    def tearDown(self):
        print("JllUsersDailyVistLogAdd:\n ", self.result)

    # @unittest.skipUnless(config.Environment == "RES", "线上环境执行")
    def test_daily_vist_log_add(self):
        """用户地理位置 新增每日访问日志"""
        self.params["device"] = common_lib.get_random_device_token()
        print(self.params["device"])
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.post(self.url, headers=_headers, data=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")


if __name__ == "__main__":
    unittest.main()
