import random
def spis(sp):
    sp1 = list()
    for i in sp:
        if i%2==0:
            sp1.append(i)
    print('четные отсортированные', sorted(sp1, reverse=True))

sp=list()
for i in range(1,16):
    d=random.randint(1,30)
    sp.append(d)
print(sp)

spis(sp)

