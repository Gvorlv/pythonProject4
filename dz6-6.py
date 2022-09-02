import random
e=[]
for i in range(20):
    d=random.randint(0, 20)
    e.append(d)
print(e)
count=0
krat3=1
for i in e:
    if i%3==0 and count%2==0:
        print('новая i',i, 'счетчик', count)
        krat3=krat3*i
        print('произведение',krat3)
    count += 1
print('произвед=',krat3)


