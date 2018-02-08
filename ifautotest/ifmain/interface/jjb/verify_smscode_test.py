# coding: utf-8


import unittest

result = None


class C_VerifySmsCode(unittest.TestCase):
    """验证短信是否正确"""
    def setUp(self):
        self.result = None
        self.url = None

    def tearDown(self):
        pass
