from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect, QueryDict

from django.urls import reverse

from django.shortcuts import render_to_response

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


# ****************** 介绍视图 ***********************

def teacher1(r):
    return HttpResponse("没错，这就是teacher1的一个视图")

# 抛出异常
def v2_exception(r):
    raise Http404
    return HttpResponse("OK")


def v9_get(request):
    # 渲染模板并返回
    return render_to_response("for_post.html")


def v9_post(request):
    rst = ''
    for k, v in request.POST.items():
        rst += k + '-->' + v + ','
    return HttpResponse("Get value of POST is {0}".format(rst))

def render_test(request):

    # 环境变量
    c = dict()

    # 变量名与模板(render_test.html)中变量名一致
    c['name'] = 'jiege'

    # 没有配置的话，要先在setting.py文件中配置，views.py中有配置方法
    # context: 传入变量值
    rsp = render(request, 'render_test.html', context=c)

    '''
    另一种写法，作用相同：
        from django.template import loader 
        # 得到模板实例
        t = loader.get_template("render_test.html")
        
        rsp = t.render({"name": "jiege"})
        
        return HttpResponse(rsp)
    '''

    return rsp

def get404(request):
    from django.views import defaults

    # 也可使用自定义的模板
    # return defaults.page_not_found(request, template_name='render_test.html')
    return defaults.page_not_found(request, Exception)


# ****************  模板 ****************************

def one(request):
    ct = dict()

    ct['score'] = [60, 70, 80, 90]
    return render(request, r'one.html', context=ct)


# **************** session ***********

def mySession(request):
    print(request.session)

    # 返回session中的teacher_name的值，如果没有，则返回NoName
    print(request.session.get("teacher_name", "NoName"))

    return None

# ************* 分页 *************

def teacher_(request):
    '''
    请求所有老师(10000名)的详情列表
    :param request:
    :return:
    '''
    from django.core.paginator import Paginator

    # 导入models.py, 使用其中的类
    from teacher import models

    # 因为有10000条数据，全部返回到页面，不行
    # 所以需要分页

    # 老师的数据
    tea = models.Teacher.objects.all()

    # 两个参数：
    # 1. 数据来源，也即从数据库中查询出的结果
    # 2. 每一页返回的数据量
    p = Paginator(tea, 20)

    # 可以对Paginator进行设置或者使用其属性
    print(p.count)  # p里面有多少条数据
    print(p.num_pages)  # 页面总数
    print(p.page_range)  # 页码列表，从1开始

    # 取得第3页
    # 如果页码不存在，则报异常InvalidPage
    p.page(3)

    return p

# *************** 类的视图 ****************

from django.views.generic import ListView

from teacher import models

class TeacherListView(ListView):
    '''
    需要设置两个内容：
    1. queryset：数据来源集合
    2. template_name: 模板名称
    '''

    queryset = models.Teacher.objects.all().filter(age=18)

    template_name = "name.html"