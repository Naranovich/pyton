n = int(input('введите значение n :'))
a = map(int, input().split())
x = int(input('введите значение x :'))
print(sum(map(lambda z: int(z == x), a)))