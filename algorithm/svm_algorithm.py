import numpy as np
import  matplotlib.pyplot as plt
from sklearn import svm

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler  # 标准化
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

# 指定生成“特定”的随机数-与seed 8 相关, 当再次使用np.random.seed(8)时，生成的随机数时一样的
np.random.seed(8)

# 线性可分

array = np.random.randn(20, 2)  # 20行2列
X = np.r_[array-[3,3], array+[3,3]]  # 每一元素减3， 再按列连接两个矩阵
y = [0]*20 + [1]*20  # 由20个0和20个1组成列表
print(X[0])
print(X[20])
print(y)

# 建立svm模型
# 软间隔svm（线性可分，允许一定量的样本分类错误， 硬间隔svm：完全分类准确, 非线性svm: 线性不可分）
clf = svm.SVC(kernel='linear')
clf.fit(X,y)

x1_min, x1_max = X[:,0].min(), X[:,0].max()
x2_min, x2_max = X[:,1].min(), X[:,1].max()
# meshgrid: 返回坐标矩阵,接受两个一维数组生成两个二维矩阵，如： z,s = np.meshgrid(x,y): 将 x 变成矩阵 z 的行向量，y 变成矩阵 s 的列向量，重复至 z和s的维数一样
# linspace: 等差数列
xx1, xx2 = np.meshgrid(np.linspace(x1_min, x1_max), np.linspace(x2_min, x2_max))
# 得到向量w  : w_0x_1+w_1x_2+b=0
w = clf.coef_[0]
# intercept_ : 截距
# 加1后才可绘制 -1 的等高线， 数组[-1,0,1] + 1 = [0,1,2]
f = w[0]*xx1 + w[1]*xx2 +clf.intercept_[0] + 1
# 绘制等高线，为等高线上注明等高线的含义
plt.contour(xx1, xx2, f, [0,1,2])
# 绘制散点图，plt.scatter(数据, 数据, 颜色序列, colormap)， Paired表示两个相近色彩输出，比如浅蓝、深蓝
# plt.scatter(X[:,0], X[:,1], c=y, cmap=plt.cm.Paired)
plt.scatter(X[:,0], X[:,1], c=y)
plt.scatter(clf.support_vectors_[:,0],clf.support_vectors_[:,1],color='k')
# plt.show()
print('-------------------------------')

# 非线性可分
iris = datasets.load_iris()
X = iris.data
y = iris.target
print(iris.target_names)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3.)

scalar = StandardScaler()  # 标准化, 对每个属性/每列来说所有数据都聚集在0附近
# 先拟合数据，再标准化
X_train_std = scalar.fit_transform(X_train)
# 数据标准化
X_test_std = scalar.transform(X_test)

# 交叉验证，调整参数

# gamma = 1/(2*delta^2)
param_grid = {'C':[1e1,1e2,1e3, 5e3,1e4,5e4],
              'gamma':[0.0001,0.0008,0.0005,0.008,0.005,]}
# 网格搜索，找到最优超参数
clf = GridSearchCV(svm.SVC(kernel='rbf',class_weight='balanced'),param_grid,cv=10)
clf = clf.fit(X_train_std,y_train)
print (clf.best_estimator_)  # 参数最优估计值

clf.score(X_test_std,y_test)
y_pred = clf.predict(X_test_std)


# （真实因变量值，预测因变量值， ）
print(classification_report(y_test,y_pred,target_names=iris.target_names))
# 混淆矩阵：评估分类的准确度
# 对于混淆矩阵C，C(i,j) 表示真实分类是第i类，但是预测值为第j类的观测总数
# 矩阵的对角线表示正确分类的个数，非对角线的点是分类错误的情况
print(confusion_matrix(y_test,y_pred,labels=range(iris.target_names.shape[0])))

# recall表示召回率 = (True positive) / ((True positive)+ (False negative))，表示样本中的正例有多少被预测正确。

# precision表示精确率 = (True positive) / ((True positive)+ (False negative))，表示预测为正的样本中有多少是真正的正样本。

# f1-score（F1指标）表示召回率和精确率两个指标的调和平均数，召回率和精确率越接近,F1指标越高。F1 = 2 / （1/recall + 1/precision）。召回率和精确率差距过大的学习模型，往往没有足够的实用价值。

# avg/total : 加权平均值