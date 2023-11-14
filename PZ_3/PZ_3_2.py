# Дано целое число в диапазоне 1-7.
# Вывести строку - название дня недели, соответствующее данному числу (1 - понедельник, 2 - вторник)

try:
    day_number = int(input("Введите число от 1 до 7: "))

    if 1 <= day_number <= 7:
        if day_number == 1:
            print("Понедельник")
        elif day_number == 2:
            print("Вторник")
        elif day_number == 3:
            print("Среда")
        elif day_number == 4:
            print("Четверг")
        elif day_number == 5:
            print("Пятница")
        elif day_number == 6:
            print("Суббота")
        elif day_number == 7:
            print("Воскресенье")
    else:
        print("Пожалуйста, введите число от 1 до 7")
except ValueError:
    print("Пожалуйста, введите целое число от 1 до 7")