## session
- 作用：
    - 为了应对HTTP协议的无状态性
    - 用来保存用户比较敏感的信息
- 属于request的一个属性
- 常用操作：    
    - request.session.get(key, defaultValue)
        - 获取session中的key，如果没有，则返回defaultValue
        - 【案例】views.py的mySession()
    - request.session.clear()
        - 清除session值
    - request.session[key] = value
        - 赋值
    - request.session.flush()
        - 删除当前会话，清除会话的cookie
        
## 分页
- 例如：百度上搜索‘python’，会出现很多页
- 假设每一页有20条搜索结果，意味着每次反馈20个结果，点击下一页时再反馈20个结果
- django提供现成的分页器来对结果分页
- 需要导入 from django.core.paginator import Paginator
- 【案例】views.py中的teacher_()

## 基于类的视图
- 参考：https://yiyibooks.cn/
- 可以针对http协议不同的方法创建不同的函数
- 可以使用MiXin等oop技术
- MiXin：
    - 把来自父类的行为或者属性组合在一起
    - 解决多重继承问题
- 【案例】
    - views.py中创建TeacherListView类（继承ListView父类）
    - urls.py中编写 url(r'^teacher/', tv.TeacherListView.as_view())
    
## admin
- 创建admin
    - 配置urls.py: 配置路径
    - 配置setting.py:
        - INSTALLED_APPS中加入新建的app
        - 汉化：修改setting.py中 LANGUAGE_CODE = 'zh-Hans'
        - 时区：TIME_ZONE = 'Asia/Shanghai'  
    - 创建超级用户
        - 进入conda环境下，进入项目文件下，命令：python manage.py createsuperuser
        - 输入Username: admin
        - 输入Email address: admin@example.com
        - Password: **********
        - Password (again): *********
    - 运行项目的服务器
    - 访问 http://127.0.0.1:8000/admin/

- admin界面管理数据表
- 数据表在APP中，那么如何在admin中显示app呢？
    - 在admin.py中：
        - -# 导入类(表)
        - from teacher.models import ClassRoom, Teacher, Student
        - -# 站点注册
        - admin.site.register(ClassRoom)
    - 类中增加以下内容，在admin界面才可以看到新添加的成员的名字
        - def __str__(self):
        -   return self.roomName
        
- 设置admin管理类（用于修改admin界面）
- 实现方式：
    - 1. ModelAdmin
        - 例如：在admin.py中设置：
            class ClassRoomAdmin(admin.ModelAdmin):
                pass（这里面自定义admin界面）
        - 用来管理ClassRoom类
        - 在站点注册时, 需注明其admin管理类：
            - admin.site.register(ClassRoom, ClassRoomAdmin)
    - 2. 装饰器（更直观）
        - 例如：在admin.py中设置：
            @admin.register(Teacher)
            class TeacherAdmin(admin.ModelAdmin):
                pass（这里面自定义admin界面）
        - 就不需要再站点注册
- 管理类里面可设置的变量（admin.py）
    - list_per_page = 2: 页面显示数量
    - actions_on_top/actions_on_button = True/False：控制动作栏显示的位置
    - search_fields = ['name','age'] : 添加一个搜索框（只能搜索name或者age）
    - list_display = [] : 控制要显示的信息（比如个人信息中哪些显示）（默认不显示）(控制成员列表界面)
    - fields = [] : 控制要显示的信息 (默认全部显示) (控制某个成员具体信息的界面)
    - fieldsets = ():
        - 是一个二元元组，将个人信息进行分组显示，每一组可以设置组名、组成员
        - 【案例】admin.py中TeacherAdmin类下的fieldsets
- 在类的外边可以进行如下设置
    - admin.site.site_header = "这是站头"
    - admin.site.site_title = "这是站标题" （html的title）
    - admin.site.index_title = "这是首页标语"
           

- 将方法作为admin界面的列显示
    - 在models.py中对应的类中进行设置
    - 设置方法：
        - 函数必须有返回值
        - 设置short_description作为列名
        - 排序使用admin_order_field
        - 【案例】
            - models.py中Teacher类中的 def curTime()
            - list_display = [] 中需加入类名，才会显示
        