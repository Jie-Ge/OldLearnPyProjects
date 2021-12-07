import time
from django.db import models

# Create your models here.

class ClassRoom(models.Model):
    roomID = models.IntegerField()
    loc = models.CharField(max_length=20)
    roomName = models.CharField(max_length=20)

    def __str__(self):
        return self.roomName


class Teacher(models.Model):

    name = models.CharField(max_length=12)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    course = models.CharField(max_length=20)

    room = models.OneToOneField(ClassRoom, on_delete=models.CASCADE)

    def curTime(self):
        return time.time()
    # curTime一列的列名
    curTime.short_description = "当前时间"
    # curTime按'name'排序
    curTime.admin_order_field = 'name'


    # 加入魔法函数，可以在使用shell命令行时，反馈信息，检查是否成功
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

