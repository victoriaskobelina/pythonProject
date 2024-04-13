#В исходном текстовом файле(dates.txt) найти все даты в форматах ДД.ММ.ГГГГ и
#ДД/ММ/ГГГГ. Посчитать количество дат в каждом формате. Поместить в новый
#текстовый файл все даты февраля в формате ДД/ММ/ГГГГ.
import re
with open('dates.txt', 'r') as file:
    data = file.read()
# Находим все даты в форматах ДД.ММ.ГГГГ и ДД/ММ/ГГГГ
dates_dd_mm_yyyy = re.findall(r'\b\d{2}[./]\d{2}[./]\d{4}\b', data)
dates_dd_mm_yyyy_slash = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', data)
# Считаем количество дат в каждом формате
count_dd_mm_yyyy = len(dates_dd_mm_yyyy)
count_dd_mm_yyyy_slash = len(dates_dd_mm_yyyy_slash)
# Находим все даты февраля в формате ДД/ММ/ГГГГ
feb_dates_dd_mm_yyyy = re.findall(r'\b(0[1-9]|[12][0-9]|3[01])/(0[2])/(\d{4})\b', data)
# Записываем найденные даты февраля в новый файл
with open('feb_dates.txt', 'w') as file:
    for date in feb_dates_dd_mm_yyyy:
        file.write('/'.join(date) + '\n')
# Выводим результаты
print(f'Количество дат в формате ДД.ММ.ГГГГ: {count_dd_mm_yyyy}')
print(f'Количество дат в формате ДД/ММ/ГГГГ: {count_dd_mm_yyyy_slash}')
