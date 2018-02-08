
import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, jjb_route_params


result = None


class OpenDays(unittest.TestCase):
    """打开天数"""
    def setUp(self):
        self.result = None
        self.common_header = common_lib.get_common_header()
        self.url = "http://{0}/{1}".format(config.URL.JJB_URL, jjb_route_params.OpenDays.route)
        self.params = jjb_route_params.OpenDays.params

    def tearDown(self):
        print("opendays: ", self.result)
        global result
        result = self.result

    def test_opendays(self):
        """打开天数"""
        _headers = common_lib.get_secret_header(self.url, self.common_header, self.params)
        req = requests.post(self.url, headers=_headers, params=self.params)
        self.result = req.json()
        self.assertEqual(str(self.result["errorCode"]), "0", "打开天数 校验失败")


if __name__ == "__main__":
    unittest.main()