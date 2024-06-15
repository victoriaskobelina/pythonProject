#Задание предполагает, что у студента есть проект с практическими работами (№ 2-13),
#оформленный согласно требованиям. Все задания выполняются c использованием модуля
#OS:
#з1 перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге. Имена
#вложенных подкаталогов выводить не нужно.
#з2 перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку
#test1. В папку test переместить два файла из ПЗ6, а в папку test1 - один файл из ПЗ7.
#Файл из ПЗ7 переименовать в test.txt. Вывести в консоль информацию о размере
#файлов в папке test.
#з3 перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в
#консоль. Использовать функцию basename () (os.path.basename()).
#з4 перейти в любую папку, где есть отчет в формате .pdf и «запустите» файл в
#привязанной к нему программе. Использовать функцию os.startfile().
#з5 удалить файл test.txt
import os
#з1
os.chdir("/home/student/Документы/SkobelinaIS-25/PZ_11")
files = os.listdir()
print("Список файлов в каталоге PZ11:")
for file in files:
    if os.path.isfile(file):
        print(file)

#з2
os.chdir("/home/student/Документы/SkobelinaIS-25/")
os.mkdir("test")
os.chdir("test")
os.mkdir("test1")
# Переместить файлы из PZ6 и PZ7
os.rename("/home/student/Документы/SkobelinaIS-25/PZ_6/", "file1.txt")
os.rename("/home/student/Документы/SkobelinaIS-25/PZ_7/", "test.txt")
# Вывести информацию о размере файлов в папке test
file_sizes = {}
for file in os.listdir():
    if os.path.isfile(file):
        file_sizes[file] = os.path.getsize(file)
print("Размер файлов в папке test:")
for file, size in file_sizes.items():
    print(f"{file}: {size} байт")

#з3
# Найти файл с самым коротким именем в каталоге PZ11
os.chdir("/home/student/Документы/SkobelinaIS-25/PZ_11")
files = os.listdir()
shortest_file = min(files, key=lambda x: len(os.path.basename(x)))
print(f"Файл с самым коротким именем в каталоге PZ11: {os.path.basename(shortest_file)}")

#з4
file_path = "/home/student/Документы/SkobelinaIS-25/reports/PZ_17.pdf"
command = "xdg-open '{}'".format(file_path)
os.system(command)

#з5
os.rmdir("/home/student/Документы/SkobelinaIS-25/test/test.txt")