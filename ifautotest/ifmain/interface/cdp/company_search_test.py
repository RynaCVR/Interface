# coding=utf-8


import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, cdp_route_params


class CompanySearch(unittest.TestCase):
    """工厂搜索"""

    continue_result = None

    def setUp(self):
        self.result = None
        self.common_headers = common_lib.get_common_header()
        self.url = "http://{0}/{1}".format(config.URL.JJB_URL, cdp_route_params.CompanySearch.route)
        self.params = cdp_route_params.CompanySearch.params

    def tearDown(self):
        print("company_search: ", self.result)

    def test_1_company_search(self):
        """工厂搜索"""
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.post(self.url, headers=_headers, data=self.params)
        CompanySearch.continue_result = self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")

    def test_2_company_search_next_page(self):
        """工厂搜索下一页"""

        xid = CompanySearch.continue_result["results"][-1]["xid"]
        self.params["xid"] = xid
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.post(self.url, headers=_headers, data=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")


if __name__ == "__main__":
    unittest.main()
