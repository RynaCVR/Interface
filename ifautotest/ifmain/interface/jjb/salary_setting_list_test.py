
import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, jjb_route_params


result = None


class SalarySettingList(unittest.TestCase):
    """基本工资备份"""

    def setUp(self):
        self.result = None
        self.common_header = common_lib.get_common_header()
        self.url = "http://{0}/{1}".format(config.URL.JJB_URL, jjb_route_params.SalarySettingList.route)
        self.params = jjb_route_params.SalarySettingList.params

    def tearDown(self):
        print("salary_setting_list: ", self.result)
        global result
        result = self.result

    def test_salary_setting_list(self):
        """基本工资列表"""
        _headers = common_lib.get_secret_header(self.url, self.common_header, self.params)
        req = requests.post(self.url, headers=_headers, params=self.params)
        self.result = req.json()
        self.assertEqual(str(self.result["errorCode"]), "0", "获取基本工资列表数据 校验失败")


if __name__ == "__main__":
    unittest.main()
