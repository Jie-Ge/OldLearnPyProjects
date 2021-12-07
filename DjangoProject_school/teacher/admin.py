from django.contrib import admin

# 此文件用于管理admin界面

# Register your models here.

# 导入类(表)
from teacher.models import ClassRoom, Teacher, Student

admin.site.site_header = "这是站头"
admin.site.site_title = "这是站标题"
admin.site.index_title = "这是首页标语"


# 设置admin管理类，用来管理相应的类
class ClassRoomAdmin(admin.ModelAdmin):
    list_per_page = 2  # 每一页显示2个


# 使用装饰器，就不再需要进行站点注册了
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    # curTime是models.py中Teacher类中的函数名
    list_display = ['name', 'age', 'curTime']  # 控制Teacher界面显示的信息
    search_fields = ['name', 'age']

    # 将teacher的个人信息进行分组显示
    fieldsets = (
        ('基本信息', {'fields': ['name']}),
        ('其他信息', {'fields': ['age', 'address', 'course']})
    )


class StudentAdmin(admin.ModelAdmin):
    pass


# 站点注册, 并注明其admin管理类
admin.site.register(ClassRoom, ClassRoomAdmin)
# admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
