"""test_backstage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

from backstage import views


urlpatterns = [
    path('', views.main),
    path('accounts/login/', views.main),
    path('admin/', admin.site.urls),

    path('backstage/', include('backstage.urls')),
    path('uiautotest/', include('uiautotest.urls')),
    path('ifautotest/', include('ifautotest.urls')),

    path('test/', views.test),
]
