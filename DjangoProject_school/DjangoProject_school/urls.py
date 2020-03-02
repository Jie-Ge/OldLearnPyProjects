"""firstDjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from teacher import views as tv

from django.conf.urls import  include, url
from teacher import teacher_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # 添加的
    # 视图函数只有名称，无括号和参数
    path(r'normalmap/', tv.do_normalmap),  # path不支持正则

    # 【例2】

    #  尖号表示匹配以后面内容开头的url
    #  圆括号表示的是一个参数( ?P 表示参数)，里面的内容作为参数传递给被调用的函数
    #  参数名称以问好加大写P开头，尖括号里就是参数的名字
    #  尖括号后表示正则，用于描述参数
    #  大括号表示出现的次数，此处4表示只能出现4个0-9的数字
    url(r'^withparam/(?P<year>[0-9]{4})/(?P<month>[0,1][0-9])', tv.withparam),

    # 凡是由teacher开头的url都交给teacher模块处理
    url(r'^teacher/', include(teacher_urls)),

    # 捕获参数
    # 参数page_number，要与views.py中的参数名一样
    url(r'index_2/(?:page-(?P<page_number>\d+)/)$', tv.do_myindex_2),

    # 传递额外参数, 参数名要相同
    url(r'extrem/$', tv.extremParam, {'name': 'liuying'}),

    # URL的反向解析（替换网址）
    url(r'toolongurlllllll/', tv.revParse, name='revvurl'),


    # ========== 下面介绍视图 ===================

    url(r'^teacher/', tv.teacher1),

    url(r'^v2_exp/', tv.v2_exception),
]
