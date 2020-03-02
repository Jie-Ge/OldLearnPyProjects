# Django的使用：
- 创建django项目
    - 进入安装有Django的conda环境下
    - django-admin startproject DjangoProject_name : 创建django项目
    -  cd DjangoProject_name : 进入项目文件
    
- 启动自带的服务器
    -  命令行启动
        - conda进入到相应环境下，cd到项目文件
        - python manage.py runserver [可指定端口号]: 启动的是 Django 自带的用于开发的简易服务器
    - pycharm启动
        - 需要配置
        - 1. 需用有django的环境下的python解释器 python.exe
        - 2. pycharm界面上方的"manage"下拉，选择 "Edit Configurations"
        - 3. 在Parameters一栏出填上“runserver”
        - 4. 运行‘manage.py’文件，ok
        - 可用浏览器访问给出的ip地址，控制台会反馈访问信息，状态

- 创建APP
    - app: 负责一个具体业务或者一类具体业务的模块
    - conda进入到相应环境下，cd到项目文件
    - python manage.py startapp app_name
    
# 路由系统-urls
- 路由（看门大爷，前台，领路人）
    - 按照具体的请求url，导入到相应的业务处理模块的一个功能模块
    - django的信息控制中枢
    - 本质上是接收的URL和相应的处理模块的一个映射
    - 在接收URL请求的匹配上使用了RE
    - URL的具体格式如urls.py中所示
    
- 需要关注两点
    1. 接受的URL是什么，即如何用RE对传入的URL进行匹配
    2. 已知URL匹配到哪个处理模块

- url匹配规则
    - 从上往下一个一个比对
    - url格式是分级格式，则按照级别一级一级往下比对，主要对应url包含子url的情况
    - 子url一旦被调用，则不会返回到主url
        - '/one/two/three/'
    - 正则以r开头，表示不需要转义，注意尖号（^）（从头匹配）和美元符号（$）（从尾匹配）
        - '/one/two/three/' 配对 r'^one/'
        - '/oo/one/two/three/' 不配对 r'^one/'
        - '/one/two/three/' 配对 r'three/$'
        - '/oo/one/two/three/oo/' 不配对 r'three/$'
        - 开头不需要反斜杠
    - 如果从上向下都没有找到合适的匹配内容，则报错
    
- 1. 正常映射
- 把某一个符合RE的URL映射到事物处理函数中去
    - 举例如下：
        （一）urls.py文件：
        '''
        from teacher import views as tv
        urlpatterns = {
            path('admin/', admin.site.urls),
            path(r'normalmap/', tv.do_normalmap),
        }
        '''
        
        （二）创建的app(teacher文件)中：views.py文件
        '''
        def do_normalmap(request):
            pass
        '''
        
        （三）运行manage.py文件，访问，查看效果
        127.0.0.1:8000/normalmap/

- 2. URL中带参数的映射    
- 在事件处理代码中需要由URL传入参数，型如 /myurl/param中的param
- 参数都是字符串形式，如果需要整数等形式需要自行转换
- 通常的形式如下：
    '''
        /search/page/432 中的432需要经常性变换
    '''
    如urls.py文件中的【例2】

- 3. URL在app中的处理
    - 如果所有应用URL都集中在DjangoProject/urls.py中，可能导致文件的臃肿
    - 可以把urls具体功能逐渐分散到每个app中
        - 从django.conf.urls 导入 include
        - 注意此时RE部分的写法
        - 添加include导入
    - 同样可以使用参数
    - 方法：
        - 主路由（school文件）/urls.py 添加主路由的开头url：
            '''
                from django.conf.urls import  include, url
                from teacher import teacher_urls
                path(r'^teacher/', include(teacher_urls))
            '''
        - 子路由（teacher文件）下新建teacher_urls.py，
            - 添加匹配子路由：path(r'student1/', tv.do_app)
            - views.py文件中添加：def do_app(request): return HttpResponse("这是子路由")
            
- 4. URL中的嵌套参数
    - 捕获某个参数的一部分
        - 例如URL：/index/page-3, 需要捕获数字3作为参数
            '''
                url(r'index_1/(page-(\d+)/)?$', tv.myindex_1), #不太好
                
                # ?P 表明后面是参数，<参数名>，\d+ 描述参数
                # 如：index_2/page-3/
                url(r'index_2/(?:page-(?P<page_number>\d+)/)?$', tv.myindex_2), #好
            '''
            - 上述例子会得到两个参数，但 ?: 表明忽略此参数

- 5. 传递额外参数
    - 参数不仅仅来自于URL，还可能是我们自己定义的内容
        '''
        url(r'extrem/$', tv.extremParam, {'name': 'liuying'}),
        '''
    - 附加参数同样适用于include语句，此时对include内所有都添加
    
- 6. URL的反向解析
    - 防止硬编码
    - 本质上是对每一个URL进行命名
    - 以后再编码代码中使用URL的值，原则上都应该使用反向解析
    - 方法：reverse()
        - reverse()的主要作用是将提取的网址按照要求进行替换，计算得到响应所需要的新的网址
        