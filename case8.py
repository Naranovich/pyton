n = int(input('Введите  число n :'))
m = int(input('Введите  число m :'))
k = int(input('Введите  число k :'))
if k < m * n and (k % m == 0) or (k % n == 0):
    print('Yes')
else:
    print('No')