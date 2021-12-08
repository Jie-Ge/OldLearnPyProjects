import matplotlib.pyplot as plt
import seaborn as sns
sns.set(context="notebook", style="white")

import numpy as np
import pandas as pd
import scipy.io as sio

mat = sio.loadmat('./data_of_visual/ex7data1.mat')
X = mat.get("X")

# x = X.shape[0]
# ones = pd.DataFrame({'ones': np.ones(len(X))})
# data_of_visual = pd.concat([ones, x], axis=1)
print(X)
print(X.shape[1])