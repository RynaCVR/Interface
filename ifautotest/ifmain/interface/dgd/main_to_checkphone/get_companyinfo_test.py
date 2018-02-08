# coding=utf-8


import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, dgd_route_params


class GetCompanyinfo(unittest.TestCase):
    """拉取公司数据"""

    def setUp(self):
        self.result = None
        self.common_headers = common_lib.get_common_header(type="dgd")
        self.url = "http://{0}/{1}".format(config.URL.DGD_URL, dgd_route_params.CompanyInfo.route)
        self.params = dgd_route_params.CompanyInfo.params

    def tearDown(self):
        print("get_companyinfo: ", self.result)

    # @unittest.skip("无条件跳过")
    def test_get_companyinfo(self):
        """拉取公司数据"""
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.get(self.url, headers=_headers, params=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="拉取公司信息 断言失败")


if __name__ == "__main__":
    unittest.main()
