# coding: utf-8


import unittest
import requests

from ifautotest.ifmain.common import config, common_lib, dgq_route_params


class RandNickname(unittest.TestCase):
    """获取随机名字"""
    def setUp(self):
        self.result = None
        self.common_header = common_lib.get_common_header()
        self.url = "http://{0}/{1}".format(config.URL.DGQ_URL, dgq_route_params.RandNickname.route)
        self.params = dgq_route_params.RandNickname.params

    def tearDown(self):
        print("RandNickname: ", self.result)

    def test_get_rand_nickname(self):
        """获取随机名字"""
        _headers = common_lib.get_secret_header(self.url, self.common_header, self.params)
        req = requests.post(self.url, headers=_headers)
        self.result = req.json()
        self.assertEqual(str(self.result["errorCode"]), "0", "error")
