import random
digit=int(input('Введите число от 1 до 4: '))
digit_random=random.randint(1,4)
if digit==digit_random:
    print('Победа')
elif digit>digit_random:
    print('Ввели большее число')
elif digit<digit_random:
    print('Ввели меньшее число')
