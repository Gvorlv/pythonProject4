a=input()
b=0
c=0
for i in range(0,3):
    b=b+int(a[i])
for i in range(3,6):
    c=c+int(a[i])
if b==c:
    print('билет счастливый')
else:
    print('билет обычный')
# вариант 2
d=0
e=0
ab=list(a)
abchis=[int(x) for x in ab]
for j in range(0,3):
    d=d+abchis[j]
for j in range(3,6):
    e=e+abchis[j]
if d==e:
    print('билет счастливый')
else:
    print('билет обычный')