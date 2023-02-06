edges = []
no_status = True

in_str = input().split()
n, m, s, v =  int(in_str[0]), int(in_str[1]), int(in_str[2]), float(in_str[3])
currency = [0 for i in range(101)]
currency[s] = v

for i in range(m):
    in_str = input().split()
    a, b = [int(i) for i in in_str[:2]]
    rab, cab, rba, cba = [float(i) for i in in_str[2:]]

    edges.append([a, b, rab, cab])
    edges.append([b, a, rba, cba])

for i in range(n-1):
    for j in range(len(edges)):
        currency[edges[j][1]] = max((currency[edges[j][0]] - edges[j][3]) * edges[j][2], currency[edges[j][1]]);

for i in range(len(edges)):
    if (currency[edges[i][0]] - edges[i][3]) * edges[i][2] > currency[edges[i][1]]:
        print('YES')
        no_status = False
        break

if no_status:
    print('NO')        
