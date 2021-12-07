# 视图
- 作用：负责业务逻辑,并在适当时候调用模型和模板
### 1.视图概念
- 视图即视图函数，接收web请求并返回web响应，事物处理函数。
- 响应指符合http协议要求的任何内容，包括json，string，html等
- 本章忽略事务处理，重点在如何返回处理结果上

- views的功能
    - 业务处理
    - 返回response子类
        - 拿到模板
        - 拿到数据
        - 环境变脸
        - 返回
### 2.其他简单视图
- django.http给我们提供了很多类似HTTPResponse的简单视图
- from django.http import HttpResponse查看其中的http包含的函数（ctrl+左键）
- 此类视图使用方法基本类似，可通过return语句直接反馈给浏览器
### 3.HTTPResponse详解
- 方法：
    - init: 使用页内容实例化HttpResponse对象
    - write(content): 以文件的方式写
    - flush(): 以文件的方式输出缓存区
    - set_cookie(key, value='', max_age=None, expires=None): 设置cookie
        - key, value都是字符串类型
        - max_age是一个整数，表示在指定秒数后过期
        - expires是一个datetime或timedelta对象，会话将在这个指定的日期/时间过期
        - max_age与expires二选一
        - 如果不指定过期时间，则两个星期后过期
    - delete_cookie(key): 删除指定的key的cookie，如果key不存在则什么也不发生
### 4.HttpResponseRedirect
- 重定向，服务器端跳转 （访问原来的地址不合适了，再访问原来的地址时跳转到新的地址）
- 构造函数的第一个参数用来指定重定向的地址
- 案例：
    '''
    urls.py中添加：
        url(r'^v10_1/', tv.v10_1),
        url(r'^v10_2/', tv.v10_2),
        url(r'^v11/', tv.v11, name='v11'),
    '''
    '''
    views.py中添加：
        def v10_1(r):
            return HttpResponseRedirect('/v11')
            
        def v10_2(r):
            return  HttpResponseRedirect(reverse('v11'))
            
        def v11(r):
            return HttpResponse("这是v11的访问返回")   
    '''
### 5.Request对象
- 简介：
    - 服务器接收到http协议的请求后，会根据报文创建HttpRequest对象
    - 视图函数的第一个参数是HttpRequest对象
    - 在django.http模块中定义了HTTPRequest对象的API
- 属性
    - 下面除非特别说明，属性都是只读的
    - path：一个字符串，表示请求的页面的完整路径，不包含域名
    - method：一个字符串，表示请求使用的HTTP方法，常用值包括：'GET','POST'
    - encoding: 一个字符串，表示提交的数据的编码方式
        - 如果为None则表示使用浏览器的默认设置，一般为utf-8
        - 这个属性是可写的，可以通过修改它来修改访问表单数据使用的编码
    - GET：一个类似于字典的对象，包含get请求方式的所有参数
    - POST: 一个类似于字典的对象，包含post请求方式的所有参数
    - FILES: 一个类似于字典的对象，包含所有的上传文件
    - COOKIES: 一个标准的python字典，包含所有的cookie，键和值都为字符串
    - session: 一个既可读又可写的类似于字典的对象，表示当前的会话，
        - 只有当Django启用会话的支持时才可用
- 方法
    - is_ajax(): 如果请求是通过XMLHttpRequest发起的，则返回True

- QueryDict对象
    - 定义在django.http中
    - request对象的属性GET, POST都是QueryDict类型
    - 与python字典不同，QueryDict类型的对象用来处理同一个键带有多个值的情况
    - 方法get(): 根据键获取值
        - 只能获取键的一个值
        - 如果一个键同时拥有多个值，获取最后一个值
    - 方法getlist(): 根据键获取值
        - 将键的值以列表返回，可以获取一个键的多个值
- GET属性
    - QueryDict类型的对象
    - 包含get请求方式的所有参数
    - 与url请求地址中的参数对应，位于？后面
    - 参数的格式是键值对，如key1=value1
    - 多个参数之间，使用&连接，如key1=value1&key2=value2
    - 键是开发人员定下来的，值是可变的
- POST属性
    - QueryDict类型的对象
    - 包含post请求方式的所有参数
    - 与form表单中的控件对应
    - 表单中控件必须有name属性，name为键，value为值
        - checkbox存在一键多值的问题
    - 【案例】：
         - 在项目文件下创建一个存放其他类型文件的文件夹templates
            - 新建for_post.html文件，编写表单
         - 由于在项目下新建了文件夹，所以需要在settings.py中配置，不然找不到新建文件夹下的文件
            -  setting.py文件中找到TEMPLATES, 添加  'DIRS': [os.path.join(BASE_DIR, 'templates')],
         '''
         urls.py：
            url(r'^v9_get/', tv.v9_get),
            url(r'^v9_post', tv.v9_post),
            
         views.py:
            def v9_get(request):
                # 渲染模板并返回
                return render_to_response("for_post.html")

            def v9_post(request):
                ...
         '''    
         - 访问127.0.0.1:8000/v9_get/
            - 发现可以访问，然后填写表单，提交，发现报错
            - 原因：是由于安全问题，导致无法访问
            - 解决方法：在setting.py文件中找到MIDDLEWARE，然后注释掉django.middleware.csrf.CsrfViewMiddleware
            - 当然，只是看下效果，还是取消注释
- 手动编写视图
    - 实验目的：
        - 利用django快捷函数手动编写视图处理函数
        - 编写过程中理解视图运行的原理
    - 分析：
        - django把所有请求信息封装入request
        - django通过urls模块把相应请求跟事件处理函数(视图里的函数)链接起来，并把request作为参数传入视图函数
        - 在相应的处理函数中，我们需要完成两部分
            - 处理业务
            - 把结果封装并返回，我们可以使用简单HTTPResponse
        - 本案例不介绍业务处理，把目光集中在如何渲染结果并返回
- render函数
    - render(request, template_name[, context][,...]）
        - 结合一个给定的模板和一个给定的上下文字典，并返回一个渲染后的HttpResponse对象。
    - 参数：
        - request： 用于生成响应的请求对象。
        - template_name：要使用的模板的完整名称，可选的参数
        - context：添加到模板上下文的一个字典。默认是一个空字典。如果字典中的某个值是可调用的，视图将在渲染模板之前调用它。
        - content_type：生成的文档要使用的MIME类型。默认为DEFAULT_CONTENT_TYPE 设置的值。
        - status：响应的状态码。默认为200。
        - 【案例】views.py中的render_test()函数
    - 作用：render方法主要是将从服务器提取的数据，填充到模板中，然后将渲染后的html静态文件返回给浏览器。
    - 这里一定要注意：render渲染的是模板。
    
- 系统内建视图
    - 系统内建视图，可以直接使用
    - 404
        - default.page_not_found(request, template_name='404.html')
        - 系统引发Http404时触发
        - DEBUG=True则不会调用404，取而代之的是调试信息
        - 404视图会被传递一个RequestContext对象并且可以访问模板上下文处理器提供的变量
     
    - 500（server error）
        - default.server_error(request, template_name='500.html')
        - 需要DEBUG=False，否则不调用
    - 403（HTTP Forbidden）
        - default.permission_denied(request, template_name='403.html')
        - 通过PermissionDenied触发
    - 400（bad request）
        - default.bad_request(request, template_name='400.html')
        - DEBUG=False
    - 【案例：views.py中的 get404() 函数】
    
### 基于类的视图
    - 即封装成类
        