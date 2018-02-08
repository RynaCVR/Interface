#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import socket
import subprocess
import time
import copy
import multiprocessing

import uiautotest.server.config as config
import uiautotest.server.common.operate_file as operate_file


class StartGrid(object):

    def __init__(self):
        self.jar_path = "../common/selenium-server-standalone-{0}.jar".format(config.grid_version)
        self.jar_path = self.abs_path(self.jar_path)
        # print("jar_path", self.jar_path)
        self.cmd = ['java', '-jar', self.jar_path, '-role', 'hub', '-hub', config.grid_ip, '-host', config.grid_ip, '-hubHost', config.grid_ip, '-port', config.grid_port]

    def abs_path(self, path):
        PATH = lambda p: os.path.abspath(
            os.path.join(os.path.dirname(__file__), p)
        )
        return PATH(path)

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
            result = False
        finally:
            if socket_:
                socket_.close()
        return result

    def close_file(self, file_path, port):
        """异步关闭打开的文件；如果端口不存在，则关闭文件"""
        while self.port_is_running(port):
            time.sleep(1)
        if operate_file.OperateFile(file_path).check_file():
            self.log_file.close()

    def async_kill_grid(self, port):
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

    def start(self):
        """
        result:
            None or 0，error
            1, success
            2, is running
        :return:
        """
        result = {
            "code": None,
            "pid": None,
            "gpid": None
        }
        try:
            if self.port_is_running(config.grid_port):
                if not self.kill_pid_with_port(config.grid_port):
                    if self.port_is_running(config.grid_port):
                        result["code"] = 12003
                        print("kill port failed, port {0} is running!".format(config.grid_port))
                        raise RuntimeError

            current_time = time.strftime("%Y%m%d%H%M%S")
            self.log_path = self.abs_path("/home/log/grid/gridlog_{0}.log".format(current_time))
            self.log_file = open(self.log_path, mode="wb")
            while not operate_file.OperateFile(self.log_path, method="wb").check_file():
                time.sleep(1)
            # print("log_path:", self.log_path, "cmd:", self.cmd)
            self.start_p = subprocess.Popen(
                self.cmd,
                shell=False,
                stdout=self.log_file,
                stderr=self.log_file,
                preexec_fn=os.setsid
            )
            result["pid"] = self.start_p.pid
            result["gpid"] = os.getpgid(self.start_p.pid)
            count = 0
            while True:
                if self.port_is_running(config.grid_port):
                    break
                count += 1
                print(count)
                time.sleep(1)
                if count == 30:
                    result["code"] = 12002
                    raise ConnectionError

            print('%s : ' % time.ctime(), 'grid service start successfully!')
            print('%s : ' % time.ctime(), 'grid service url is: %s:%s' % (config.grid_ip, config.grid_port))
            result["code"] = 12001

            # 异步关闭打开的文件
            close_file_p = multiprocessing.Process(target=self.close_file, args=(self.log_path, config.grid_port))
            close_file_p.start()

            # 异步关闭grid
            close_grid = multiprocessing.Process(target=self.async_kill_grid, args=(config.grid_port, ))
            close_grid.start()

        except ConnectionError:
            print('%s : Can not start grid service!!' % time.ctime())
            self.start_p.kill()
            self.log_file.close()
            result = 12002
        except RuntimeError:
            print("%s : grid service is running!!" % time.ctime())
        finally:
            print(result)
            return result


def my_main():
    grid = StartGrid()
    result = grid.start()
    return result


if __name__ == "__main__":
    # result = StartGrid().start()
    # print(result)
    # my_main()
    pass
