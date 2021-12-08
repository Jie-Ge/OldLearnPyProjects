import calendar

'''
calendar: 获取一年的日历字符串
参数：
    w = 每个日之间的间隔字符串
    l = 每个周所占用的行数
    c = 每个月之间的间隔字符串
方法：
    isleap(year): 判断某一年是否是闰年
    leapdays(year1, year2): 获取指定年份之间的闰年个数
    month(year, month): 获取某个月的日历字符串
    weekday(year, month, day): 获取周几
    ...
'''

cal = calendar.calendar(2018)
print(cal)
