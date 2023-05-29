n = int(input('Введите N: '))
m = int(input('Введите M: '))
k = int(input('Введите K: '))

if ((k % m == 0) or (k % n == 0)) and (k < (m*n)):
    print('Yes')
else:
    print('No')