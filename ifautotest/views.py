
# Create your views here.


from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.urls import reverse


from ifautotest.ifmain.common import user_send_email


@login_required
def ifautotest_index(request):
    return render(request, 'index.html')


@login_required
def run_ifautotest(request):
    user_email = request.GET.get('user_email', '')
    print(user_email)
    user_send_email.my_main(user_email)
    return HttpResponseRedirect(reverse('ifautotest_index'))
