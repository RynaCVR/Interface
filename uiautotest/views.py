from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# SUCCESS: 12001
# FAIL: 12002
# RUNNING = 12003


import uiautotest.server.common.common_lib as common_method

import uiautotest.server.appium_service.start_appium as start_appium
import uiautotest.server.appium_service.stop_appium as stop_appium

import uiautotest.server.grid_service.start_grid as start_grid
import uiautotest.server.grid_service.stop_grid as stop_grid


def grid_start(request):
    """启动grid"""
    return_code = start_grid.my_main()
    return HttpResponse(str(return_code))


def grid_stop(request):
    """停止grid"""
    pid_dic = dict(request.GET)        # 拿到参数
    return_code = stop_grid.my_main(pid_dic["pid"])
    return HttpResponse(str(return_code))


def appium_start(request):
    """启动appium"""
    device_args = dict(request.GET)        # 拿到参数
    return_code = start_appium.my_main(device_args)
    return HttpResponse(str(return_code))


def appium_stop(request):
    """结束appium"""
    device_args = dict(request.GET)     # 拿到参数
    return_code = stop_appium.my_main(device_args)
    return HttpResponse(str(return_code))


