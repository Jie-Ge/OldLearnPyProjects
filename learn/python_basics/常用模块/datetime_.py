import datetime

# from datetime import datetime
'''
- datetime.date()

- datetime.datetime()
    方法：
        today
        now
        utcnow
        fromtimestamp
        
- datetime.time()

- datetime.timedelta(): 表示一个时间长度，可用于加上一个具体时间

'''
dt1 = datetime.date(2019, 3, 12)
print(dt1)
print(dt1.year, dt1.month)

dt2 = datetime.datetime(2019, 2, 23)
print(dt2)

dt3 = datetime.datetime.today()
print(dt3)

t = datetime.timedelta(hours=2)

print(dt3 + t)
