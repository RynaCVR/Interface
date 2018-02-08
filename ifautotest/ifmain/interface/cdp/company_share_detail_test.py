# coding=utf-8


import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, cdp_route_params


class CompanyShareDetail(unittest.TestCase):
    """工厂详情页分享落地页"""

    def setUp(self):
        self.result = None
        self.common_headers = common_lib.get_common_header()
        self.url = "http://{0}/{1}".format(config.URL.CDP_URL, cdp_route_params.CompanyShareDetail.route)
        self.params = cdp_route_params.CompanyShareDetail.params

    def tearDown(self):
        print("CompanyShareDetail: ", self.result)

    def test_company_share_detail(self):
        """工厂详情页分享落地页"""
        # _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        # req = requests.post(self.url, headers=_headers, data=self.params)
        req = requests.get(self.url, params=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")


if __name__ == "__main__":
    unittest.main()
