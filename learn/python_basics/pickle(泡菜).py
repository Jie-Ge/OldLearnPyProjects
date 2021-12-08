import pickle

list1 = ['11122', '阿斯达', '撒大大', '1321']
# 写
# 后缀名随意取，‘wb’以字节型数据写入
pickle_file = open('pickle_file.pkl', 'wb')
pickle.dump(list1, pickle_file)
pickle_file.close()

# 读
pickle_file = open('pickle_file.pkl', 'rb')
data = pickle.load(pickle_file)
print(data)


# 这样的话就可以将一个长数据（如字典）写入一个文件，用的时候再读
