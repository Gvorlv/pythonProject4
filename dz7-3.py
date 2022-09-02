import random
dct={}
d=1
for i in range(10):
        d=random.randint(1, 100)
        if d not in dct:

            print('ввод:')
            fio = input('введите имя и фамилию: ')
            dct[d]=fio

            print('В словарь добавляются элементы:')
            print(d, '::', dct.get(d))
            print(dct)


