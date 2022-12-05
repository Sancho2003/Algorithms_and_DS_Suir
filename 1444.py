import math


n = int(input())
pumpkins = list()
for i in range(n):
    x, y = map(float, input().split())
    pumpkins.append((x, y, i + 1))

x1 = pumpkins[0][0]
y1 = pumpkins[0][1]
n1 = pumpkins[0][2]

measures = list()
for i in range(1, n):
    x2 = pumpkins[i][0]
    y2 = pumpkins[i][1]
    n2 = pumpkins[i][2]

    x_diff = x2 - x1
    y_diff = y2 - y1
    angle = math.degrees(math.atan2(y_diff, x_diff))
    length = x_diff ** 2 + y_diff ** 2
    measures.append((angle, length, n2))

result = (sorted(measures, key=lambda t: (t[0], t[1])))
if n > 2:
    max_angle = result[0][0] - result[n - 2][0] + 360
    max = max_angle
    max_i = 1
    for i in range(1, n - 1):
        if max_angle <= result[i][0] - result[i - 1][0]:
            max_angle = result[i][0] - result[i - 1][0]
            max_i = i
else:
    max = 720
    max_angle = 0
    max_i = 0

if max_angle == 180 and max == 180:
    if max_i - 1 > n - max_i:
        print(max_i)
        print(1)
        for i in range(max_i):
            print(result[i][2])
    else:
        print(n - max_i + 1)
        print(1)
        for i in range(n - 1):
            print(result[i][2])
else:
    print(n)
    print(1)
    if max_angle > 180 and max_i != 1:
        for i in range(max_i, n - 1):
            print(result[i][2])
        for i in range(max_i):
            print(result[i][2])
    else:
        for i in range(n - 1):
            print(result[i][2])
