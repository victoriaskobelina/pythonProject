#Из предложенного текстового файла (text18-28.txt) вывести на экран его содержимое,
#количество символов в тексте. Сформировать новый файл, в который поместить текст в
#стихотворной форме предварительно вставив после строки N (N – задается пользователем)
#произвольную фразу
#Чтение содержимого текстового файла и подсчет количества символов
import chardet
#определение кодировки файла
with open('text18-28.txt', 'rb') as file:
    rawdata = file.read()
    result = chardet.detect(rawdata)
    encoding = result['encoding']
#чтение содержимого файла с учетом определенной кодировки
with open('text18-28.txt', 'r', encoding=encoding) as file:
    content = file.read()
    count = len(content)
    print("Содержимое файла:")
    print(content)
    print("Количество символов в тексте:", count)
#запрос пользователя для вставки фразы после строки N
N = int(input("Введите номер строки, после которой нужно вставить фразу: "))
phrase = input("Введите произвольную фразу для вставки: ")
#формирование нового файла с текстом в стихотворной форме и вставкой фразы после строки N
lines = content.split('\n')
new_content = '\n'.join(lines[:N] + [phrase] + lines[N:])
#запись нового содержимого в файл
with open('new_text.txt', 'w', encoding=encoding) as new_file:
    new_file.write(new_content)
print("Текст успешно сохранен в новом файле new_text.txt.")
