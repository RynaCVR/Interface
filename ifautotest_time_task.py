# coding=utf-8


import time
import ifautotest.ifmain.runner_test as runner_test


def start_task():
    while 1:
        now = time.strftime("%H%M%S", time.localtime(time.time()))
        # print(now)
        if now == "0"+str(91000) or now == str(180900):
            time.sleep(5)
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) + ": start interface autotest!")
            runner_test.my_main()
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) + ": end interface autotest!")
            time.sleep(5)
        time.sleep(1)


if __name__ == "__main__":
    start_task()
