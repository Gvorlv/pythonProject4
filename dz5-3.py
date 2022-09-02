a=input()
b=[]
col=0
for i in range(len(a)):
    b=b+a[i]
for j in range(len(b)):
    if b[j].isdigit():
        col+=1
print(f'В введенной строке : {col} цифр')