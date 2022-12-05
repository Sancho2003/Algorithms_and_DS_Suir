string_num = int(input()) - 1
s = input()
n = len(s)
start = list()
cur = string_num
for i in range(n):
    start.append((s[i], i))

start.sort()
result = list()
for i in range(n):
    result.append(start[i][1])

result_printing = list()
for i in range(n):
    result_printing.append(start[cur][0])
    cur = result[cur]

target_word = "".join(result_printing)
print(target_word)
