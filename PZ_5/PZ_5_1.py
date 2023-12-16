#Составить функцию решения задачи: из заданного числа вычли сумму его цифр.
#Из результата вновь вычли сумму его цифр и т. д. Через сколько таких дейтсвий получится нуль?
def sum_of_digits(number):
    sum = 0
    while number != 0:
        sum += number % 10  # получаем последнюю цифру числа и прибавляем к сумме
        number //= 10  # удаляем последнюю цифру числа
    return sum

def steps_to_zero(number): #шаги к нулю
    steps = 0
    while number != 0:
        number -= sum_of_digits(number)
        steps += 1
    return steps

try:
    number = int(input("Введите число: "))
    result = steps_to_zero(number)
    print("Количество действий для достижения нуля: ", result)
except ValueError:
    print("Введите, пожалуйста, целое число")
