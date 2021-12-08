from random import sample

num = [str(i) for i in range(10)]
a = 'A'
for i in range(26):
    num.append(a)
    a = chr(ord(a)+1)
b = 'a'
for i in range(26):
    num.append(b)
    b = chr(ord(b)+1)
print(num)
# s = ''
# q = sample(num, 10)
# for i in q:
#     s += str(i)
# print(s)
print(''.join(sample(num,10)))