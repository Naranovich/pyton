a = int(input('введите a: '))
b = int(input('введите b: '))
c = int(input('введите c: '))
progressive = [a + (i - 1) * c for i in range(1, b + 1)]
print(*progressive)