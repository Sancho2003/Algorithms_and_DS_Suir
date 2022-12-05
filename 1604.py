k = int(input())
n = list(map(int, input().split()))

for i in range(k):
    n[i] = (n[i], i + 1)

n.sort(reverse=True, key = lambda x: x[0])

result = list()
t = n[0][0]
for i in range(t):
    result.append(n[0][1])
count = -1
for i in range(1, k):
    for j in range(n[i][0]):
        count += 2
        if count < t * 2:
            result.insert(count, n[i][1])
        else :
            count = 0
            t = t * 2
            result.insert(count, n[i][1])
print(*result)
