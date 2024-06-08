#Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
#сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
#Использовать модуль pickle для сериализации и десериализации объектов Python в
#бинарном формате
import pickle
class student:
    def __init__(self, name, sec_n, marks):
        self.name = name
        self.sec_n = sec_n
        self.marks = marks

    @staticmethod
    def ave_marks(marks):
        average = sum(marks) / len(marks)
        return average

    @staticmethod
    def respect(average):
        st_is_otl = average == 5
        return st_is_otl


def save_def(stude, file):
    with open(file, 'wb') as f:
        pickle.dump(stude, f)


def load_def(file):
    with open(file, 'rb') as f:
        studen = pickle.load(f)
    return studen

Bondarev = student('Сергей', 'Бондарев', [2, 1, 2, 3, 4, 5, 4])
Korennoi = student('Никита', 'Коренной', [2, 1, 5, 3, 4, 5, 5])
Borzistiy = student('Максим', 'Борзистый', [5, 5, 5, 5])

students_info = [Bondarev,Borzistiy,Korennoi]

for stud in students_info:
    save_def(stud, 'students.pkl')
    students = load_def('students.pkl')
    print(students.ave_marks(students.marks))
    print('Student is otlichnik -', students.respect(students.ave_marks(students.marks)))