# coding=utf-8


import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, cdp_route_params


class CompanyRedPacket(unittest.TestCase):
    """上传工资条领红包活动，用户活动状态"""

    def setUp(self):
        self.result = None
        self.common_headers = common_lib.get_common_header()
        self.url = "http://{0}/{1}".format(config.URL.CDP_URL, cdp_route_params.CompanyRedPacket.route)
        self.params = cdp_route_params.CompanyRedPacket.params

    def tearDown(self):
        print("CompanyRedPacket: ", self.result)

    @unittest.skipUnless(config.Environment == "11", "此接口已停用")
    def test_company_red_packet(self):
        """上传工资条领红包活动，用户活动状态"""
        req = requests.get(self.url, params=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")


if __name__ == "__main__":
    unittest.main()
