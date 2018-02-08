# coding = "utf-8"

import os
import copy
import uiautotest.server.config as config
import time
import socket
import subprocess
import multiprocessing
from uiautotest.server.common import operate_file
from uiautotest.server.appium_service.operate_node_config import NodeConfigJson


class AppiumService:

    def __init__(self, device):
        self.device = device
        self.appium_ip = config.appium_ip
        self.appium_port = str(device["port"])
        self.appium_bport = str(int(self.appium_port) + 100)

    def abs_path(self, path):
        PATH = lambda p: os.path.abspath(
            os.path.join(os.path.dirname(__file__), p)
        )
        return PATH(path)

    def assert_process_still_running(self, process):
        """
        检查process是否结束，return_code不为空，说明有错误
        :param process:
        :return:
        """
        return_code = None
        try:
            return_code = process.poll()
            if return_code is not None:
                raise OSError
        except OSError:
            print('Service grid unexpectedly exited. Status code was: %s' % return_code)

    def kill_pid_with_port(self, port):
        result = False
        cmd_search_pid = "netstat -tnlp | grep {0} | cut -c 81-85".format(port)
        try:
            search_pid = subprocess.check_output(cmd_search_pid, shell=True)
            search_pid = str(search_pid).strip("\/n'b")  # 如果是4位pid，截取的5位最后一位是/，要去除
            print("search_pid: ", str(search_pid))

            if len(search_pid) == 0:  # 有可能是为空
                print("根据端口查进程pid为空!")
                return result
            cmd_kill_pid = "kill -9 {0}".format(search_pid)
            kill_pid = subprocess.call(cmd_kill_pid, shell=True)
            if kill_pid != 0:
                print("kill pid {0} failed".format(search_pid))
                return False

            result = True
            print("kill pid {0} successfully".format(search_pid))
            return result
        except:
            print("异常退出！")
            return result

    def async_kill_appium(self, port):
        _port = copy.deepcopy(port)
        time.sleep(7200)
        if not self.port_is_running(_port):
            print("异步要结束的端口{0}没有在运行".format(_port))
            return
        result = self.kill_pid_with_port(_port)
        if result is False:
            print("结束端口号为{0}服务失败".format(_port))
            return
        print("结束端口号为{0}服务成功".format(_port))

    def port_is_running(self, port):
        """
        Tries to connect to the server at port to see if it is running.
        :Args:
         - port - The port to connect.
        """
        socket_ = None
        host = "localhost"
        try:
            socket_ = socket.create_connection((host, port), 1)
            result = True
        except socket.error:
            print("socket.error....555...555")
            result = False
        finally:
            if socket_:
                socket_.close()
        return result

    def close_file(self, file_path, port):
        """如果进程结束，关闭异步关闭文件"""
        while self.port_is_running(port):
            time.sleep(1)
        if operate_file.OperateFile(file_path).check_file():
            self.log_file.close()

    def start(self):
        result = {
            "code": None,
            "pid": None,
            "gpid": None
        }
        if not self.port_is_running(config.grid_port):      # 判断 grid 是否在运行
            print("Please start the grid service first !!")
            result["code"] = 12004
            return result

        if self.port_is_running(self.appium_port):      # 判断 appium 是否在运行
            if not self.kill_pid_with_port(self.appium_port):
                if self.port_is_running(self.appium_port):
                    result["code"] = 12003
                    print("kill port failed, port {0} is running!".format(self.appium_port))
                    raise RuntimeError

        self.device["appium_ip"] = self.appium_ip
        self.device["appium_port"] = self.appium_port
        self.device["grid_ip"] = config.grid_ip
        self.device["grid_port"] = config.grid_port

        try:
            config_path = NodeConfigJson(self.device).create_node_config()

            self.args_list = ['appium',
                              '--port', self.appium_port,
                              '--bootstrap-port', self.appium_bport,
                              '--session-override',
                              '--nodeconfig', config_path]

            current_time = time.strftime('%Y_%m_%d_%H_%M_%S')
            self.log_path = self.abs_path("/home/log/appium/{0}_{1}.log".format(current_time, self.device["name"]))
            self.log_file = open(self.log_path, 'w+')

            self.start_p = subprocess.Popen(
                self.args_list,
                shell=False,
                stdout=self.log_file,
                stderr=self.log_file,
                preexec_fn=os.setsid        # 这个不能少，因为要创建一个进程组
            )
            result["pid"] = self.start_p.pid
            result["gpid"] = os.getpgid(self.start_p.pid)
            count = 0
            while True:
                if self.port_is_running(self.appium_port):
                    break
                count += 1
                time.sleep(1)
                if count == 30:
                    self.log_file.close()
                    result["code"] = 12002
                    raise ConnectionError

            time.sleep(8)  # 服务开启之后要等几秒，不然到driver推送到grid时，会识别不了
            print('%s : ' % time.ctime(), '%s appium service open successfully!' % self.device['name'])
            print('%s : ' % time.ctime(), '%s appium service url is: %s:%s' % (self.device['name'], self.appium_ip, self.appium_port))
            result["code"] = 12001

            # 异步关闭已打开的文件
            close_file_p = multiprocessing.Process(target=self.close_file, args=(self.log_path, self.appium_port))
            close_file_p.start()

            # 异步结束未关闭的appium服务
            close_appium = multiprocessing.Process(target=self.async_kill_appium, args=(self.appium_port, ))
            close_appium.start()

        except ConnectionError:
            print("Can not connect to the Service appium !!")
            if self.start_p is not None:
                self.start_p.kill()
                self.log_file.close()
        finally:
            print(result)
            return result


def my_main(device=None):

    if device is None:
        # device = {
        #         'name': 'M3NOTE3',
        #         'udid': '91QEBPF5S4WM',
        #         'version': '5.1',
        #         'platform': 'Android',
        #         'port': '4725'
        #     }
        result = {
            "code": 12001,
            "pid": None,
            "gpid": None
        }
    else:
        appium = AppiumService(device)
        result = appium.start()
    return result


# if __name__ == "__main__":
#     device = {
#         'name': 'HUAWEIP9',
#         'udid': '123456',
#         'version': '7.0',
#         'platform': 'Android',
#         'port': '4723'
#     }
#     appium = AppiumService(device)
#     result = appium.start()
#     print(result)

