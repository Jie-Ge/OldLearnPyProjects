import numpy as np
from keras.layers import Dense
from keras.models import Sequential
import matplotlib.pyplot as plt

np.random.seed(1337)

X = np.linspace(-1, 1, 200)
np.random.shuffle(X)  # 打乱数据
Y = 0.5 * X + 2 + np.random.normal(0, 0.1, (200,))

plt.scatter(X, Y)
plt.show()

x_train, y_train = X[:160], Y[:160]
x_test, y_test = X[160:], Y[160:]

module = Sequential()  # 序贯模型，是多个网络层的线性堆叠
# Dense(输出的个数，输入数据的维度(特征个数))
module.add(Dense(units=1,input_dim=1))

module.compile(optimizer='sgd', loss='mse')

# train
print('train---------------')
for step in range(301):
    cost = module.train_on_batch(x_train, y_train)
    if step%100 == 0:
        print('train cost:', cost)

print('test-------')
cost = module.evaluate(x_test, y_test, batch_size=40)
print('test cost:', cost)
W, b = module.layers[0].get_weights()
print('Weights=', W, '\nbiases=', b)

y_pre = module.predict(x_test)
plt.scatter(x_test, y_test)
plt.plot(x_test, y_pre)
plt.show()
