#Создайте класс «Счетчик», который имеет атрибут текущего значения и методы для
#инкремента и декремента значения
class Counter:
    def __init__(self, initial_value=0):
        self.value = initial_value
    def increment(self):
        self.value += 1
    def decrement(self):
        self.value -= 1
counter = Counter(5)
print("Текущее значение:", counter.value)
counter.increment()
print("После инкремента:", counter.value)
counter.decrement()
print("После декремента:", counter.value)
