import numpy as np
import scipy.io as sio
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(context='notebook', style='white')


# pca 适用于无监督学习的数据降维, 只在有必要的时候（算法运行太慢或者占用太多内存）才考虑采用PCA
# pca算法步骤: http://www.ai-start.com/ml2014/html/week8Z.html#header-n187
# 注意: 本代码是与链接中的算法公式相反的. eg:80行  Sigma = X.T @ X / m.  后面的公式都是相反的,注意看维度

# ============= load data_of_visual ==============

def get_X(df):
    '''

    :param df:
    :return:
        add a column to the feature, it is all one
    '''
    ones = pd.DataFrame({'ones': np.ones(len(df))})
    data = pd.concat([ones, df], axis=1)
    return data.iloc[:, :-1].as_matrix()


def get_y(df):
    return np.array(df.iloc[:, -1])


def normalize_feature(df):
    '''

    :param df:
    :return:
        std: 标准差
    '''
    return df.apply(lambda column: (column - column.mean()) / column.std())


mat = sio.loadmat('./data_of_visual/ex7data1.mat')
X = mat.get('X')

# --- figure1 -----
sns.lmplot('X1', 'X2', data=pd.DataFrame(X, columns=['X1', 'X2']), fit_reg=False)


# plt.show()

# =====================  normalize data_of_visual ====================

def normalize(X):
    '''

    :param X:
    :return: for each column, (X - mean) / std
    '''
    X_copy = X.copy()
    m, n = X_copy.shape
    for col in range(n):
        X_copy[:, col] = (X_copy[:, col] - X_copy[:, col].mean()) / X_copy[:, col].std()
    return X_copy


X_norm = normalize(X)

# --- figure2 -----
sns.lmplot('X1', 'X2', data=pd.DataFrame(X_norm, columns=['X1', 'X2']), fit_reg=False)


# plt.show()

# ================= covariance matrix(协方差矩阵) ==============
# cov = x.T * X / m -1     m:样本数,  x: 特征矩阵,  x.T: 转置

def covariance_marix(X):
    m = X.shape[0]
    return X.T @ X / m  # 不知为何m没有减一


Sigma = covariance_marix(X_norm)
print(Sigma)


# ================== PCA ============================

def pca(X):

    X_norm = normalize(X)
    Sigma = covariance_marix(X_norm)

    # 奇异值分解: https://blog.csdn.net/u012162613/article/details/42214205
    U, S, V = np.linalg.svd(Sigma)
    return U, S, V


U, S, V = pca(X_norm)
print(U)
u1 = U[0]
print(u1)


# ================= project data_of_visual to lower dimension (降维) ==========

def project_data(X, U, k):
    '''

    :param X:
    :param U:
    :param k: 选取k列
    :return:
    '''
    m, n = X.shape
    if k > n:
        raise ValueError('k should be lower of n')
    return X @ U[:, :k]


Z = project_data(X_norm, U, 1)
print(Z)

# --- figure3 -----
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 5))
sns.regplot('X1', 'X2', data=pd.DataFrame(X_norm, columns=['X1', 'X2']), fit_reg=False, ax=ax1)
ax1.set_title('Original dimension')

sns.rugplot(Z, ax=ax2)
ax2.set_xlabel('Z')
ax2.set_title('Z dimension')


# plt.show()

# ================ recover data_of_visual (恢复数据到原来的维度) ===========

# z = x @ u ,  则 x = z @ u.T

def recover_data(Z, U):
    m, n = Z.shape
    return Z @ U[:, :n].T


X_recover = recover_data(Z, U)
print(X_recover)

# --- figure4 -----
fig1, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize=(12, 5))
sns.rugplot(Z, ax=ax1)
ax1.set_title('Z dimension')
ax1.set_xlabel('Z')

# 在二维上展示Z
sns.regplot('X1', 'X2', data=pd.DataFrame(X_recover, columns=['X1', 'X2']),
            fit_reg=False, ax=ax2)
ax2.set_title('2D of Z')

# 原来的维度
sns.regplot('X1', 'X2', data=pd.DataFrame(X_norm, columns=['X1', 'X2']),
            fit_reg=False, ax=ax3)
ax3.set_title('Original dimension')
# plt.show()
