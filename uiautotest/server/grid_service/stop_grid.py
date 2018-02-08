import time
import subprocess
import socket
import os
import uiautotest.server.config as config
from subprocess import CalledProcessError
import signal


class StopGrid:
    def __init__(self, pid):
        self.stop_p = None
        self.pid = int(pid)

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

    # def stop(self):
    #     """1.0版本"""
    #     result = None
    #     try:
    #         if not self.port_is_running(config.grid_port):
    #             raise RuntimeError
    #
    #         # cmd_kill_java = 'taskkill /f /t /im java.exe'     # 用于windows
    #         cmd_kill_java = "netstat -tnlp | grep {0} | cut -c 81-84 | xargs kill -s 9".format(config.grid_port)
    #
    #         self.stop_p = subprocess.check_call(cmd_kill_java, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)     #windows下shell改成
    #
    #         print('%s : status code: ' % time.ctime(), self.stop_p)
    #         print('%s : ' % time.ctime(), 'grid service stop successfully!')
    #         result = 12001
    #     except CalledProcessError as e:
    #         print("killing java.exe service fail:\n", e)
    #         result = 12002
    #     except RuntimeError:
    #         print("Maybe the service isn't running !")
    #         result = 12002
    #     finally:
    #         return result

    def stop(self):
        """2.0版本"""
        result = {
            "code": None,
        }
        print("即将要杀死进程组为：{0}".format(self.pid))
        try:
            if not self.port_is_running(config.grid_port):
                result["code"] = 12002
                print("没有在运行grid")
                return result

            os.killpg(self.pid, 9)
            result["code"] = 12001
            print("杀死进程组成功：{0}".format(self.pid))
            return result
        except Exception:
            result["code"] = 12002
            print("kill failed !!!")
            return result


def my_main(pid):
    grid = StopGrid(pid)
    result = grid.stop()
    return result
