import pandas as pd
import numpy as np

# data1 = pd.DataFrame([[1, 2, 3],
#              [2, 3, 4],
#              [3, 4, 5]],
#              columns=['c2','time', 'c3'])
# data2 = pd.DataFrame([[3, 2, 5],
#                      [4, 5, 6],
#                      [5, 6, 7]],
#                      columns=['c2','time', 'c3'])
#
# qq = pd.concat([data1, data2], axis=0)
# print(qq)
# data = data1.merge(data2, how='left', left_on='time1', right_on='time')
# print(data)
# # data.fillna(method='ffill',inplace=True)
# # data.fillna(method='bfill',inplace=True)
#
#
# # 左连接：左边全部保留，
# data = data1.merge(data2, how='left')
# print(data)
# data = data2[(data2.time >= 5) & (data2.time <= 6)]
# print(data)
#
# a = 1
# print(1<=a<=2)

# data3 = [11, 130, 150, 200, 111, 140]
#
# new = [1 if x < 120 or x > 160 else 0 for x in data3]
#
# print(new)

import datetime
with open('C:/Users/jiege/Desktop/宁夏项目/outputfilename1.csv') as f:
    df1 = pd.read_csv(f)

# print(df)
import pylab
import numpy as np
import pandas as pd
import sys, os
from scipy.optimize import curve_fit

print('000>>>>>>>>>>>>>>>>>>>')


def list1():
    a = []
    i = 3
    while (i < 11):
        a.append(i)
        i += 0.5
    return a


def func(x, a, b, c, d):
    return a * x ** b + c * x + d


def gl(num):
    dic = {3: 7.28, 3.5: 29.21, 4: 57.21, 4.5: 91.42, 5: 131.5, 5.5: 180.72, 6: 242.4, 6.5: 316.06, 7: 401.63,
           7.5: 499.83, 8: 616.01, 8.5: 741.6, 9: 877.94, 9.5: 1020.09, 10: 1165.59, 10.5: 1304.53, 11: 1500}
    if num >= 10.9:
        return 1500

    else:
        a = num % 1
        b = num // 1
        if (a > 0.5):
            b = b + 1
        elif a < 0.5 and a != 0:
            b += 0.5
        elif a == 0.5:
            b = b
        return dic.get(b)


# ********weibull概率密度函数****

def weibull_pro(fs, v_ave):
    # fs: 10min平均风速
    # v_ave: 轮毂中心高度的月平均风速值
    pr = np.pi * fs / 2 / v_ave ** 2 * np.exp((-np.pi / 4 / v_ave ** 2) * (fs ** 2))
    return round(pr, 4)


# *********weibull分布函数*******
def weibull_dis(fs, v_ave):
    pr = 1 - np.exp(-np.pi / 4 * (fs ** 2 / v_ave ** 2))
    return round(pr, 4)


# *********************** 标准功率曲线拟合 ********************

x = list1()  # 标准风速（完整）
y = []  # 标准功率
for i in x:
    y.append(gl(i))

x_sjfs = df1['bzfs']

popt, pcov = curve_fit(func, x, y, maxfev=500000)

y_pred = [func(i, popt[0], popt[1], popt[2], popt[3]) for i in x_sjfs]

df1['nhgl_bz'] = y_pred
df1.loc[:, 'nhgl_bz'] = df1[['nhgl_bz', 'bzgl']].apply(lambda x: x.bzgl if x.nhgl_bz < 0 else x.nhgl_bz, axis=1)
df1.loc[:, 'nhgl_bz'] = df1[['nhgl_bz', 'bzfs']].apply(lambda x: 1500 if x.nhgl_bz > 1500 else x.nhgl_bz, axis=1)

# ************************ 实际功率曲线拟合 *********************
print('111>>>>>>>>>>>>>')

tag = list(set(df1['ystagname'].dropna().get_values()))
tag = [i for i in tag if i != '']

df2 = pd.DataFrame()
for i in tag:
    print('222>>>>>>>>>>>')
    data = df1[df1['ystagname'] == i]  # 筛选每一台风机
    data_two_col = data[['bzfs', 'BIN_gl_mean']].drop_duplicates()
    data_two_col = data_two_col.dropna()  # bzfs是补全的，而BIN_gl_mean没有，会有空值

    try:
        data_two_col = data_two_col.sort_values(['bzfs']).reset_index(drop=True)
        # idx = data['BIN_gl_mean'].idxmax()  # 最大功率所在行的索引
        # max_gl = data.loc[:, "BIN_gl_mean"].max()  # 最大功率
        # fs_of_maxGL = data.loc[[idx]]['BIN_fs_mean']  # 最大功率对应的风速

        # 计算相邻功率的差值（风速在5以上对应的功率）
        data_loc = data_two_col[data_two_col['bzfs'] > 5]
        data_loc['BIN_gl_mean_1'] = data_loc["BIN_gl_mean"].shift(1)
        data_loc['differ'] = data_loc["BIN_gl_mean"] - data_loc['BIN_gl_mean_1']
        print(data_loc)
        # 计算相邻两点的斜率第一次出现小于50所对应数据的索引
        idx = data_loc[data_loc['differ'] / 0.5 < 50].index.tolist()[0]

        max_gl_value = data_loc.loc[idx - 1]['BIN_gl_mean']
        fs_of_maxGL = data_loc.loc[idx - 1]['bzfs']
        print(max_gl_value, fs_of_maxGL)
        # 对在达到最小斜率之前的数据做拟合，（在达到最小斜率后设置功率保持不变）
        x2 = data_two_col.loc[:idx - 1]['bzfs'].dropna().tolist()
        y2 = data_two_col.loc[:idx - 1]['BIN_gl_mean'].dropna().tolist()

        popt2, pcov2 = curve_fit(func, x2, y2, maxfev=500000)

        y_pred2 = [func(i, popt2[0], popt2[1], popt2[2], popt2[3]) for i in data_two_col['bzfs']]

        data_two_col['nhgl_sj'] = y_pred2

        data = pd.merge(data, data_two_col, how='left', on=['bzfs', 'BIN_gl_mean'])

        # 在达到最大功率后设置功率保持不变
        data.loc[:, 'nhgl_sj'] = data[['nhgl_sj', 'bzfs']].apply(
            lambda x: max_gl_value if x.bzfs > np.double(fs_of_maxGL) else x.nhgl_sj, axis=1)
        data.loc[:, 'nhgl_sj'] = data[['nhgl_sj']].apply(lambda x: 0 if x.nhgl_sj < 0 else x.nhgl_sj, axis=1)

        # ******** 计算weibull概率密度 **********
        # 输入10min平均风速，月平均风速
        data['wb_pro'] = data['fs_mean'].apply(lambda x: weibull_pro(x, data['ysfs'].mean()))

        # ******** 计算weibull分布函数 **********
        # 输入10min平均风速，月平均风速
        data['wb_dis'] = data['fs_mean'].apply(lambda x: weibull_dis(x, data['ysfs'].mean()))

        df2 = pd.concat([df2, data], axis=0)

    except Exception as e:
        print(e)
        continue

print(df2)