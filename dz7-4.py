dct={
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
dkey=dct.keys()
dval=dct.values()
#print(dval)
#print(dkey)
for i in dkey:
    if len(i)<=4:
        print('ключи <=4 ',i)
for i in dkey:
    if len(i)>=5:
        print('ключи >=5 ',i)
for i in dval:
    if len(i)<=4:
        print('значения <=4 ',i)
for i in dval:
    if len(i)>=5:
        print('значения >=5 ',i)