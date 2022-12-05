import math


n = int(input())
dots = list()
for i in range(n):
    x, y = map(float, input().split())
    dots.append((x, y, i))
dots.sort()

x1 = dots[0][0]
y1 = dots[0][1]
n1 = dots[0][2] + 1

degrees = list()
for i in range(1, n):
    x2 = dots[i][0]
    y2 = dots[i][1]
    n2 = dots[i][2] + 1

    x_diff = x2 - x1
    y_diff = y2 - y1

    d = math.atan2(y_diff, x_diff)
    degrees.append((d, (n1, n2)))

degrees.sort()
print(degrees[(len(degrees) - 1) // 2][1][0], degrees[(len(degrees) - 1) // 2][1][1])
