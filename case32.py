list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = int(input('Введите минимальное значение :'))
max_number = int(input('Введите максимальное значение :'))
for i in range(len(list)):
    if min_number <= list[i] <= max_number:
        print(i)