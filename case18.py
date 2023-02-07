l = input('Введите размерность массива :')
numbers = list(map(int, input().split()))
x = int(input('Введите число :'))

res = numbers[0]
for i in numbers:
    if abs(i - x) < abs(res - x):
        res = i

print(res)
