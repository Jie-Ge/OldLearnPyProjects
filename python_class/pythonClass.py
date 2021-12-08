import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime
import random
import csv

'''
fn = 'data_of_visual.csv'
with open(fn, 'w') as fp:
    wr = csv.writer(fp)
    wr.writerow(['日期', '销量', '单价'])
    startDate = datetime.date(2014, 1, 1)
    for i in range(1, 1825):
        count = 300 + random.randrange(100)
        price = 100+random.randint(1,5)
        wr.writerow([str(startDate),count,price])
        startDate = startDate+datetime.timedelta(days=1)
'''
# 1. 创建csv文件
startDate = datetime.date(2014, 1, 1)
datelist = [str(startDate)]
count = [300+random.randrange(100)]
price = [100+random.randint(1,5)]
for i in range(1, 1825):
    startDate = startDate+datetime.timedelta(days=1)
    datelist.append(str(startDate))
    count.append(300+random.randrange(100))
    price.append(100+random.randint(1,5))
dataframe = pd.DataFrame({'日期': datelist, '销量': count, '单价': price})
dataframe = dataframe[['日期', '销量', '单价']]
dataframe.to_csv('data_of_visual.csv', sep=',', index=False)


# 2. pandas读取数据并删除含有缺失值的行
df = pd.read_csv('data_of_visual.csv')
df = df.dropna()


# 3. 使用matplotlib生成折线图，反映每月的销量情况，并把图形保存为本地文件one.jpg
plt.figure(figsize=[12, 8])
yearMonth = pd.DataFrame(i[:7] for i in df['日期'])
df['年月'] = yearMonth
countMonth = df['销量'].groupby(df['年月']).sum()
countMonth = list(countMonth.values)
x_yearMonth = list(set(df['年月']))
x_yearMonth.sort()

plt.xlabel('month')
plt.ylabel('sales')
plt.plot(x_yearMonth, countMonth)
plt.xticks(rotation=80)
plt.savefig('one.png')


# 4. 按年进行统计，使用matplotlib绘制柱状图显示每年的营业额，并把图形保存为本地文件two.jpg；
plt.figure()
year = pd.DataFrame(i[:4] for i in df['日期'])
df['年'] = year
priceTotal = df['单价'].groupby(df['年']).sum()
priceTotal = list(priceTotal.values)
x_year = list(set(df['年']))
x_year.sort()
x_year1 = x_year

plt.xlabel('year')
plt.ylabel('Total-price')
plt.ylim((37400, 37700))
plt.bar(x_year, priceTotal)
plt.savefig('two.png')


# 5. 按年进行统计，使用matplotlib绘制柱状图显示每年销售量最大的月份及销售额，并把图形保存为本地文件three.jpg；
# 第一个y坐标轴
month = pd.DataFrame(i[5:7] for i in df['日期'])
df['月'] = month
df_groupby_year = df[['年', '销量']].groupby(df['年']).max()
df_merge = pd.merge(df_groupby_year,df, on=['年', '销量'], how='left')
# 删除'年'、’销量'重复的行，保留第一次出现的行
df_duplicates = df_merge.drop_duplicates(subset=['年','销量'],keep='first')
y1_monthOfMaxSales = list(df_duplicates['月'])
# 将str列表转为int列表
y1_monthOfMaxSales = list(map(int, y1_monthOfMaxSales))
x_year = list(map(int, x_year))
# print(df_duplicates)
# print(y_monthOfMaxSales)
# print(y1_monthOfMaxSales)
y2_sales_MaxYearmonth = []
for index1, row1 in df_duplicates.iterrows():
    sumPrice = 0
    for index2, row2 in df.iterrows():
        if row1['年月'] == row2['年月']:
            sumPrice += row2['单价']
    y2_sales_MaxYearmonth.append(sumPrice)

fig, ax1 = plt.subplots()
for i in range(len(x_year)):
    x_year[i] -= 0.2

ax1.bar(x_year, y1_monthOfMaxSales, width=0.4, fc='b')  # green, solid line
ax1.set_xlabel('year')
ax1.set_ylabel('The biggest monthly sales each year', color='b')

# 第二个y坐标轴
ax2 = ax1.twinx()  # 生成次坐标轴
for i in range(len(x_year)):
    x_year[i] += 0.4
ax2.bar(x_year, y2_sales_MaxYearmonth, width=0.4, fc='g')  # blue
ax2.set_ylabel('The sales volume of the biggest monthly sales each year', color='g')
ax2.set_ylim(min(y2_sales_MaxYearmonth)-100, max(y2_sales_MaxYearmonth)+100)
plt.savefig('three.png')
# plt.show()


# 6. 按年度统计该商品的营业额数据，使用matplotlib生成饼状图显示每年都的营业额分布情况，并把图形保存为本地文件four.jpg。
plt.figure()
sales_year = df['单价'].groupby(df['年']).sum()
total_sales = sum(sales_year)
sales_year = [i/total_sales*100 for i in list(sales_year)]
plt.pie(sales_year, labels=x_year1, autopct='%1.3f%%', startangle=90)
plt.title('Turnover per year')
plt.savefig('four.png')
plt.show()