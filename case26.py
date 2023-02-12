a = int(input('print a :'))
b = int(input('Print b :'))


def power(a, b):
    if (b == 1):
        return (a)
    if (b != 1):
        return (a * power(a, b - 1))

print("Результат возведения в степень равен:", power(a, b))