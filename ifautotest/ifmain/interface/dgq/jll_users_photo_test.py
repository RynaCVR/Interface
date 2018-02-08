# coding=utf-8


import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, dgq_route_params


result = None


class a_JllUsersPhotoList(unittest.TestCase):
    """个人中心图片列表"""
    
    def setUp(self):
        self.result = None
        self.common_headers = common_lib.get_common_header(type="dgq")
        self.url = "http://{0}/{1}".format(config.URL.DGQ_URL, dgq_route_params.JllUsersPhotoList.route)
        self.params = dgq_route_params.JllUsersPhotoList.params
    
    def tearDown(self):
        print("JllUsersPhotoList:\n ", self.result)
        global result
        result = self.result
    
    # @unittest.skipUnless(config.Environment == "RES", "线上环境执行")
    def test_users_photo_list(self):
        """个人中心图片列表"""
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.get(self.url, headers=_headers)
        self.result = req.json()
        
        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")


class JllUsersPhotoAdd(unittest.TestCase):
    """个人中心图片上传"""

    def setUp(self):
        self.result = None
        self.common_headers = common_lib.get_common_header(type="dgq")
        self.url = "http://{0}/{1}".format(config.URL.DGQ_URL, dgq_route_params.JllUsersPhotoAdd.route)
        self.params = dgq_route_params.JllUsersPhotoAdd.params

    def tearDown(self):
        print("JllUsersPhotoAdd:\n ", self.result)

    # @unittest.skipUnless(config.Environment == "RES", "线上环境执行")
    def test_users_photo_add(self):
        """个人中心图片上传"""
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.post(self.url, headers=_headers, data=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")


class b_JllUsersPhotoDelPhoto(unittest.TestCase):
    """个人中心图片删除"""

    def setUp(self):
        self.result = None
        self.common_headers = common_lib.get_common_header(type="dgq")
        self.url = "http://{0}/{1}".format(config.URL.DGQ_URL, dgq_route_params.JllUsersPhotoDelPhoto.route)
        self.params = dgq_route_params.JllUsersPhotoDelPhoto.params

    def tearDown(self):
        print("JllUsersPhotoDelPhoto:\n ", self.result)

    # @unittest.skipUnless(config.Environment == "RES", "线上环境执行")
    def test_users_del_photo(self):
        """个人中心图片删除"""
        self.params["id"] = str(result["results"][0]["id"])
        print("params: \n", self.params)
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.post(self.url, headers=_headers, data=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")


if __name__ == "__main__":
    unittest.main()
