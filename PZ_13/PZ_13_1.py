#В матрице элементы последней строки заменить на 0.
import random
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in range(len(matrix[-1])):
    matrix[-1][i] = 0
for row in matrix:
    print(row)
