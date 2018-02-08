
import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, jjb_route_params


class WorkdaySettingAdd(unittest.TestCase):
    """工作日设定新建"""
    def setUp(self):
        self.result = None
        self.common_header = common_lib.get_common_header()
        self.url = "http://{0}/{1}".format(config.URL.JJB_URL, jjb_route_params.WorkdaySettingAdd.route)
        self.params = jjb_route_params.WorkdaySettingAdd.params

    def tearDown(self):
        print("workday_setting_add: ", self.result)
        global result
        result = self.result

    @unittest.skip("无条件跳过")
    def test_workday_setting_add(self):
        """工作日设定新建一条数据"""
        _headers = common_lib.get_secret_header(self.url, self.common_header, self.params)
        req = requests.post(self.url, headers=_headers, params=self.params)
        self.result = req.json()
        self.assertEqual(str(self.result["errorCode"]), "0", "工作日设定二次录入 校验失败")

    def test_workday_setting_two_add(self):
        """工作日设定新建二次录入"""
        _headers = common_lib.get_secret_header(self.url, self.common_header, self.params)
        req = requests.post(self.url, headers=_headers, params=self.params)
        self.result = req.json()
        self.assertEqual(str(self.result["errorCode"]), "1", "工作日设定二次录入 校验失败")


class WorkdaySettingDownload(unittest.TestCase):
    """工作日设定下载"""
    def setUp(self):
        self.result = None
        self.common_header = common_lib.get_common_header()
        self.url = "http://{0}/{1}".format(config.URL.JJB_URL, jjb_route_params.WorkdaySettingDownload.route)
        self.params = jjb_route_params.WorkdaySettingDownload.params

    def tearDown(self):
        print("workday_setting_Download: ", self.result)
        global result
        result = self.result

    def test_workday_setting_download(self):
        """工作日设定下载"""
        _headers = common_lib.get_secret_header(self.url, self.common_header, self.params)
        req = requests.post(self.url, headers=_headers, params=self.params)
        self.result = req.json()
        self.assertEqual(str(self.result["errorCode"]), "0", "工作日设定下载 出错")


if __name__ == "__main__":
    unittest.main()
