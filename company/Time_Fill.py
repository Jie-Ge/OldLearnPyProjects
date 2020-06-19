import pandas as pd
import numpy as np
with open('./主系统液压.csv') as f:
    df = pd.read_csv(f)

df1 = df[['tagname', 'time']]
dff = df1.groupby("tagname").apply(lambda x: x.sort_values('time'))
groups = dff['tagname'].unique()
dff_gp = dff.groupby('tagname')

index = -1
for group in groups:
    tagname = dff_gp.get_group(group)['tagname'].values[0]
    gp_min = dff_gp.get_group(group)['time'].min()
    gp_max = dff_gp.get_group(group)['time'].max()
    date_start = pd.to_datetime(gp_min)
    date_end = pd.to_datetime(gp_max)
    print('date_start: ', date_start)
    print('date_end: ', date_end)
    i = date_start
    while i < date_end:
        i = i + pd.Timedelta("1s")
        df.loc[index] = [tagname, str(i), np.NAN]
        index -= 1

df = df.sort_values(['tagname', 'time'], ascending=True)
df = df.reset_index(drop=True)
df = df.drop_duplicates(subset=['tagname', 'time'], keep='first')
print(df)
df.to_csv('new_主系统液压.csv', index=False)