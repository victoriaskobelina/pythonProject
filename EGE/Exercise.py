#В магазине для упаковки подарков есть N кубических коробок. Самой
#интересной считается упаковка подарка по принципу матрёшки -
#подарок упаковывается в одну из коробок, та в свою очередь в другую
#коробку и т.д. Одну коробку можно поместить в другую, если длина её
#стороны хотя бы на 7 единиц меньше длины стороны другой коробки.
#Определите наибольшее количество коробок, которое можно
#использовать для упаковки одного подарка, и максимально возможную
#длину стороны самой маленькой коробки, где будет находиться подарок.
#Размер подарка позволяет поместить его в самую маленькую коробку.
#Входные данные
#В первой строке входного файла находится число N - количество коробок
#в магазине (натуральное число, не превышающее 10 000). В следующих
#N строках находятся значения длин сторон коробок (все числа
#натуральные, не превышающие 10 000), каждое - в отдельной строке.
#Запишите в ответе два целых числа: сначала наибольшее количество
#коробок, которое можно использовать для упаковки одного подарка,
#затем максимально возможную длину стороны самой маленькой коробки
#в таком наборе.

#открываем файл
f = open('proba.txt')
#считываем и заносим в переменную первую строку из файла
n = f.readline()
#значения из файла переводятся в целые числа, сортируются в порядке убывания и сохраняются в переменную boxes
boxes = sorted([int(i) for i in f], reverse=True)
#в список answer записывается первый элемент списка boxes
answer = [boxes[0]]
#цикл, в котором перебираются все элементы списка boxes, кроме первого (т.к.записали)
for box in boxes[1:]:
    #если разница между последним элементом списка answer и текущим элементом больше либо равна 7, то текущий элемент добавляется в answer
    if answer[-1] - box >= 3:
        answer.append(box)
print("Наибольшее количество коробок, которое можно использовать для упаковки 1-ого подарка:", len(answer))
print("Максимальная длина стороны самой маленькой коробки в таком наборе:", answer[-1])
