import random
e=[]
for i in range(10):
    d=random.randint(0, 10)
    e.append(d)
print(e)
s=sum(e, start=0)
kol=len(e)
srar=s/kol
print(f'сумма= {s}; сред ариф ={srar}')

for j in e[-1::-1]:
    if j<5:
        e.remove(j)
print(e)

