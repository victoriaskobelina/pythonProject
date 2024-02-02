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

# Создаем множества для каждого магазина
magistr_books = {'Лермонтов', 'Достоевский', 'Пушкин', 'Тютчев'}
dom_knigi_books = {'Толстой', 'Грибоедов', 'Чехов', 'Пушкин'}
bukmarket_books = {'Пушкин', 'Достоевский', 'Маяковский'}
galeria_books = {'Чехов', 'Тютчев', 'Пушкин'}

# Находим пересечение множеств, чтобы определить, в каких магазинах есть книги Пушкина и Тютчева
book_intersection = magistr_books & dom_knigi_books & bukmarket_books & galeria_books

# Выводим результат
print("Книги Пушкина и Тютчева можно приобрести в следующих магазинах:", book_intersection)

