#Организовать и вывести последовательность из 20 целых чисел, выбрать не
#повторяющиеся элементы, найти их количество. Элементы больше 5 увеличить в два раза.
import random
numbers = random.choices(range(1, 20), k=20)
print("Список до обработки:", numbers)
#множество для уникальных элементов
unique = set(numbers)
#находим количество уникальных элементов
unique_numbers = len(unique)
#увеличиваем элементы больше 5 на два раза
for i in range(len(numbers)):
    if numbers[i] > 5:
        numbers[i] *= 2
print("Список после обработки:", numbers)
print("Количество уникальных элементов:", unique_numbers)