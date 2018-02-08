from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.urls import reverse


from backstage.operation import modify_loan_order
from backstage.operation import select_table
from backstage.operation import run_script as run_script_haha

# Create your views here.

def main(request):
    """首页跳转至登录"""
    # return HttpResponseRedirect('/backstage/login/')
    return HttpResponseRedirect(reverse('login'))


def login(request):
    """登录"""
    return render(request, 'login.html')


def login_action(request):
    """登录跳转"""
    if request.method == 'POST':
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            request.session['user'] = username
            # return HttpResponseRedirect('/backstage/test_home/')
            return HttpResponseRedirect(reverse('test_home'))
        else:
            return render(request, 'login.html', {'error': 'username or password error!'})
    else:
        return render(request, 'login.html', {'error': 'request method error!'})


@login_required
def test_home(request):
    """测试后台home页"""
    # username = request.session.get('user', '')
    return render(request, 'test_home.html')


@login_required
def db_sms_verify(request):
    """测试后台db页"""
    sms_data = select_table.select_sms('jjb')
    return render(request, 'sms_verify.html', {'sms_db_name': 'jjb', 'sms_data': sms_data})


@login_required
def db_run_script(request):
    """常用脚本执行"""
    return render(request, 'run_script.html')



@login_required
def db_modify_order(request):
    """修改订单数据"""
    return render(request, 'modify_order.html')


@login_required
def modify_order_status(request):
    """修改订单状态码"""
    order_num = request.GET.get("order_num", "")
    status = request.GET.get("status", "")
    modify_loan_order.modify_status(order_num, status)

    return HttpResponseRedirect(reverse('modify_order'))


@login_required
def modify_order_due_day(request):
    """修改订单逾期天数"""
    order_num = request.GET.get("order_num", "")
    due_day = request.GET.get("due_day", "")
    modify_loan_order.modify_order_due_day(order_num, due_day)

    return HttpResponseRedirect(reverse('modify_order'))


@login_required
def select_sms(request):
    """查询短信验证码"""
    db_name = request.GET.get('db_name')
    sms_data = select_table.select_sms(db_name)
    return render(request, 'sms_verify.html', {'sms_db_name': db_name, 'sms_data': sms_data})


@login_required
def run_script(request):
    """运行常用脚本"""
    script_name = request.GET.get('script_name', '')
    if script_name == 'auto_payment':
        run_script_haha.auto_payment()
    elif script_name == 'delay_back_loan':
        a = run_script_haha.auto_delay_back_loan()
        print(a)
    elif script_name == 'sys_push':
        a = run_script_haha.sys_push()
        print(a)
    return render(request, 'run_script.html')


def test(request):
    """bootstrap 学习"""
    return render(request, 'test.html')
