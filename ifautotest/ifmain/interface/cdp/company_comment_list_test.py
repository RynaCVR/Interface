# coding=utf-8


import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, cdp_route_params


class CompanyCommentList(unittest.TestCase):
    """某一工厂点评列表"""

    def setUp(self):
        self.result = None
        self.common_headers = common_lib.get_common_header()
        self.url = "http://{0}/{1}".format(config.URL.CDP_URL, cdp_route_params.CompanyCommentList.route)
        self.params = cdp_route_params.CompanyCommentList.params

    def tearDown(self):
        print("CompanyCommentList: ", self.result)

    @unittest.skipUnless(config.Environment == "RES", "当为线上环境时执行用例")
    def test_company_comment_list(self):
        """某一工厂点评列表"""
        # _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        # req = requests.post(self.url, headers=_headers, data=self.params)
        req = requests.get(self.url, params=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")


if __name__ == "__main__":
    unittest.main()
