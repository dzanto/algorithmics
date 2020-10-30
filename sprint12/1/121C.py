num = int(input('Введите количество цифр числа Х: '))
x = list(input('Введите списочную форму числа Х: ').split())
k = int(input('Введите число К: '))
x_int = int(''.join(x))
sum_kx = x_int + k
sum_kx = list(str(sum_kx))
space = ' '
for i in range(len(sum_kx)):
    if i == len(sum_kx)-1:
        space = ''
    print(sum_kx[i], end=space)
