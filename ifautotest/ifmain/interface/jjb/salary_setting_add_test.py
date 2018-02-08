# coding=utf-8

import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, jjb_route_params


result = None


class SalarySettingAdd(unittest.TestCase):
    """基本工资备份"""
    def setUp(self):
        self.result = None
        self.common_header = common_lib.get_common_header()
        self.url = "http://{0}/{1}".format(config.URL.JJB_URL, jjb_route_params.SalarySettingAdd.route)
        self.params = jjb_route_params.SalarySettingAdd.params

    def tearDown(self):
        print("salary_setting_add: ", self.result)
        global result
        result = self.result

    def test_salary_setting_add(self):
        """基本工资备份数据"""
        _headers = common_lib.get_secret_header(self.url, self.common_header, self.params)
        req = requests.post(self.url, headers=_headers, params=self.params)
        self.result = req.json()
        self.assertEqual(str(self.result["errorCode"]), "0", "基本工资备份数据 校验失败")


if __name__ == "__main__":
    unittest.main()
