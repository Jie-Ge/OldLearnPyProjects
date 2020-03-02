# 视图
### 1.视图概念
- 视图即视图函数，接收web请求并返回web响应，事物处理函数。
- 响应指符合http协议要求的任何内容，包括json，string，html等
- 本章忽略事务处理，重点在如何返回处理结果上
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