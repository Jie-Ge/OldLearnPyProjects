# 元组是关系数据库中的基本概念，关系是一张表，
# 表中的每行(即数据库中的每条记录)就是一个元组，每列就是一个属性。
# 在二维表里，元组也称为行。

#元组的标志是() 和逗号
tuple1 = (1, 2, 3, 4)
print(tuple1)
print(type(tuple1))
print(tuple1[:2])
temp = (1)
print(type(temp))
temp2 = (1,)
print(type(temp2))
temp3 = 2, 3, 4
print(type(temp3))
print(8 * (8))
print(8 * (8,))
#只能这种间接的对元组进行修改
temp4 = temp3[:1] + (11,) + temp3[1:]
print(temp4)
