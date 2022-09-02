dict={
    'день' : 'day',
    'кот' : 'cat',
    'мышь' : 'mouse',
    'собака' : 'dog',
    'животные' : 'animals',
'карта' : 'map',
'дверь' : 'Door',
'медведь' : 'bear',
'май' : 'may',
'вода' : 'water',

}

for i in range(5):
    print('ввод:')
    rus_kl=input('введите русское слово: ')
    ing_znach=input('Введите перевод: ')
    dict[rus_kl]=ing_znach
    print('В словарь добавляется :')
    print(f'{rus_kl} : {ing_znach}')


