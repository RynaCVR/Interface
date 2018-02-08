# coding=utf-8


import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, cdp_route_params


class SalaryAdd(unittest.TestCase):
    """添加工资条"""

    def setUp(self):
        self.result = None
        self.common_headers = common_lib.get_common_header()
        self.url = "http://{0}/{1}".format(config.URL.JJB_URL, cdp_route_params.SalaryAdd.route)
        self.params = cdp_route_params.SalaryAdd.params

    def tearDown(self):
        print("salary_add: ", self.result)

    def test_salary_add(self):
        """添加工资条"""
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.post(self.url, headers=_headers, data=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")
        self.assertEqual(self.result["errorStr"], "ok", "errorStr")


if __name__ == "__main__":
    unittest.main()
