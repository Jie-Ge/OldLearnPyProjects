import numpy as np
#
# data_of_visual = {1:'a', 2:'b', 3:'c'}
# q = tuple(data_of_visual)
# w = np.array(q)
# print(type(w))
# print(w)

import pickle

def load_file(filename):
    with open(filename, 'rb') as fo:
        data = pickle.load(fo, encoding='latin1')
    return data

data1 = load_file('cifar-10-data_of_visual/data_batch_1')
data2 = load_file('cifar-10-data_of_visual/data_batch_2')
data3 = load_file('cifar-10-data_of_visual/data_batch_3')
data4 = load_file('cifar-10-data_of_visual/data_batch_4')
data5 = load_file('cifar-10-data_of_visual/data_batch_5')
x_train = np.vstack((data1['data_of_visual'],data2['data_of_visual']))
x_train = np.vstack((x_train,data3['data_of_visual']))
x_train = np.vstack((x_train,data4['data_of_visual']))
x_train = np.vstack((x_train,data5['data_of_visual']))

y_train = data1['labels']
y_train.extend(data2['labels'])
y_train.extend(data3['labels'])
y_train.extend(data4['labels'])
y_train.extend(data5['labels'])
y_train = np.array(y_train).reshape((-1, 1))


testdata = load_file('cifar-10-data_of_visual/test_batch')
x_test = testdata['data_of_visual']
y_test = np.array(testdata['labels']).reshape(-1, 1)

print(x_train.shape)
print(x_test.shape)