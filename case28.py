a = int(input('print a :'))
b = int(input('print b :'))
 
 
def sum(a, b):
    if b == 0:
        return a
    return sum(a+1, b-1)
 
 
print(sum(a, b))