
import config
import time
import os
import socket
import subprocess


class ConnectSTF:

    def __init__(self, con_ip, con_port="5037"):
        self.con_ip = con_ip
        self.con_port = con_port

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

    def start(self):
        return_list = list()
        if self.port_is_running(config.stf_port):
            print("stf is running!")
            return_list += [12003, None]
            return return_list

        # 开启STF
        con_str = "stf provider " \
                  "--name localhost " \
                  "--min-port 7400 " \
                  "--max-port 7700 " \
                  "--connect-sub tcp://192.168.2.233:7114 " \
                  "--connect-push tcp://192.168.2.233:7116 " \
                  "--group-timeout 2000 " \
                  "--public-ip 192.168.2.233 " \
                  "--storage-url http://192.168.2.233:7100/ " \
                  "--adb-host {0} " \
                  "--adb-port {1} " \
                  "--vnc-initial-size 600x800 " \
                  "--allow-remote".format(self.con_ip, self.con_port)
        con_list = con_str.split()
        try:
            start_p = subprocess.Popen(con_list, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, preexec_fn=os.setsid)

            if start_p is None:
                print("mobile connect to stf 失败")
                return_list += [12002, None]
                return return_list

            count = 0
            while True:
                if count == 30:
                    print("mobile connect to stf 失败")
                    return_list += [12002, None]
                    start_p.kill()
                    return return_list

                if start_p.pid is None:
                    count += 1
                    time.sleep(1)
                    continue
                else:
                    break
            con_pid = start_p.pid
            con_gpid = os.getpgid(con_pid)
            return_list += [12001, con_gpid]
            print("连接成功！")
            start_p.kill()
            return return_list
        except:
            print("mobile connect to stf 异常退出")
            return_list += [12002, None]
            return return_list


def my_main(con_ip,con_port="5037"):
    con_stf = ConnectSTF(con_ip, con_port)
    return_code = con_stf.start()
    return return_code
