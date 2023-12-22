#Начальный вклад в банке равен 1000 руб. Через каждый месяц размер вклада увеличивается на P процентов от
#от имеющейся суммы (P - вещественное число, 0<P<25). По данному P определить, через сколько месяцев размер вклада
#превысит 1100руб., и вывести найденное количество месяцев K (целое число) и итоговый размер
#вклада S (вещественное число).
def calculate(P):
    deposit = 1000
    months = 0
    while deposit < 1100:
        deposit += deposit * (P / 100)
        months += 1
    return months, deposit

try:
    P = float(input("Введите процент P (0 < P < 25): "))
    if 0 < P < 25:
        months, final_deposit = calculate(P)
        print("Через", months, "месяцев размер вклада превысит 1100 руб")
        print("Итоговый размер вклада будет составлять", final_deposit, "руб")
    else:
        print("Введите, пожалуйста, число в диапазоне от 0 до 25")
except ValueError:
    print("Введите, пожалуйста, число")