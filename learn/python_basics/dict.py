a = {'one': 1, 'two': 2, 'three': 3}
for k in a:
    print(k)

for k in a.keys():
    print(k)

for v in a.values():
    print(v)

for k, v in a.items():
    print(k, '---', v)

# 字典生成式：方便过滤字典
q = {k: v for k, v in a.items() if v % 2 == 0}
print(q)