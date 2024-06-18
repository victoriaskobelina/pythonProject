#Создать класс person с одним атрибутом класс (count), с конструктором __init__ и
#одним статическим методом.
#Увеличение количества созданных экземпляров обеспечить в конструкторе __init__
#Статический метод total_people должен обеспечивать построение и вывод фразы
#о количестве созданных экземпляров
class Person:
    count = 0
    def __init__(self):
        Person.count += 1
    @staticmethod
    def total_people():
        print(f"Общее количество: {Person.count}")
person1 = Person()
person2 = Person()
person3 = Person()

Person.total_people()