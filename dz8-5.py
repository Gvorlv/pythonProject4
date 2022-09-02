import random
def spis_unik(sp):
    mnoj = set(sp)
    print('список с уник элем', list(mnoj))

sp=list()
for i in range(1,21):
    d=random.randint(1,10)
    sp.append(d)
print(sp)

spis_unik(sp)

