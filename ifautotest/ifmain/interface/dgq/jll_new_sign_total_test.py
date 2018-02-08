# coding=utf-8


import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, dgq_route_params


class JllNewSignTotalTotal(unittest.TestCase):
    """签到汇总 总览"""
    
    def setUp(self):
        self.result = None
        self.common_headers = common_lib.get_common_header(type="dgq")
        self.url = "http://{0}/{1}".format(config.URL.DGQ_URL, dgq_route_params.JllNewSignTotalTotal.route)
        self.params = dgq_route_params.JllNewSignTotalTotal.params
    
    def tearDown(self):
        print("JllNewSignTotalTotal: ", self.result)
    
    # @unittest.skipUnless(config.Environment == "RES", "线上环境执行")
    def test_sign_total_total(self):
        """签到汇总"""
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.post(self.url, headers=_headers)
        self.result = req.json()
        
        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")


class JllNewSignTotalList(unittest.TestCase):
    """签到汇总 排行榜"""
    
    def setUp(self):
        self.result = None
        self.common_headers = common_lib.get_common_header(type="dgq")
        self.url = "http://{0}/{1}".format(config.URL.DGQ_URL, dgq_route_params.JllNewSignTotalList.route)
        self.params = dgq_route_params.JllNewSignTotalList.params
    
    def tearDown(self):
        print("JllNewSignTotalList: ", self.result)
    
    # @unittest.skipUnless(config.Environment == "RES", "线上环境执行")
    def test_sign_total_list_day(self):
        """签到汇总 排行榜 日榜"""
        self.params["type"] = "1"
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.get(self.url, headers=_headers, params=self.params)
        self.result = req.json()
        
        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")

    # @unittest.skipUnless(config.Environment == "RES", "线上环境执行")
    def test_sign_total_list_week(self):
        """签到汇总 排行榜 周榜"""
        self.params["type"] = "2"
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.get(self.url, headers=_headers, params=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")

    # @unittest.skipUnless(config.Environment == "RES", "线上环境执行")
    def test_sign_total_list_month(self):
        """签到汇总 排行榜 月榜"""
        self.params["type"] = "3"
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.get(self.url, headers=_headers, params=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")


if __name__ == "__main__":
    unittest.main()
