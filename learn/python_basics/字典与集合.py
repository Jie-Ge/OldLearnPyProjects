brand = ['111', '222', '333', '444']
slogan = ['1啊', '2额', '3哦', '4哎']
print(slogan[brand.index('333')]) # 输出slogan中与brand相同索引的值
# ----------字典 { 用大括号表示，里面是键值对（key：value）} ---------------
dict1 = {'111':'1啊', '222':'2e', '333':'3o', '444':'4ai'}
print(dict1['222'])
dict1['555'] = '5ye' # 添加
print(dict1)

# ************ 字典的合并 *************
d1 = {'a': 1, 'b': '2'}
d2 = {'c': '3', 'd': 4}
d3 = {}

d3.update(d1)
d3.update(d2)


# ***********************
dict2 = {}
dict2 = dict2.fromkeys((1, 2, 3), 'numer')
print(dict2)
for eachkey in dict2.keys():#打印所有的键， .values()打印值， .items()打印每一项
    print(eachkey)
print(dict2.get(4, '木有'))
print(dict2.get(3, '木有')) #获得某一项，没有的就输出‘木有','3'为键名
print(2 in dict2) # 返回bool类型
# dict2.clear() 清空字典


a = {1:'one', 2:'two', 3:'three'}
b = a.copy() # 拷贝，存储的地址要变
c = a        # 赋值，存储的地址不变，相当于多了一个名字，改变其中一个，另一个也要改变
print(a, b, c)
print(id(a), id(b), id(c)) # 输出存储的地址


a.pop(2) # 弹出键‘2'
a.popitem() # 随机弹出某一项
print(a)

e = {'yang':'jie'}
a.update(e) # 用e来更新a
print(a)

print('------------------- 集合 dir(set)查看有哪些方法 ------------------')
# 没有映射关系的{}，就是集合
num = {} # 字典类型（dict）
num1 = {1, 2, 3, 3, 4, 4, 0, 112, 12, 33, 22} # 集合类型（set）
print(num1) # 集合会自动清除重复的元素, 但数据会被打乱，是无序的
# 集合里的数据是无序的， 所以不能索引
# 例如： num1[2] "error!!!!"

set1 = set((1, 2, 3, 4, 5, 6, 7)) # 可放入元组，或者是列表、大括号，会自动转化成集合
print(set1)

# 使用集合方便去掉重复元素
num2 = [1, 2, 7, 4, 5, 5, 4, 3, 0, 112, 12, 33, 22] # 创建一个列表
num2 = list(set(num2)) # 使用set去掉重复数据, 但顺序打乱，再转化成列表
print(num2)

frozenset([1,2,3,4]) # 冰冻的集合，即不能改变的集合

