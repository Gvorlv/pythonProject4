import random
e=[]
for i in range(10):
    d=random.randint(0, 100)
    e.append(d)
e.sort()
print(e)
print(e[2]+e[8])