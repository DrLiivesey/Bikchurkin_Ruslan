size = int(input("Введите размерность матрицы: "))

# Генерация матрицы
matrix = [[i+1 for i in range(size)] for j in range(size)]

# Вывод исходной матрицы
print("Исходная матрица:")
for row in matrix:
    print(row)

# Транспонирование матрицы на месте
for i in range(size):
    for j in range(i):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Вывод транспонированной матрицы
print("Транспонированная матрица:")
for row in matrix:
    print(row)

