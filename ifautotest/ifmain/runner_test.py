# coding=utf-8


import os
import time
import unittest
import HTMLTestReportCN
from ifautotest.ifmain.common import send_email


def abs_path(path):
    PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )
    return PATH(path)


def my_main():
    test_dir = abs_path('./interface')
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')

    # 无报告
    # runner = unittest.TextTestRunner()
    # runner.run(discover)

    # 有报告
    now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    fp = open(abs_path("./report/" + now + ".html"), 'wb')
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title='接口自动化执行报告',
        description='上海慧贤网络科技有限公司',
        tester="慧贤测试小分队")
    runner.run(discover)
    fp.close()

    # 邮件发送
    send_email.send_email(attach_name=now)


if __name__ == "__main__":
    my_main()
