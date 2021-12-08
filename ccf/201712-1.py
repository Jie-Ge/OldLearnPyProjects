import math
n = int(input())
num = list(map(int, input().split()))

diff = max(num)
for i in range(n):
    for j in range(i+1, n):
        sub = math.fabs(num[j]-num[i])
        if sub < diff:
            diff = sub

print(int(diff))