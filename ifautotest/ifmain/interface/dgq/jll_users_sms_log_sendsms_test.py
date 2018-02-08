# coding=utf-8


import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, dgq_route_params


class JllUserSmsLogSendSms(unittest.TestCase):
    """打工圈短信验证码发送"""

    def setUp(self):
        self.result = None
        self.common_headers = common_lib.get_common_header(type="dgq")
        self.url = "http://{0}/{1}".format(config.URL.DGQ_URL, dgq_route_params.JllUserSmsLogSendSms.route)
        self.params = dgq_route_params.JllUserSmsLogSendSms.params

    def tearDown(self):
        print("JllUserSmsLogSendSms: ", self.result)

    # @unittest.skip("11")
    def test_no_edit_password(self):
        """未注册手机号 修改密码 短信验证码发送"""
        self.params['mobile'] = '13010002348'
        self.params['template'] = 'EditPassword'
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.post(self.url, headers=_headers, data=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "124", msg="errorCode")

    # @unittest.skip("11")
    def test_already_edit_password(self):
        """已注册手机号 修改密码 短信验证码发送"""
        self.params['mobile'] = '13010000002'
        self.params['template'] = 'EditPassword'
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.post(self.url, headers=_headers, data=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")

    # @unittest.skip("11")
    def test_1_no_register_verify_(self):
        """未注册手机号 短信验证码发送"""
        self.params['mobile'] = '13010002349'
        self.params['template'] = 'RegisterVerify'
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.post(self.url, headers=_headers, data=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")

    # @unittest.skip("11")
    def test_2_already_register_verify_often(self):
        """未注册手机号 短信验证码发送 紧急发送"""
        self.params['mobile'] = '13010002349'
        self.params['template'] = 'RegisterVerify'
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.post(self.url, headers=_headers, data=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "128", msg="errorCode")

    # @unittest.skip("11")
    def test_already_register_verify(self):
        """已注册手机号 短信验证码发送"""
        self.params['mobile'] = '13010000001'
        self.params['template'] = 'RegisterVerify'
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.post(self.url, headers=_headers, data=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "114", msg="errorCode")

    # @unittest.skip("11")
    def test_already_mobile_binding(self):
        """已注册手机号 绑定手机号 短信发送"""
        self.params['mobile'] = '18134413794'
        self.params['template'] = 'MobileBindingVerify'
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.post(self.url, headers=_headers, data=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "114", msg="errorCode")

    # @unittest.skip("11")
    def test_no_mobile_binding(self):
        """未注册手机号 绑定手机号 短信发送"""
        self.params['mobile'] = '13010004238'
        self.params['template'] = 'MobileBindingVerify'
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.post(self.url, headers=_headers, data=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")

    # @unittest.skip("11")
    def test_already_mobile_verify_mobile(self):
        """已注册手机号 实名认证 短信发送"""
        self.params['mobile'] = '13010000001'
        self.params['template'] = 'VerifyMobile'
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.post(self.url, headers=_headers, data=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")

    # @unittest.skip("11")
    def test_no_mobile_verify_mobile(self):
        """未注册手机号 实名认证 短信发送"""
        self.params['mobile'] = '13010008233'
        self.params['template'] = 'VerifyMobile'
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.post(self.url, headers=_headers, data=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")

    # @unittest.skip("11")
    def test_already_mobile_rebinding(self):
        """已注册手机号 解绑 短信发送"""
        self.params['mobile'] = '13010000003'
        self.params['template'] = 'MobileRebindingVerify'
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.post(self.url, headers=_headers, data=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")

    # @unittest.skip("11")
    def test_no_mobile_rebinding(self):
        """未注册手机号 解绑 短信发送"""
        self.params['mobile'] = '13010002837'
        self.params['template'] = 'MobileRebindingVerify'
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.post(self.url, headers=_headers, data=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "124", msg="errorCode")


if __name__ == "__main__":
    unittest.main()
