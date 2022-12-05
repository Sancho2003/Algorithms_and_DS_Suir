n = int(input())
x, y = map(int, input().split())
x -= 1
y -= 1
line = ["*"] * (2**n)
matrix_1 = list()
for i in range(2**n):
matrix_1.append(line[:])
matrix_1[x][y] = 0

def computing(size, x_zero, y_zero, x_start, y_start):
global num
global matrix_1
if size == 2:
num += 1
if x_zero == x_start and y_zero == y_start:
matrix_1[x_start + 1][y_start] = num
matrix_1[x_start + 1][y_start + 1] = num
matrix_1[x_start][y_start + 1] = num

if x_zero == x_start + 1 and y_zero == y_start:
matrix_1[x_start][y_start] = num
matrix_1[x_start + 1][y_start + 1] = num
matrix_1[x_start][y_start + 1] = num

if x_zero == x_start and y_zero == y_start + 1:
matrix_1[x_start][y_start] = num
matrix_1[x_start + 1][y_start + 1] = num
matrix_1[x_start + 1][y_start] = num

if x_zero == x_start + 1 and y_zero == y_start + 1:
matrix_1[x_start][y_start] = num
matrix_1[x_start + 1][y_start] = num
matrix_1[x_start][y_start + 1] = num

return
else:
length = size // 2

if x_zero < x_start + length and y_zero < y_start + length:
num += 1
matrix_1[x_start + length][y_start + length - 1] = num
matrix_1[x_start + length - 1][y_start + length] = num
matrix_1[x_start + length][y_start + length] = num
computing(length, x_zero, y_zero, x_start, y_start)
computing(length, x_start + length, y_start + length - 1, x_start + length, y_start)
computing(length, x_start + length - 1, y_start + length, x_start, y_start + length)
computing(length, x_start + length, y_start + length, x_start + length, y_start + length)

elif x_zero < x_start + length and y_zero >= y_start + length:
num += 1
matrix_1[x_start + length][y_start + length - 1] = num
matrix_1[x_start + length - 1][y_start + length - 1] = num
matrix_1[x_start + length][y_start + length] = num
computing(length, x_zero, y_zero, x_start, y_start + length)
computing(length, x_start + length, y_start + length - 1, x_start + length, y_start)
computing(length, x_start + length - 1, y_start + length - 1, x_start, y_start)
computing(length, x_start + length, y_start + length, x_start + length, y_start + length)

elif x_zero >= x_start + length and y_zero < y_start + length:
num += 1
matrix_1[x_start + length - 1][y_start + length - 1] = num
matrix_1[x_start + length - 1][y_start + length] = num
matrix_1[x_start + length][y_start + length] = num
computing(length, x_zero, y_zero, x_start + length, y_start)
computing(length, x_start + length - 1, y_start + length - 1, x_start, y_start)
computing(length, x_start + length - 1, y_start + length, x_start, y_start + length)
computing(length, x_start + length, y_start + length, x_start + length, y_start + length)

elif x_zero >= x_start + length and y_zero >= y_start + length:
num += 1
matrix_1[x_start + length][y_start + length - 1] = num
matrix_1[x_start + length - 1][y_start + length - 1] = num
matrix_1[x_start + length - 1][y_start + length] = num
computing(length, x_zero, y_zero, x_start + length, y_start + length)
computing(length, x_start + length, y_start + length - 1, x_start + length, y_start)
computing(length, x_start + length - 1, y_start + length - 1, x_start, y_start)
computing(length, x_start + length - 1, y_start + length, x_start, y_start + length)

num = 0
computing(len(matrix_1), x, y, 0, 0)
for i in range(2 ** n):
for j in range(2 ** n):
print(matrix_1[i][j], end = " ")
print()
