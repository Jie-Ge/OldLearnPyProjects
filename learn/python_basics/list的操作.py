a = [['one', 1], ['two', '2'], ['three', 3]]
# 直接使用两个参数获取数据
for i, j in a:
    print(i, '---', j)


a = [1, 2, 3, ]
b = [10, 20, 30, 40]
# a中的每一个数依次和b中的每一个数想加
c = [i + j for i in a for j in b]
print(c)


# 将列表a转化为字符串，并用分号连接
keys_list = ['申请人', '发明(设计)人', '主分类号', '分类号']

result = ';'.join(keys_list)

print(result)  # 申请人;发明(设计)人;主分类号;分类号

# 同时遍历两个列表
name_list = ['张三', '李四', '王五']
age_list = [54, 18, 34]
for name, age in zip(name_list, age_list):
    print(name, ':', age)

