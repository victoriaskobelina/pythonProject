#В матрице элементы последней строки заменить на 0.
import random
rows = 3 #столбцы
cols = 3 #строки
matrix = [[random.randint(1, 10) for j in range(cols)] for i in range(rows)]
print("Изначальная матрица: ")
for row in matrix:
    print(row)
matrix[-1] = [0 for _ in range(cols)]
print("Изменённая матрица: ")
for row in matrix:
    print(row)
