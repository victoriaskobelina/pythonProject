# Чтение входных данных из файла
with open("313_26.txt", "r") as file:
    N = int(file.readline())
    boxes = [int(file.readline()) for _ in range(N)]
# Сортировка коробок по возрастанию длины стороны
boxes.sort()
# Инициализация переменных
max_boxes = 0 #
max_inner_box_side = 0
# Перебор коробок и проверка условий
for i in range(N):
    inner_boxes = 1
    inner_box_side = boxes[i]
    for j in range(i + 1, N):
        if boxes[j] - inner_box_side >= 7:
            inner_boxes += 1
            inner_box_side = boxes[j]
    if inner_boxes > max_boxes:
        max_boxes = inner_boxes
        max_inner_box_side = boxes[i]
print(f"{max_boxes} {max_inner_box_side}")