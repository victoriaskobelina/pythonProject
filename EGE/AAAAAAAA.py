# Чтение данных из файла
with open('313_26.txt', 'r') as file:
    data = file.readlines()

# Количество коробок
N = int(data[0])
boxes = [int(x) for x in data[1:]]

# Сортировка коробок по убыванию
boxes.sort(reverse=True)

max_boxes = 1
min_box_side = boxes[-1]

# Поиск максимального количества коробок
for i in range(N):
    cnt = 1
    size = boxes[i]
    for j in range(i+1, N):
        if size - boxes[j] >= 7:
            cnt += 1
            size = boxes[j]
    if cnt > max_boxes:
        max_boxes = cnt
        min_box_side = boxes[i]

print(str(max_boxes) + ' ' + str(min_box_side))
