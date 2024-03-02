import random
def pr_sequence():
    sequence = [random.randint(1, 10) for _ in range(20)]
    print("Исходная последовательность:")
    print(sequence)
    unique_elements = list(set(sequence))
    print("Неповторяющиеся элементы:")
    print(unique_elements)
    n_of_un_elements = len(unique_elements)
    print("Количество неповторяющихся элементов:", n_of_un_elements)
    up_sequence = [x * 2 if x > 5 else x for x in unique_elements]
    print("Последовательность с элементами больше 5, увеличенными в два раза:")
    print(up_sequence)
pr_sequence()