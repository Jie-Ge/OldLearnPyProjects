import pandas as pd
import numpy as np

# pandas会自动给数据加一个索引值
s = pd.Series([1, 3, 4, np.nan, 7])
print(s)
a = np.random.randn(3)
print(a)

'''
inner: 内连接，仅返回匹配的行
outer：外连接，返回两个表的全部行
left：左连接，返回左表的全部行
right：右连接，返回右表的全部行
'''
pd.merge(how='inner')