import pandas as pd
import numpy as np
with open('./outputfilename.csv') as f:
    df = pd.read_csv(f)

# print(df.duplicated(subset=['tagname', 'time']).value_counts())


# df = pd.DataFrame(df)
df.dropna(subset=['tagname'], inplace=True)

df = df.sort_values(['tagname', 'time'])

df = df.astype(str)

# print(df['tagname'].value_counts())
tagnames=np.unique(df['tagname'])
datetime_imput = []
tagname_imput=[]
# time=pd.to_datetime(df['time'])
time_min=df["time"].min()
time_max=df["time"].max()
tagname=list(df['tagname'])
# print(tagnames)

for i in tagnames:
    # print(i)
    min = pd.to_datetime(time_min)
    time_max = pd.to_datetime(time_max)
    while min <= time_max:
        datetime_imput.append(min)
        tagname_imput.append(i)
        min = min + pd.Timedelta("1s")

tagname_imput = pd.DataFrame(tagname_imput)
datetime_imput = pd.DataFrame(datetime_imput)
data = pd.merge(datetime_imput, tagname_imput, left_index=True, right_index=True)

data.rename(columns={'0_x': 'time', '0_y': 'tagname'}, inplace=True)

data = data.sort_values(['tagname', 'time'])

print('取time列后得到的类型：', type(data['time']))
print('\ntime列中的元素类型：', type(data['time'][0]))
print('\n数据各列的类型：', data.dtypes)
# print('\n数据各列的类型：', data.info())
data['time'] = data['time'].astype('str')
print('\n上句代码并未出现异常')


data['tagtime']=data['tagname']+data['time']

# df[['time']]=df['time'].astype('str')
df['tagtime']=df['tagname']+df['time']
data=data.merge(df, how='left',left_on=['tagtime'],right_on=['tagtime'])

data.rename(columns={'tagtime_x':'tagtime'},inplace=True)
data_merge=data.loc[:,['tagtime','qdyyb','yldx','ylgx','fksj','gzsjgcgz','djbhgz','zxtyy','fjph']]
# print(data)
data_merge['tagname']=data['tagname_x']
data_merge['time']=data['time_x']

# print(data.icol(0).value_counts())
# data_merge.to_csv('new_主系统液压.csv', index=False)

# df1 = df[['tagname', 'time']]
# dff = df1.groupby("tagname").apply(lambda x: x.sort_values('time'))
# groups = dff['tagname'].unique()
# dff_gp = dff.groupby('tagname')
#
# index = -1
# for group in groups:
#     tagname = dff_gp.get_group(group)['tagname'].values[0]
#     gp_min = dff_gp.get_group(group)['time'].min()
#     gp_max = dff_gp.get_group(group)['time'].max()
#     date_start = pd.to_datetime(gp_min)
#     date_end = pd.to_datetime(gp_max)
#     print('date_start: ', date_start)
#     print('date_end: ', date_end)
#     i = date_start
#     while i < date_end:
#         i = i + pd.Timedelta("1s")
#         new_row = pd.DataFrame({'tagname': tagname,
#                                 'time': str(i)},
#                                index=[1])
#         df = df.append(new_row, ignore_index=True)
#         # df.loc[index] = [tagname, str(i), np.NAN]
#         # index -= 1
#
# df = df.sort_values(['tagname', 'time'], ascending=True)
# df = df.reset_index(drop=True)
# df = df.drop_duplicates(subset=['tagname', 'time'], keep='first')
# print(df)
# df.to_csv('new_主系统液压.csv', index=False)