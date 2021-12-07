import pandas as pd
import datetime

t = datetime.datetime.now()

t1 = t.strftime('%Y-%m-%d %H:%M:%S')
t1 = pd.to_datetime(t1)

t2 = (t-datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S")
t2 = pd.to_datetime(t2)

# data_per_hour = data[(data.time >= t1) & (data.time <= t2)]

# t3 = pd.to_datetime('2020-08-11 11:22:23')

print(t1)