
import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, jjb_route_params

"""这里的测试用例还会添加，用于验证备份的数据，是否正确"""

result = None


class A_BackupData(unittest.TestCase):
    """备份数据"""
    def setUp(self):
        self.result = None
        self.common_header = common_lib.get_common_header()
        self.url = "http://{0}/{1}".format(config.URL.JJB_URL, jjb_route_params.BackupDatas.route)
        self.params = jjb_route_params.BackupDatas.params

    def tearDown(self):
        print("backup_datas: ", self.result)
        global result
        result = self.result

    def test_backup_datas(self):
        """备份数据"""
        _headers = common_lib.get_secret_header(self.url, self.common_header, self.params)
        req = requests.post(self.url, headers=_headers, params=self.params)
        self.result = req.json()
        self.assertEqual(str(self.result["errorCode"]), "0", "备份数据 校验失败")


class B_PullBata(unittest.TestCase):
    """下拉数据"""
    def setUp(self):
        self.result = None
        self.common_header = common_lib.get_common_header()
        self.url = "http://{0}/{1}".format(config.URL.JJB_URL, jjb_route_params.PullDatas.route)
        self.params = jjb_route_params.PullDatas.params

    def tearDown(self):
        print("pull_datas: ", self.result)
        global result
        result = self.result

    def test_pull_datas(self):
        """下拉数据"""
        _headers = common_lib.get_secret_header(self.url, self.common_header, self.params)
        req = requests.post(self.url, headers=_headers, params=self.params)
        self.result = req.json()
        self.assertEqual(str(self.result["errorCode"]), "0", " 下拉数据 校验失败")


if __name__ == "__main__":
    unittest.main()
