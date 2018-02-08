
from django.urls import path
from ifautotest import views


urlpatterns = [
    path('index/', views.ifautotest_index, name='ifautotest_index'),
    path('run_ifautotest', views.run_ifautotest, name='run_ifautotest')
]
