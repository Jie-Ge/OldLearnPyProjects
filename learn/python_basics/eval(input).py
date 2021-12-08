x = 1
y = 2
# eval(字符串表达式)
# input():返回数据为字符串
str1 = eval(input('请输入表达式：'))
print(str1)

# eval() : 可以保留输入数据的类型
# 键盘必须输入已经定义了的变量, 否则只能输入数字
qwe = []
q = eval(input('input:'))
print(type(q))


num1 = input('输入多个数字(用空格隔开):')
num2 = num1.split(' ')  # 输入时用的啥隔开就用啥分割
print(num2)