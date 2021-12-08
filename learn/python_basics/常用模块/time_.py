'''
- 时间戳：是从1970年1月1日0时0分0秒到现在的秒数
- UTC时间： 世界标准时间
- 夏令时
- 时间元组

方法：
    timezone: 当前地区的时间和UTC时间相差的秒数
    time(): 得到时间戳
    localtime():得到当前时间的时间结构
    ctime(): 获取字符串类型的当前时间
    clock(): 获取cpu时间
    sleep(s): 使程序进入睡眠，n秒后继续
    strftime(format, t): 格式化时间
'''

import time

t = time.localtime()
print(t)

ft = time.strftime('%Y年%m月%d日 %H:%M', t)
print(ft)

print(time.clock())


tt = time.time()
time.sleep(3)
print(time.time()-tt)

