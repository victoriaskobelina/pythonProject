# Создание матрицы
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

try:
    # Запрос номера столбца у пользователя
    column_num = int(input("Введите номер столбца для увеличения: "))

    # Увеличение элементов столбца в два раза
    for i in range(len(matrix)):
        matrix[i][column_num - 1] *= 2

    # Вывод измененной матрицы
    for row in matrix:
        print(row)

except ValueError:
    print("Ошибка: Некорректный формат ввода. Пожалуйста, введите целое число.")
except IndexError:
    print(f"Ошибка: Номер столбца должен быть в диапазоне от 1 до {len(matrix[0])}.")
