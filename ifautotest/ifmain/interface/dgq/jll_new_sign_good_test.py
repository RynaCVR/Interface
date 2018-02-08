# coding=utf-8


import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, dgq_route_params


class JllNewSignGoodAdd(unittest.TestCase):
    """签到点赞 点赞"""

    def setUp(self):
        self.result = None
        self.common_headers = common_lib.get_common_header(type="dgq")
        self.url = "http://{0}/{1}".format(config.URL.DGQ_URL, dgq_route_params.JllNewSignGoodAdd.route)
        self.params = dgq_route_params.JllNewSignGoodAdd.params

    def tearDown(self):
        print("JllNewSignGoodAdd: ", self.result)

    # @unittest.skipUnless(config.Environment == "RES", "线上环境执行")
    def test_sign_good_add_1_1_day(self):
        """签到点赞 日榜 点赞1次"""
        self.params["type"] = "1"
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.post(self.url, headers=_headers, data=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")

    # @unittest.skipUnless(config.Environment == "RES", "线上环境执行")
    def test_sign_good_add_1_2_week(self):
        """签到点赞 周榜 点赞1次"""
        self.params["type"] = "2"
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.post(self.url, headers=_headers, data=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")

    # @unittest.skipUnless(config.Environment == "RES", "线上环境执行")
    def test_sign_good_add_1_3_month(self):
        """签到点赞 月榜 点赞1次"""
        self.params["type"] = "3"
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.post(self.url, headers=_headers, data=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")

    def test_sign_good_add_2_ten_times(self):
        """签到点赞 日榜 点赞超过10次"""
        if common_lib.is_afternoon() is False:
            return
        
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = None
        for n in range(11):
            req = requests.post(self.url, headers=_headers, data=self.params)
        self.result = req.json()
        
        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "1000", msg="errorCode")


if __name__ == "__main__":
    unittest.main()
