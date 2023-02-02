a = int(input('введите первое число :'))
b = int(input('введите второе число:'))
for i in range (a + b):
    for j in range(a + b):
        if i + j == a and i * j == b:
            print(([i, j]))

