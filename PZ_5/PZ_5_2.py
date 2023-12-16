#Описать функцию AddLeftDigit(D,K), добавляющую к целому положительному числу K
#слева цифру D (D-входной параметр целого типа, лежащий в диапозоне 1-9, K-параметр целого типа,
#являющийся одновременно входным и выходным). С помощью этой функции последовательно добавить к
#данному числу K слева данные цифры D1 b D2, выводя результат каждого добавления
def AddLeftDigit(D, K): #Добавить левую цифру
    return int(str(D) + str(K))

try:
    D1 = int(input("Введите первую цифру: "))
    K = int(input("Введите исходное число: "))
    result = AddLeftDigit(D1, K)
    print("Результат добавления первой цифры:", result)
except ValueError:
    print("Введите, пожалуйста, целое число.")

try:
    D2 = int(input("Введите вторую цифру: "))
    result = AddLeftDigit(D2, result)
    print("Результат добавления второй цифры:", result)
except ValueError:
    print("Введите, пожалуйста, целое число")