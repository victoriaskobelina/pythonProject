def rectangle ():
    a = float(input("Ширина %s: " % figure))
    b = float(input("Высота %s: " % figure))
    print("Площадь: %.2f" % (a*b))
def triangle():
    a = float(input("Основание %s: " % figure))
    b = float(input("высота %s: " % figure))
figure = input("1-прямоугольник, 2-треугольник: ")
if figure == '1':
    rectangle()
elif figure == '2':
    triangle()

