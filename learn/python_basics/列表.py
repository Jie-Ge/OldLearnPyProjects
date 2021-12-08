astring = 'asdadasd'
for i in astring:
    print(i, end = " ")
print("\n")
menber = ['remove', 'pop', 'dfd', 'ffdd', 'delete']
for i in menber:
    print(i, len(i))
#------对列表进行操作------
menber.append(['append', 'sd'])
print(menber)

# 合并两个列表
menber.extend(['extend111', 'extend222'])
print(menber)

menber.insert(1, 'insert')
print(menber)

# remove只能删除第一个匹配到的值
menber.remove('remove')
print(menber)

del menber[2]
print(menber)

print(menber.pop())
print(menber.pop(1))
print(menber)

print(menber[1:3]) # 1到2号元素
print(menber[:3]) # 0到2号元素
print(menber[1:]) # 1到结尾
print(menber[:]) # 所有
#----列表比较大小----
print('------------------------------')
list1 = [123, 345]
list2 = [99, 450]
print(list1 > list2)
list1 = list1 * 3
print(list1)
print(123 in list1)
print(250 not in list1)
list3 = [123, ['jiege', 111], 456]
print('jiege' in list3[1])
print(list3[1][1])

'''
map(function, iterable1,...):
    根据提供的函数对指定序列做映射;
    序列中的每一个元素作为参数调用 function 函数，返回包含每次 function 函数返回值的新列表

'''

w = map(lambda x: x ** 2, [1, 2, 3])
print(list(w))

q = map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
print(list(q))