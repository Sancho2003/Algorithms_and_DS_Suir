import math


n = int(input())
a = list()
b = list()
for i in range(n):
    x, y = map(int, input().split())
    a.append((x, y))
    b.append((y, x))

a.sort()
b.sort()
result = 0
for i in range(n - 1):
    result += (a[i + 1][0] - a[i][0]) * (i + 1) * (n - i - 1) * 2
    result += (b[i + 1][0] - b[i][0]) * (i + 1) * (n - i - 1) * 2

result /= n * (n - 1)
print(math.trunc(result))
