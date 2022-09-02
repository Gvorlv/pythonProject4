import random
b=set()
c=set()
d=0
e=0
while len(b)!=20:
    d=random.randint(0, 100)
    if d not in b:
        b.add(d)
while len(c)!=20:
    e=random.randint(0, 100)
    if e not in c:
        c.add(e)
print(b)
print(c)
print(b|c, 'объединение')
print(b&c, 'пересечение')
print(b-c, 'разность')




