
c=list(input())
kol_a=c.count('a')
kol_e=c.count('e')
kol_u=c.count('u')
if kol_a>0:
    for i in range(kol_a):
        c.remove('a')
if kol_e>0:
    for i in range(kol_e):
        c.remove('e')
if kol_u>0:
    for i in range(kol_u):
        c.remove('u')
print(c)