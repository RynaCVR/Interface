# coding = utf-8
"""
resource: https://github.com/appium/appium/blob/master/docs/cn/advanced-concepts/grid.md

"""

import json
import os

import uiautotest.server.config as config
from uiautotest.server.common import operate_file


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class NodeConfigJson(object):
    """
    device = {
        'name': 'HUAWEIP9',
        'udid': '123456',
        'version': '7.0',
        'platform': 'Android',
        'appium_ip': '127.0.0.1',
        'appium_port': '4723',
        'grid_ip': '127.0.0.1',
        'grid_port': '4444',
    }
    """

    def __init__(self, device):
        self.device = device

    def config_exist(self, device_name):
        config_path = './nodeconfig/config_%s.json' % device_name
        config_path = PATH(config_path)
        return operate_file.OperateFile(config_path).check_file()

    def modify_config(self):

        node_config = None
        if config.grid_version == "3.6.0":
            node_config = config.node_config_3
            node_config['capabilities'][0]['browserName'] = self.device['udid']
            node_config['capabilities'][0]['version'] = str(self.device['version'])
            node_config['capabilities'][0]['platform'] = self.device['platform']

            node_config['port'] = self.device['appium_port']
            node_config['hub'] = "http://{0}:{1}".format(self.device['grid_ip'], self.device['grid_port'])

        elif config.grid_version == "2.53.1":
            node_config = config.node_config_2
            node_config['capabilities'][0]['browserName'] = self.device['udid']
            node_config['capabilities'][0]['version'] = str(self.device['version'])
            node_config['capabilities'][0]['platform'] = self.device['platform']
            # node_config['configuration']['url'] = 'http://%s:%s/wd/hub' % (self.device['appium_ip'], self.device['appium_port'])
            node_config['configuration']['url'] = 'http://%s:%s/wd/hub' % (self.device["appium_ip"], self.device['appium_port'])
            node_config['configuration']['host'] = self.device['appium_ip']
            node_config['configuration']['port'] = self.device['appium_port']
            node_config['configuration']['hubPort'] = self.device['grid_port']
            node_config['configuration']['hubHost'] = self.device['grid_ip']

        else:
            print("error")

        return node_config

    def create_node_config(self):
        config_path = './nodeconfig/config_%s.json' % self.device['name']
        config_path = PATH(config_path)

        node_config = self.modify_config()
        fp = open(config_path, 'w')
        json.dump(node_config, fp)
        fp.close()
        return config_path


# if __name__ == '__main__':
#     device = {
#         'name': 'HUAWEIP9',
#         'udid': '41142219921010',
#         'version': '7.0',
#         'platform': 'Android',
#         'appium_ip': '127.0.0.1',
#         'appium_port': '4723',
#         'grid_ip': '127.0.0.1',
#         'grid_port': '4444',
#     }
#
#     NodeConfigJson(device).create_node_config()
