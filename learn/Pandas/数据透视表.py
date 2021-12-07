import pandas as pd
import numpy as np
df1 = pd.DataFrame([[1, 4.6800159814195536e+92, 1.6, 1000.123],
                    [1, 2, 3.5, 30.123],
                    [3, 4, 3, 3]],
                   columns=['tagname', 'time', 'fs', 'gl'])

# 按照index分组，对values取平均值
BIN_mean = pd.pivot_table(df1, index='tagname', values='gl', aggfunc=np.mean).reset_index()
BIN_mean.columns = ['tagname', 'gl_mean']
