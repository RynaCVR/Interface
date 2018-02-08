# coding=utf-8

import time
import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, dgq_route_params


class JllNewSignDetailList(unittest.TestCase):
    """签到明细 签到列表"""

    def setUp(self):
        self.result = None
        self.common_headers = common_lib.get_common_header(type="dgq")
        self.url = "http://{0}/{1}".format(config.URL.DGQ_URL, dgq_route_params.JllNewSignDetailList.route)
        self.params = dgq_route_params.JllNewSignDetailList.params

    def tearDown(self):
        print("JllNewSignDetailList: ", self.result)

    @unittest.skipUnless(config.Environment == "RES", "线上环境执行")
    def test_sign_detail_list(self):
        """签到明细 签到列表"""
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.get(self.url, headers=_headers, params=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")


class JllNewSignDetailAdd(unittest.TestCase):
    """签到操作"""
    
    def setUp(self):
        self.result = None
        self.common_headers = common_lib.get_common_header(type="dgq")
        self.url = "http://{0}/{1}".format(config.URL.DGQ_URL, dgq_route_params.JllNewSignDetailAdd.route)
        self.params = dgq_route_params.JllNewSignDetailAdd.params
        
    def tearDown(self):
        print("JllNewSignDetailAdd: ", self.result)

    def test_sign_detail_add_1(self):
        """签到操作"""
        if common_lib.is_morning() is False:
            return
        
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.post(self.url, headers=_headers, data=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")

    def test_sign_detail_add_2_more_add(self):
        """多次签到操作"""
        if common_lib.is_morning() is False:
            return
        
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.post(self.url, headers=_headers, data=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "150", msg="errorCode")


if __name__ == "__main__":
    unittest.main()
