### models类的使用
- 作用：在django中，models负责跟数据库交互（负责业务对象和数据库的关系映射）（相当于views与数据库之间的转接口）
- ORM
    - Object Relational Mapping: 对象关系映射，主要实现模型对象到数据库数据的映射
        - 类名对应------》数据库中的表名
        - 类属性对应---------》数据库里的字段
        - 类实例对应---------》数据库表里的一行数据
    - 使用：
        - 在应用(app)中的models.py文件中定义class
        - 所有需要使用ORM的class都必须是 models.Model 的子类
        - class中的所有属性对应表格中的字段
        - 字段的类型都必须使用 models.xxx ,不能是python中的类型
    - 字段常用参数
        - max_length：数值的最大长度
        - blank：是否允许字段为空，默认不允许
        - null：在db中控制是否保存为null，默认为false
        - default：默认值
        - unique：唯一
        - verbose_name：假名

### 数据库的迁移
1. 在命令行(conda环境下cd到项目文件下)中，生成数据迁移的语句（生成sql语句）
    【将model层转为迁移文件migrations, 即会在app文件下创建数据库迁移文件migrations】
    【会生成数据库空文件】
    - '''
        （默认为全局，即对所有最新更改的model或迁移文件进行操作）
        python manage.py makemigrations
    - '''
2. 在命令行中，输入数据迁移的指令
    【将新版本的迁移文件执行，更新数据库】
    - '''
        （默认为全局）
        python manage.py migrate
    - '''
    - ps: 如果迁移中出现没有变化或者报错，可以尝试强制迁移
    - '''
        强制迁移命令：
        （对指定app进行操作）
        python manage.py makemigrations 应用名
        python manage.py migrate 应用名
    - '''
3. 对于默认数据库，为了避免出现混乱，如果数据库中没有数据，可以将自带的migrations文件、sqllite3数据库删除
4. 修改了表（即修改了models.py中的表的属性，类型等）,就需要数据库的迁移

### 使用shell命令进行数据库的操作
- 在使用shell之前，需进行数据库的迁移
- cd到conda环境下的项目文件下
- python manage.py shell：启动shell

- from 应用.models import 类名：导入models文件中自定义的类
- t_all = 类名.objects.all(): 显示这个类的所有对象实例
- t = 类名(): 创建实例
- t.属性 = "..." : 为属性赋值
- t.save() : 保存实例，即保存到数据库

- 其他操作：
    - 注意：all() 括号里不能添加条件
    - te = 类名.objects.filter(age=18): 过滤，得到age=18的实例
    - te = 类名.objects.exclude(age=18): 排除age=18的实例
    - get(): 如果知道只有一个对象和查询匹配，则可以直接使用 get() 方法返回单个对象
    
    - 格式：属性名__条件=值
    - te = 类名.objects.filter(age__gt=18): 查询年龄大于18岁的对象
        - gt: 大于
        - gte：大于等于
        - lt：小于
        - lte：小于等于
        - range：范围 age__range=[20, 30]
        - year：年份
        - isnull：是否为空
        - contains: 包含，icontains：不区分大小写
        - startswith：以...开头，istartswith
        - endswith: 以...结尾, iendswith
    
    - 其他的参考django中文文档 https://www.django.cn/course/show-18.html

### 数据库表关系
- 主键：关系型数据库中的一条记录中有若干个属性，若其中某一个属性组(注意是组)能唯一标识一条记录，该属性组就可以成为一个主键
- 外键：成绩表中的学号不是成绩表的主键，但它和学生表中的学号相对应，并且学生表中的学号是学生表的主键，则称成绩表中的学号是学生表的外键
- 多表联查：利用多个表联合查找某一项或者多项信息
- 关系
    - OneToOneField
        - 建立关系：在需要建立关系的两个类中，只需在一个类中使用OneToOneField
            - django2.0开始，OneToOneField()需要包含on_delete 参数
            
            - on_delete=None,               # 删除关联表中的数据时,当前表与其关联的field的行为
            - on_delete=models.CASCADE,     # 删除关联数据,与之关联也删除
            - on_delete=models.DO_NOTHING,  # 删除关联数据,什么也不做
            - on_delete=models.PROTECT,     # 删除关联数据,引发错误ProtectedError
            
            - -# models.ForeignKey('关联表', on_delete=models.SET_NULL, blank=True, null=True)
            - on_delete=models.SET_NULL,    # 删除关联数据,与之关联的值设置为null（前提FK字段需要设置为可空,一对一同理）
            
            - -# models.ForeignKey('关联表', on_delete=models.SET_DEFAULT, default='默认值')
            - on_delete=models.SET_DEFAULT, # 删除关联数据,与之关联的值设置为默认值（前提FK字段需要设置默认值,一对一同理）
            - on_delete=models.SET,         # 删除关联数据,
                a. 与之关联的值设置为指定值,设置：models.SET(值)
                b. 与之关联的值设置为可执行对象的返回值,设置：models.SET(可执行对象)
                
        - shell命令添加实例时建立表关系（联表添加）：
            - 在两张表中的其中一张没有声明关系的表中：
                - 直接添加实例就行，不需要说明关系
            - 在有声明关系的表中：
                - 使用create()方法, 或者使用实例化然后save()
                1. 使用实例化：
                    '''
                        设一张表(School_table)的实例s；然后在另一张(President_table)有申明关系的表中创建实例：
                        p = President_table()
                        p.属性 = "..."
                        p.my_school = s  <<<<<<< 就是此句 (my_school也是属性)
                        p.save()    
                    '''
                2. 使用create()方法  (推荐使用)
                    '''
                        如果是一对一或者一对多，一的那一方就只能创建一个对象，再创会报错
                        p = President_table.objects.create(属性1=value，属性2.., my_school=s)
                        另一种写法：
                            dicts = {'属性1':value，'属性2':.., 'my_school':s}
                            President_table.objects.create(**dicts)
                    '''
        - 联表查询 (母表: School_table；子表：President_table，关系：1对1)
            '''由子表查母表：
                    母表有属性school_name, 子表有属性my_school、president_name
                    因为 母表 和 子表 建立了1对1的关系，
                    所以 子表 的实例对象可以查询到 母表 的属性 
                    方法：
                        p = President_table.objects.get(president_name='jiege')
                        p.my_school.school_name   
               由母表查子表 ：
                    格式：子表名__子表的属性=value
                    s = School_table.objects.get(President_table__president_name='jiege')
            '''
        - 修改
            - 单个修改使用save()
            - 批量修改使用update()
        - 删除
            - delete()
             
    - OneToManyField
        - 如：学校(School_table)与学校的老师(Teacher_table)就是1对多的关系
        - 建立关系（声明外键）：
            - 使用ForeignKey
            - 在'多'的那一边使用，比如Teacher_table里进行定义:
                - my_school = models.ForeignKey("School_table")
        - 添加
            - 跟1对1方法类似，create()或者save()
            - 不能添加空对象
        - 查询
            - 知道老师查学校，通过声明的关系属性，直接查
                - t = Teacher_table()
                - t.my_school
            - 知道学校，查这个学校的所有老师
                - 在Teacher_table中声明关系时，系统会自动在School_table(未声明关系的一方)中添加“teacher_table__set”属性【格式：类名开头小写__set】
                - 查：
                    - s = School_table()
                    - s.teacher_table__set.all()
                - 过滤
                    - s.teacher_table__set.all().filter(...)
        
    - ManyToManyField
        - 如：老师（Teacher_table）和学生（Student_table）
        - 建立关系
            - 在任意一方使用ManyToManyField （只需要定义一边）：
                - my_teachers = models.ManyToManyField("Teacher_table")
        - 添加
            - 在添加某个学生的老师时，需要添加多个老师（因为是多对多的关系）
            - t1 = Teacher_table.objects.filter(id=4)
            - s1 = Student_table.objects.filter(id=9).first()
            - s1.author.add(t1)
            - 好像需要 s1.save()
        - 查询
            - 同一对多的方法：系统会自动在未声明关系的一方添加属性‘类名开头小写__set’

### django连接数据库
- 自带默认数据库sqllite3
    - 关系型数据库
    - 轻量型
- 建议开发用sqllite3，实际部署用mysql之类的数据库
- 切换数据库：
    1. 切换数据库在setting.py中设置
        - '''
            ### django连接mysql
            DATABASES = {
                'default' = {
                    'ENGING': 'django.db.backends.mysql',
                    'NAME': '数据库名',
                    'PASSWORD': '数据库密码',
                    'HOST': '127.0.0.1',
                    'PORT': '3306',
                }
            }
        - '''
    2. 需要在项目文件下的__init__文件中导入pymysql包
        - '''
            import pymysql
            pymysql.install_as_MySQLdb()
        - '''