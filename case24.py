n = int( input( 'Введите число кустов ' ) )
lis = [ int(x) for x in input( 'Введите количество ягод на кусте ' ).split() ]
n = len(lis)
lis = lis + lis[:2]
ma = 0
for i in range(n):
    ma = max( ma, lis[i] + lis[i+1] + lis[i+2] )
print(ma)