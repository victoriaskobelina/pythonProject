#Известно, что x кг шоколадных конфет стоит a рублей, а y кг ирисок стоит b рублей.
#Определить сколько стоит 1 кг шоколадных конфет, 1 кг ирисок, а также во сколько раз шоколадные конфеты дороже ирисок
x = float(input("Введите количество шоколадных конфет (в кг):"))
a = float(input("Введите стоимость шоколадных конфет (в руб):"))
y = float(input("Введите количество ирисок (в кг):"))
b = float(input("Введите стоимость ирисок(в руб):"))
price1 = (a/x)
price2 = (b/y)
difference = (price1/price2)
print("Стоимость 1 кг шоколадных конфет:", price1)
print("Стоимость 1 кг ирисок:", price2)
print("В", difference, "шоколадные конфеты дороже ирисок")