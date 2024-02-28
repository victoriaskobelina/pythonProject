#В матрице элементы столбца N (N задать с клавиатуры) увеличить в два раза.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
try:
    #запрос номера столбца у пользователя
    column_num = int(input("Введите номер столбца для увеличения: "))
    #увеличение элементов столбца в два раза
    for i in range(len(matrix)):
        matrix[i][column_num - 1] *= 2
    #вывод измененной матрицы
    for row in matrix:
        print(row)
except ValueError:
    print("Ошибка: Некорректный формат ввода. Пожалуйста, введите целое число.")
except IndexError:
    print(f"Ошибка: Номер столбца должен быть в диапазоне от 1 до {len(matrix[0])}.")