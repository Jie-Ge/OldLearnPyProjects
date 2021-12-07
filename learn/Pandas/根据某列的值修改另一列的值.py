

data1 = pd.DataFrame([[1, 200011, 33333],
                     [1, 300011, 43333],
                     [2, 40, 5]],
                     columns=['c2', 'time', 'c3'])
# with open('C:/Users/jiege/Desktop/宁夏项目/outputfilename1.csv') as f:
#     df = pd.read_csv(f)
# print(df[df['metric'] == 'AI0047'])
# data1.loc[:, 'bzfs'] = data1[['bzfs', 'BIN_fs']].apply(lambda x: round(x/100, 2) if x.BIN_fs==11.5 else x, axis=1)
# df.loc[:, 'value'] = df[['metric', 'value']].apply(lambda x: round(x.value/1000,4) if x.metric=='AI0047' else x, axis=1)
# print(df[df['metric'] == 'AI0047'])

data1.loc[:, 'time'] = data1[['time', 'c2']].apply(lambda x: round(x.time/100, 1) if x.c2==1 else x.time, axis=1)
print(data1)