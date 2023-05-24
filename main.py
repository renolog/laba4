def r1():
    try:
        a = int(input('Введите число:'))
        b = a % 3
    except ValueError:
        print('Это не число!')
    else:
        if b == 0 and a != 0:
            print('Число', a, 'делится на 3')
        elif a == 0:
            print('Введен ноль!!!')
        else:
            print('Число', a, 'не делится на 3!')

def r2():
    try:
        a = int(input('Введите число:'))
        b = 100 / a
    except ZeroDivisionError:
        print('Введен 0!')
    except ValueError:
        print('Это не число!')
    else:
        print('Результат:', b)

def r3():
    data = input('Ведите дд.мм.гггг:')
    data = data.split('.')
    if int(data[0]) * int(data[1])== int(data[2][2:4]):
        print('Магическая дата! Ура!')
    else:
        print('Увы... Это не магическая дата')

def r4():
    bil = input('Введите номер билет:')
    a = 0
    b = 0
    if len(bil) % 2 == 0:
        for i in bil[0:int(len(bil) / 2)]:
            a = a + int(i)
        for i in bil[int(len(bil) / 2) : int(len(bil)) + 1]:
            b = b + int(i)
        if a == b:
            print('Вам повезло! Это счастливый билет!')
        else:
            print('Увы... Не повезло.')
    else:
        print('Количество цифр нечетное!!!')
r4()
