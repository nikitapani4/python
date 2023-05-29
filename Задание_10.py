n = int(input('Введите число монеток: '))

count = 0

for i in range(n):
    i = int(input('Какой стороной лежит монетка (1 - орел, 0 - решка): '))
    if i == 1:
        count += 1
        
if count <= n - count:
    print(f'Необходимо перевернуть {count} монеток')
else:
    print(f'Необходимо перевернуть {n - count} монеток')