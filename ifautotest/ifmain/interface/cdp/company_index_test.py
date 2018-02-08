# coding=utf-8


import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, cdp_route_params


class CompanyIndex(unittest.TestCase):
    """厂点评首页数据获取"""

    def setUp(self):
        self.result = None
        self.common_headers = common_lib.get_common_header()

        if config.Environment == "RES":
            self.url = "http://{0}/{1}".format(config.URL.CDP_URL, cdp_route_params.CompanyIndex.route)
        else:
            self.url = "http://{0}:8080/{1}".format(config.URL.CDP_URL, cdp_route_params.CompanyIndex.route)
        self.params = cdp_route_params.CompanyIndex.params

    def tearDown(self):
        print("company_index: ", self.result)

    def test_company_index(self):
        """厂点评首页数据获取"""
        # _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.get(self.url)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")


if __name__ == "__main__":
    unittest.main()
