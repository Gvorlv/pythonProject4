e=[]
for i in range(10):
    c=int(input())
    e.append(c)
print('исходный список', e)
t=[]
for d in range(10):
    if d%2==0:
        t.append(e[d])
print('список для очистки',t)
for f in t:
    e.remove(f)
print('очищенный список',e)