#Дана строка, содержащая по крайней мере один символ пробела.
#Вывести подстроку, расположенную между первым и последним пробелом исходной строки.
#Если строка содержит только один пробел, то вывести пустую строку.
def get_substring_between_spaces(input_string):
    # Находим индексы первого и последнего пробела в строке
    first_space_index = input_string.find(' ')
    last_space_index = input_string.rfind(' ')
    # Если строка содержит только один пробел, возвращаем пустую строку
    if first_space_index == last_space_index:
        return ""
    # Иначе возвращаем подстроку, находящуюся между первым и последним пробелом
    return input_string[first_space_index + 1:last_space_index]
input_string = "Mother drinks meat"
result = get_substring_between_spaces(input_string)
print(result)