

self_ip = "192.168.2.233"

grid_version = "2.53.1"     # 2.53.1 or 3.6.0
grid_ip = self_ip
# grid_ip = "127.0.0.1"
grid_port = "4444"

appium_ip = self_ip
# appium_ip = "127.0.0.1"

stf_ip = self_ip
stf_port = "7100"

node_config_2 = {
  "capabilities":
      [
          {
              "browserName": "<e.g._iPhone5_or_iPad4>",  # device name
              "version": "<version_of_iOS_e.g._7.1>",  # device os version
              "maxInstances": 1,
              "platform": "<platform_e.g._MAC_or_ANDROID>"  # iOS or Android
          }
      ],
  "configuration":
      {
          "cleanUpCycle": "2000",
          "timeout": "30000",
          "proxy": "org.openqa.grid.selenium.proxy.DefaultRemoteProxy",
          "url": "http://<host_name_appium_server_or_ip-address_appium_server>:<appium_port>/wd/hub",
            # appium service ip:port
          "host": "<host_name_appium_server_or_ip-address_appium_server>",  # appium service ip
          "port": "<appium_port>",  # appium service port
          "maxSession": "1",
          "register": True,
          "registerCycle": "5000",
          "hubPort": "<grid_port>",  # grid service port
          "hubHost": "<Grid_host_name_or_grid_ip-address>"  # grid service ip
      }
}


node_config_3 = {
    "capabilities": [{
        "browserName": "",      # device name
        "version": "",      # os version
        "platform": "",     # iOS or Android
        "maxInstances": 5,
        "seleniumProtocol": "WebDriver"
    }],
    "proxy": "org.openqa.grid.selenium.proxy.DefaultRemoteProxy",
    "maxSession": 1,
    "port": 5555,   # appium service port
    "register": True,
    "registerCycle": 5000,
    "hub": "http://localhost:4444",     # grid service ip:port
    "nodeStatusCheckTimeout": 5000,
    "nodePolling": 5000,
    "role": "node",
    "unregisterIfStillDownAfter": 60000,
    "downPollingLimit": 2,
    "debug": False,
    "servlets": [],
    "withoutServlets": [],
    "custom": {}
}
