
from django.urls import path
from backstage import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('login_action/', views.login_action, name='login_action'),

    path('test_home/', views.test_home, name='test_home'),

    # 短信验证页面
    path('test_db/sms_verify/', views.db_sms_verify, name='sms_verify'),
    path('test_db/select_sms/', views.select_sms, name='select_sms'),


    # 订单修改页面
    path('test_db/modify_order/', views.db_modify_order, name='modify_order'),
    path('test_db/modify_order_status/', views.modify_order_status, name='modify_order_status'),
    path('test_db/modify_order_due_day/', views.modify_order_due_day, name='modify_order_due_day'),

    path('test_db/run_script/', views.db_run_script, name='run_script'),
    path('test_db/run_script_haha/', views.run_script, name='run_script_haha'),
]
