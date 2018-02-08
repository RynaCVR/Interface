# coding: utf-8


import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, jjb_route_params


result = None


class SendSms(unittest.TestCase):
    """发送短信验证码"""
    def setUp(self):
        self.result = None
        self.common_header = common_lib.get_common_header()
        self.url = "http://{0}/{1}".format(config.URL.JJB_URL, jjb_route_params.SendSms.route)
        self.params = jjb_route_params.SendSms.params

    def tearDown(self):
        print("SendSms: ", self.result)
        global result
        result = self.result

    def test_send_sms_with_success(self):
        """发送短信"""

        self.params["mobile"] = "18134413794"
        self.params["type"] = "1"
        headers = common_lib.get_secret_header(self.url, self.common_header, self.params)

        req = requests.post(self.url, headers=headers, params=self.params)
        self.result = req.json()

        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")
        self.assertEqual(self.result["errorStr"], "ok", "errorStr")


if __name__ == "__main__":
    unittest.main()
