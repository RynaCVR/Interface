
import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, jjb_route_params


class SplashScreen(unittest.TestCase):
    """闪屏数据获取"""
    def setUp(self):
        self.result = None
        self.common_header = common_lib.get_common_header()
        self.url = "http://{0}/{1}".format(config.URL.JJB_URL, jjb_route_params.SplashScreen.route)
        self.params = jjb_route_params.SplashScreen.params

    def tearDown(self):
        print("splash_screen: ", self.result)
        global result
        result = self.result

    def test_splash_screen(self):
        """闪屏数据获取"""
        _headers = common_lib.get_secret_header(self.url, self.common_header, self.params)
        req = requests.post(self.url, headers=_headers, params=self.params)
        self.result = req.json()
        self.assertEqual(str(self.result["errorCode"]), "0", "获取闪屏图片 校验失败")


if __name__ == "__main__":
    unittest.main()
