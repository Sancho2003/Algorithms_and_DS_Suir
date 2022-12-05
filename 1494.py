n = int(input())
s = list()
f = True
k = 0
for i in range(n):
    ball = int(input())
    if ball > k:
        s += list(range(k + 1, ball))
        k = ball
    else:
        current = s.pop(-1)
        if ball != current:
            f = False

if f:
    print("Not a proof") 
else:
    print("Cheater")
