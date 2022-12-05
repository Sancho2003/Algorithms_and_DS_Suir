n = int(input())

if n == 0:
    print(0)
elif n == 1:
    sum = int(input())
    print(max(sum, 0))
else:
    sum = 0
    result = 0
    for i in range(n):
        p = int(input())
        sum += p
        if sum > result:
            result = sum
        if sum < 0:
            sum = 0
    print(result)
