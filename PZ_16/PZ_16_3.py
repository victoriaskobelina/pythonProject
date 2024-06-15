#Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
#сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
#Использовать модуль pickle для сериализации и десериализации объектов Python в
#бинарном формате
import pickle
class Counter:
    def __init__(self, value=0):
        self.value = value
    def increment(self):
        self.value += 1
    def decrement(self):
        self.value -= 1
def save_def(filename, *counters):
    with open(filename, 'wb') as file:
        pickle.dump(counters, file)
def load_def(filename):
    with open(filename, 'rb') as file:
        counters = pickle.load(file)
    return counters

counter1 = Counter(5)
counter2 = Counter(10)
counter3 = Counter(15)

counter1.increment()
counter2.increment()
counter3.increment()

save_def('counters.pickle', counter1, counter2, counter3)
loaded_counters = load_def('counters.pickle')

for c in loaded_counters:
    print("Значение после инкремента: ", c.value)
