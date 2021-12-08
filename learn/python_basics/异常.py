'''
try:
    ...
except 异常类型1：
    ...
except 异常类型2：
    ...
except (异常类型1,异常类型2,...)
    针对多个异常使用相同的处理
except:
    所有异常的解决方案
[else:
    如果没有异常，则执行此处代码
finally:
    都要执行的代码
]
'''
try:
    num = int(input('input number: '))
    rst = 100/num
    print('计算结果是：', rst)
except ZeroDivisionError as e:
    print('number is 错误的')
    print(e)
# 所有异常都是继承自Exception类
# 任何异常都会被拦截住
except Exception as e:
    print('所有异常都会被拦截住')
    print(e)

print('========= raise手动已发异常 =============')

try:
    print('trytrytry...')
    raise ValueError
except NameError as e:
    print('NameError')
except ValueError as e:
    print('ValueError')

print('============ 自定义异常 ============')

# 自定义的异常必须是系统异常的子类
class DefError(ValueError):
    pass


try:
    print('try.....')
    raise DefError
except DefError as e:
    print('DefError')