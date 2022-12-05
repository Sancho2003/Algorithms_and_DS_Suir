m, n, k = map(int, input().split())
result = 0
points = list()
single_points = list()

for i in range(k):
    p_first, p_second = map(int, input().split())
    p_first -= 1
    p_second -= 1
    points.append((p_first, p_second))

for i in range(m):
    p_first = (i, -1)
    p_second = (i, n)
    points.append(p_second)
    points.append(p_first)

for i in range(n):
    p_first = (-1, i)
    p_second = (m, i)
    points.append(p_second)
    points.append(p_first)

points.sort(key=lambda k: (k[0], k[1]))

for i in range(len(points) - 1):
    if points[i][0] == points[i + 1][0]:
        if points[i + 1][1] - points[i][1] - 1 > 1:
            result += 1
        elif points[i + 1][1] - points[i][1] - 1 == 1:
            p_first = points[i][0]
            p_second = points[i][1] + 1
            single_points.append((p_first, p_second))

points.sort(key=lambda k: (k[1], k[0]))

for i in range(len(points) - 1):
    if points[i][1] == points[i + 1][1]:
        if points[i + 1][0] - points[i][0] - 1 > 1:
            result += 1
        elif points[i + 1][0] - points[i][0] - 1 == 1:
            p_first = points[i][0] + 1
            p_second = points[i][1]
            single_points.append((p_first, p_second))

single_points.sort(key=lambda k: (k[0], k[1]))

if len(single_points) > 1:
    for i in range(len(single_points) - 1):
        if single_points[i] == single_points[i + 1]:
            result += 1
            i += 1

print(result)
