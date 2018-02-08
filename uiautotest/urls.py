# coding=utf-8


from django.urls import path
from uiautotest import views


urlpatterns = [
    path('grid/start/', views.grid_start, name='grid_start'),
    path('grid/stop/', views.grid_stop, name='grid_stop'),
    path('appium/start/', views.appium_start, name='appium_start'),
    path('appium/stop/', views.appium_stop, name='appium_stop'),
]

