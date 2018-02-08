
import subprocess
import time
import os
import socket
from subprocess import CalledProcessError


class StopAppium:
    def __init__(self, device):
        self.device = device
        self.pid = int(self.device["pid"])
        self.appium_port = self.device["port"]

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
    #         if not self.port_is_running(self.appium_port):
    #             raise RuntimeError
    #
    #         kill_cmd = "netstat -tnlp | grep {0} | cut -c 81-84 | xargs kill -s 9".format(self.appium_port)
    #         self.stop_p = subprocess.check_call(kill_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)
    #
    #         print('%s : status code: ' % time.ctime(), self.stop_p)
    #         print('%s : ' % time.ctime(), 'appium service stop successfully! ')
    #         result = 12001
    #     except CalledProcessError as e:
    #         print("killing java.exe service fail:\n", e)
    #         result = 12002
    #     except RuntimeError:
    #         print("appium service is not running in port:{0}".format(self.appium_port))
    #         result = 12002
    #     finally:
    #         return result

    def stop(self):
        result = {
            "code": None,
        }
        print("即将要杀死的设备：{0}".format(self.device))
        try:
            if not self.port_is_running(self.appium_port):
                result["code"] = 12002
                print("要杀死的端口不存在")
                return result

            os.killpg(self.pid, 9)
            result["code"] = 12001
            print("杀死appium进程成功{0}".format(self.device))
            return result
        except:
            result["code"] = 12002
            print("kill failed !!!")
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
            "code": 12002,
        }
    else:
        appium = StopAppium(device)
        result = appium.stop()
    return result


# if __name__ == "__main__":
#     device = {
#         'name': 'HUAWEIP9',
#         'udid': '123456',
#         'version': '7.0',
#         'platform': 'Android',
#         'port': '4723'
#     }
#     appium = StopAppium(device)
#     appium.stop()

