#Дан список A размера N. Найти максимальный элемент
#из его элементов с нечетными номерами: A1, A3, A5, ... .
def max_elements(A):
    max_element = float('-inf')  #максимальный элемент как отрицательную бесконечность
    for i in range(len(A)):
        try:
            if i % 2 != 0 and A[i] > max_element:  # Проверяем нечетный индекс и обновляем максимальный элемент
                max_element = A[i]
        except IndexError:
            print("Индекс выходит за границы списка.")
            return None
    return max_element
A = [1, 5, 2, 3, 8, 4, 7, 6, 4]
result = max_elements(A)
if result is not None:
    print("Максимальный элемент с нечетными индексами:", result)