import pandas as pd
import datetime
with open('C:/Users/jiege/Desktop/比对数据2号风机/AI0018.csv') as f:
    df = pd.read_csv(f)

new_data = [0 if x >= 120 and x <= 160 else 1 for x in df['值']]

# new_data = pd.DataFrame(new_data, columns=['value'])
df['value'] = new_data
# print(df)

df['时间戳'] = df['时间戳'].str[1:-1]
start = df['时间戳'].min()
end = df['时间戳'].max()
# print(df)
print(start)
print(end)
# full_time = pd.date_range(start=start, end=end, freq='S')
full_time = [x.strftime('%Y-%m-%d %H:%M:%S') for x in list(pd.date_range(start=start, end=end, freq='S'))]
# print(full_time[0])
# print(full_time[-1])
full_time = pd.DataFrame(full_time, columns=['时间戳'])
# print(full_time)

df = df.merge(full_time, how='outer')
df = df.sort_values(['时间戳'], ascending=True)

df = df.fillna(method='ffill', axis=0)
df = df[df['时间戳'] < '2020-05-26 00:00:00']
print(df)
print(df['value'].value_counts())