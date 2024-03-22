import random
rows = 3
cols = 3
matrix = [[random.randint(1, 10) for j in range(cols)] for i in range(rows)]
print("Initial matrix:")
for row in matrix:
    print(row)
number = int(input("Enter the column number to double the values: "))
# Double the elements in the selected column
matrix = list(map(lambda row, idx: [elem * 2 if idx == number - 1 else elem for idx, elem in enumerate(row)], matrix, range(len(matrix))))
print("Updated matrix:")
for row in matrix:
    print(row)
