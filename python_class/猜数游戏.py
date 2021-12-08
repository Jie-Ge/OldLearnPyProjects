import random
# random.choice([1,2,3,4]) 随机的选择一个
for i in range(10):
    num = random.randint(0, 9)
    # print(num)

# 当输入数据是浮点数,会保留为浮点数类型
a = eval(input("只能输入已经定义的变量和数字(会保留数据类型):"))
print(type(a))


s = input('输入的所有数据都是字符串类型:')
print(type(s))
print(s.isdigit())

'''
针对string
-str.isdigit() 判断是否是数字
-str.isalpha() 判断是否是字母
-str.isalnum() 判断是否是数字和字母的组合
'''