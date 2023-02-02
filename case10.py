n = int(input('введите количество монет'))
count = 0
min_count = 0
for i in range(n):
    temp = int(input())
    if temp > 0:
        count += 1
    else:
        if min_count < count:
            min_count = count = count
        count = 0
print(f'Result {min_count}')



