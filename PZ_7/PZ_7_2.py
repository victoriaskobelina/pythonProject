#Дана строка, содержащая по крайней мере один символ пробела.
#Вывести подстроку, расположенную между первым и последним пробелом исходной строки.
#Если строка содержит только один пробел, то вывести пустую строку.
def string_between_spaces(input_string):
    #индексы первого и последнего пробела в строке
    first_index = input_string.find(' ')
    last_index = input_string.rfind(' ')
    #если строка содержит только один пробел, возвращаем пустую строку
    if first_index == last_index:
        return ""
    #возвращаем подстроку, находящуюся между первым и последним пробелом
    return input_string[first_index + 1:last_index]
input_string = "Mother drinks meat"
result = string_between_spaces(input_string)
print(result)