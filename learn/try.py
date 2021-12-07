
num = eval(input("请输入截止的整数："))
a=0
b=1
list1 = []
while b < int(num):
    list1.append(b)
    a, b = b, a+b
print(list1)
