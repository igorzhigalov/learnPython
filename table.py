value=input('Введите номер элемента: ')
if len(value)>0:
    el=int(value)
    if el==3:
        print('Литий')
    if el==25:
        print('Марганец')
    if el==80:
        print('Ртуть')
    if el==17:
        print('Хлор')
    else:
        print('Что это?')
else:
    print('Введите номер элемента!')
