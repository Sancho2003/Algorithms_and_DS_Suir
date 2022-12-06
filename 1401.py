n = int(input())
x, y = [int(i) for i in input().split()]
x -= 1
y -= 1

matrix_size = 2 ** n 
line = [0] * (matrix_size)
matrix = [line[:] for i in range(matrix_size)]


def computing(size, x_zero, y_zero, x_start, y_start):
    global current
    global matrix
    if size == 2:
        current += 1
        if x_zero == x_start and y_zero == y_start:
            matrix[x_start + 1][y_start] = current
            matrix[x_start + 1][y_start + 1] = current
            matrix[x_start][y_start + 1] = current

        if x_zero == x_start + 1 and y_zero == y_start:
            matrix[x_start][y_start] = current
            matrix[x_start + 1][y_start + 1] = current
            matrix[x_start][y_start + 1] = current
        
        if x_zero == x_start and y_zero == y_start + 1:
            matrix[x_start][y_start] = current
            matrix[x_start + 1][y_start + 1] = current
            matrix[x_start + 1][y_start] = current

        if x_zero == x_start + 1 and y_zero == y_start + 1:
            matrix[x_start][y_start] = current
            matrix[x_start + 1][y_start] = current
            matrix[x_start][y_start + 1] = current

        return
        # Заполняем матрицу во всех остальных случаях
    else:
        length = int(size / 2)

        if x_zero < x_start + length and y_zero < y_start + length:
            current += 1
            matrix[x_start + length][y_start + length - 1] = current
            matrix[x_start + length - 1][y_start + length] = current
            matrix[x_start + length][y_start + length] = current
            computing(length, x_zero, y_zero, x_start, y_start)
            computing(length, x_start + length, y_start + length - 1, x_start + length, y_start)
            computing(length, x_start + length - 1, y_start + length, x_start, y_start + length)
            computing(length, x_start + length, y_start + length, x_start + length, y_start + length)

        elif x_zero < x_start + length and y_zero >= y_start + length:
            current += 1
            matrix[x_start + length][y_start + length - 1] = current
            matrix[x_start + length - 1][y_start + length - 1] = current
            matrix[x_start + length][y_start + length] = current
            computing(length, x_zero, y_zero, x_start, y_start + length)
            computing(length, x_start + length, y_start + length - 1, x_start + length, y_start)
            computing(length, x_start + length - 1, y_start + length - 1, x_start, y_start)
            computing(length, x_start + length, y_start + length, x_start + length, y_start + length)

        elif x_zero >= x_start + length and y_zero < y_start + length:
            current += 1
            matrix[x_start + length - 1][y_start + length - 1] = current
            matrix[x_start + length - 1][y_start + length] = current
            matrix[x_start + length][y_start + length] = current
            computing(length, x_zero, y_zero, x_start + length, y_start)
            computing(length, x_start + length - 1, y_start + length - 1, x_start, y_start)
            computing(length, x_start + length - 1, y_start + length, x_start, y_start + length)
            computing(length, x_start + length, y_start + length, x_start + length, y_start + length)

        elif x_zero >= x_start + length and y_zero >= y_start + length:
            current += 1
            matrix[x_start + length][y_start + length - 1] = current
            matrix[x_start + length - 1][y_start + length - 1] = current
            matrix[x_start + length - 1][y_start + length] = current
            computing(length, x_zero, y_zero, x_start + length, y_start + length)
            computing(length, x_start + length, y_start + length - 1, x_start + length, y_start)
            computing(length, x_start + length - 1, y_start + length - 1, x_start, y_start)
            computing(length, x_start + length - 1, y_start + length, x_start, y_start + length)

current = 0
computing(matrix_size, x, y, 0, 0)
for i in  range(matrix_size):
    for j in range(matrix_size):
        print(matrix[i][j], end = " ")
    print()
