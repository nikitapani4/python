n = int(input('Введите номер билета: '))

x1 = n % 10
n //= 10
x2 = n % 10
n //= 10
x3 = n % 10
n //= 10
y1 = n % 10
n //= 10
y2 = n % 10
n //= 10
y3 = n % 10
n //= 10

if (x1 + x2 + x3) == (y1 + y2 + y3):
    print('Yes')
else:
    print('No')