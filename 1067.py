n = int(input())
s = list()
for i in range(n):
    s.append(list(input().split("\\")))
s.sort()

s_set = set()
s_list = list()

for i in s:
    for j in range(len(i)):
        word=" " * j + i[j]
        root = str(i[:j])
        if root + word not in s_set:
            s_set |= {root + word}
            s_list.append(word)

for i in s_list:
    print(i)
