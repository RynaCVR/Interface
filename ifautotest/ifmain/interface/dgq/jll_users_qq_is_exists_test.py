# coding=utf-8


import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, dgq_route_params


class JllUsersQQIsExists(unittest.TestCase):
    """判断QQ是否已经存在"""

    def setUp(self):
        self.result = None
        self.common_headers = common_lib.get_common_header(type="dgq")
        self.url = "http://{0}/{1}".format(config.URL.DGQ_URL, dgq_route_params.JllUsersQQIsExists.route)
        self.params = dgq_route_params.JllUsersQQIsExists.params
    
    def tearDown(self):
        print("JllUsersPhotoList:\n ", self.result)
    
    @unittest.skipUnless(config.Environment == "RES", "线上环境执行")
    def test_users_qq_is_exists_yes(self):
        """已存在qqopenid 判断QQ是否已经存在"""
        self.params["qq_openid"] = "1517218394"
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.post(self.url, headers=_headers, data=self.params)
        self.result = req.json()
        
        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")

    @unittest.skipUnless(config.Environment == "RES", "线上环境执行")
    def test_users_qq_is_exists_no(self):
        """不存在qqopenid 判断QQ是否已经存在"""
        self.params["qq_openid"] = "6"
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.post(self.url, headers=_headers, data=self.params)
        self.result = req.json()
    
        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "4", msg="errorCode")
