n = int(input())
countries = list()
for i in range(105):
    countries.append([0] * 105)
result = list()
borders = list()


def computing(v, color):
    if result[v] != -1 and result[v] == color:
        return True
    elif result[v] != -1 and result[v] != color:
        return False
    result[v] = color
    for i in range(n):
        if countries[v][i] and not computing(i, 1 - color):
            return False
    return True


for i in range(n):
    borders.append(list(map(int, input().split()))[:-1])
for i in range(n):
    for j in range(len(borders[i])):
        countries[i][borders[i][j] - 1] = countries[borders[i][j] - 1][i] = 1
result = [-1] * 105
f = computing(0, 0)
if f:
    for i in range(n):
        print(result[i], end='') 
else:
    print(-1)
