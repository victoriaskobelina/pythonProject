#Задание предполагает, что у студента есть проект с практическими работами (№ 2-13),
#оформленный согласно требованиям. Все задания выполняются c использованием модуля
#OS:
# перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге. Имена
#вложенных подкаталогов выводить не нужно.
# перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку
#test1. В папку test переместить два файла из ПЗ6, а в папку test1 - один файл из ПЗ7.
#Файл из ПЗ7 переименовать в test.txt. Вывести в консоль информацию о размере
#файлов в папке test.
# перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в
#консоль. Использовать функцию basename () (os.path.basename()).
# перейти в любую папку где есть отчет в формате .pdf и «запустите» файл в
#привязанной к нему программе. Использовать функцию os.startfile().
# удалить файл test.txt
import os
# Перейти в каталог PZ11 и вывести список файлов
os.chdir("PZ11")
files = os.listdir()
print("Список файлов в каталоге PZ11:")
for file in files:
    if os.path.isfile(file):
        print(file)

# Перейти в корень проекта и создать папку test и test1
os.chdir("..")
os.mkdir("test")
os.chdir("test")
os.mkdir("test1")

# Переместить файлы из PZ6 и PZ7
os.rename("../PZ6/file1.txt", "file1.txt")
os.rename("../PZ6/file2.txt", "file2.txt")
os.rename("../PZ7/file3.txt", "test.txt")

# Вывести информацию о размере файлов в папке test
file_sizes = {}
for file in os.listdir():
    if os.path.isfile(file):
        file_sizes[file] = os.path.getsize(file)
print("Размер файлов в папке test:")
for file, size in file_sizes.items():
    print(f"{file}: {size} байт")

# Найти файл с самым коротким именем в каталоге
shortest_file = min(files, key=lambda x: len(os.path.basename(x)))
print(f"Файл с самым коротким именем: {os.path.basename(shortest_file)}")

os.startfile("test.txt")
os.remove("test.txt")
