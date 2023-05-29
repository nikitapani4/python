s = int(input('Введите сумму чисел: '))
p = int(input('Введите произведение чисел: '))

x = 1

while x != p:
    y = p / x
    if x + y == s:
        print(x)
        x = p
    else:
        x += 1
if y % int(y) != 0:
    print('Таких чисел нет!')
else:
    print(int(y))
    
