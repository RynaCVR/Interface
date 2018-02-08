# coding=utf-8


import unittest
import requests
from ifautotest.ifmain.common import config, common_lib, dgq_route_params


class TopicDetail(unittest.TestCase):
    """某一话题详情"""

    def setUp(self):
        self.result = None
        self.common_headers = common_lib.get_common_header(type="dgq")
        self.url = "http://{0}/{1}".format(config.URL.DGQ_URL, dgq_route_params.JllTopicTopicDetail.route)
        self.params = dgq_route_params.JllTopicTopicDetail.params

    def tearDown(self):
        print("TopicDetail: ", self.result)

    @unittest.skipUnless(config.Environment == "RES", "线上环境执行")
    def test_topic_detail(self):
        """某一话题详情"""
        _headers = common_lib.get_secret_header(self.url, self.common_headers, self.params)
        req = requests.get(self.url, headers=_headers, params=self.params)
        self.result = req.json()

        # 断言相关参数，是否正确
        self.assertEqual(str(self.result["errorCode"]), "0", msg="errorCode")


if __name__ == "__main__":
    unittest.main()
