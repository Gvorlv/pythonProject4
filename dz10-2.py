f=open('zadanie2.txt')
count=0
for i in f:
    if i!='\n':
        count+=1
        #print(i, end='')
print(count)


