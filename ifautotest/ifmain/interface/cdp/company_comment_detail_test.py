# coding=utf-8


import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, cdp_route_params


class CompanyCommentDetail(unittest.TestCase):
    """点评详情"""

    def setUp(self):
        self.result = None
        self.common_headers = common_lib.get_common_header()
        self.url = "http://{0}/{1}".format(config.URL.CDP_URL, cdp_route_params.CompanyCommentDetail.route)
        self.params = cdp_route_params.CompanyCommentDetail.params

    def tearDown(self):
        print("CompanyCommentDetail: ", self.result)

    def test_company_comment_detail(self):
        """点评详情"""

        req = requests.get(self.url, params=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")


if __name__ == "__main__":
    unittest.main()
