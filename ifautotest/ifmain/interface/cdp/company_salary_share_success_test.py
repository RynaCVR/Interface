# coding=utf-8


import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, cdp_route_params


class CompanySalaryShareSuccess(unittest.TestCase):
    """工资条分享成功"""

    def setUp(self):
        self.result = None
        self.common_headers = common_lib.get_common_header()
        self.url = "http://{0}/{1}".format(config.URL.CDP_URL, cdp_route_params.CompanySalaryShareSuccess.route)
        self.params = cdp_route_params.CompanySalaryShareSuccess.params

    def tearDown(self):
        print("CompanySalaryShareSuccess: ", self.result)

    def test_company_salary_share_success(self):
        """工资条分享成功"""

        req = requests.get(self.url, params=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")


if __name__ == "__main__":
    unittest.main()
