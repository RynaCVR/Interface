# coding=utf-8


import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, dgq_route_params


class JllTopDayTopmark(unittest.TestCase):
    """红人榜 日榜"""

    def setUp(self):
        self.result = None
        self.common_headers = common_lib.get_common_header(type="dgq")
        self.url = "http://{0}/{1}".format(config.URL.DGQ_URL, dgq_route_params.JllTopDayTopmark.route)
        self.params = dgq_route_params.JllTopDayTopmark.params

    def tearDown(self):
        print("JllTopDayTopmark: ", self.result)

    # @unittest.skipUnless(config.Environment == "RES", "线上环境执行")
    def test_day_topmark(self):
        """红人榜 日榜"""
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.post(self.url, headers=_headers, data=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")


class JllTopWeekTopmark(unittest.TestCase):
    """红人榜 周榜"""

    def setUp(self):
        self.result = None
        self.common_headers = common_lib.get_common_header(type="dgq")
        self.url = "http://{0}/{1}".format(config.URL.DGQ_URL, dgq_route_params.JllTopWeekTopmark.route)
        self.params = dgq_route_params.JllTopWeekTopmark.params

    def tearDown(self):
        print("JllTopWeekTopmark: ", self.result)

    # @unittest.skipUnless(config.Environment == "RES", "线上环境执行")
    def test_week_topmark(self):
        """红人榜 周榜"""
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.post(self.url, headers=_headers, data=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")


if __name__ == "__main__":
    unittest.main()
