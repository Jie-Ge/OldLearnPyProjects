from django.shortcuts import render
from django.http import HttpResponse, Http404

from django.urls import reverse

# Create your views here.

# =======  介绍 路由--urls ================

'''
视图函数需要一个参数，类型是HttpRequest
'''
# 添加的函数
def do_normalmap(request):
    print("本控制台显示，检查是否调用")
    return HttpResponse("This is a normalmap")


def withparam(request, year, month):
    return HttpResponse("This ia with param {0}, {1}".format(year, month))


def do_app(request):
    return HttpResponse("这是子路由")

# 参数page_number，要与urls.py中的参数名一样
def do_myindex_2(r, page_number):
    return HttpResponse("Page number is {0}".format(page_number))


def extremParam(r, name):
    return HttpResponse("your name is {0}".format(name))


def revParse(r):
    return HttpResponse("your requested URL is {0}".format(reverse('revvurl')))


# =============== 介绍视图 ==============

def teacher1(r):
    return HttpResponse("没错，这就是teacher1的一个视图")

# 抛出异常
def v2_exception(r):
    raise Http404
    return HttpResponse("OK")