#В исходном текстовом файле(dates.txt) найти все даты в форматах ДД.ММ.ГГГГ и
#ДД/ММ/ГГГГ. Посчитать количество дат в каждом формате. Поместить в новый
#текстовый файл все даты февраля в формате ДД/ММ/ГГГГ.
import re
with open('dates.txt', 'r') as file:
    data = file.read()
#Даты в форматах ДД.ММ.ГГГГ и ДД/ММ/ГГГГ
dates_dot = re.findall(r'\b\d{2}[./]\d{2}[./]\d{4}\b', data)
dates_slash = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', data)
count_dates_dot = len(dates_dot)
count_dates_slash = len(dates_slash)
#Даты февраля в формате ДД/ММ/ГГГГ
f_dates_slash = re.findall(r'\b(0[1-9]|[12][0-9]|3[01])/(0[2])/(\d{4})\b', data)
#Найденные даты в новый файл
with open('dates_slash.txt', 'w') as file:
    for date in f_dates_slash:
        file.write('/'.join(date) + '\n')
print(f'Количество дат в формате ДД.ММ.ГГГГ: {count_dates_dot}')
print(f'Количество дат в формате ДД/ММ/ГГГГ: {count_dates_slash}')
