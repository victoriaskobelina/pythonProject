#Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
#последовательности из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Элементы первого и второго файлов:
#Среднее арифметическое элементов первого и второго файлов:
#Количество нечетных элементов первого и второго файлов:
#Элементы общие для двух файлов:
#Количество элементов, общих для двух файлов:
import random
# Генерация случайной последовательности целых чисел
def generate(length):
    return [random.randint(-100, 100) for _ in range(length)]
# Запись последовательности в файл
def write_sequence(sequence, filename):
    with open(filename, 'w') as file:
        for number in sequence:
            file.write(str(number) + '\n')
# Чтение последовательности из файла
def read_sequence(filename):
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file]
# Создание двух файлов с последовательностями
sequence1 = generate(10)
write_sequence(sequence1, 'sequence1.txt')
sequence2 = generate(10)
write_sequence(sequence2, 'sequence2.txt')
# Чтение последовательностей из файлов
sequence1 = read_sequence('sequence1.txt')
sequence2 = read_sequence('sequence2.txt')
# Обработка элементов
average = (sum(sequence1) + sum(sequence2)) / (len(sequence1) + len(sequence2))
odd_count = sum(1 for num in sequence1 + sequence2 if num % 2 != 0)
common_elements = set(sequence1).intersection(sequence2)
# Запись результатов в новый файл
with open('result.txt', 'w') as result_file:
    result_file.write("Элементы первого и второго файлов:\n")
    result_file.write(f"{sequence1}\n{sequence2}\n\n")
    result_file.write("Среднее арифметическое элементов первого и второго файлов:\n")
    result_file.write(f"{average}\n\n")
    result_file.write("Количество нечетных элементов первого и второго файлов:\n")
    result_file.write(f"{odd_count}\n\n")
    result_file.write("Элементы общие для двух файлов:\n")
    result_file.write(f"{common_elements}\n\n")
    result_file.write("Количество общих элементов для двух файлов:\n")
    result_file.write(f"{len(common_elements)}\n")