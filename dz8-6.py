def int_num(n):
    k=0
    for i in range(2,n):
        if n%i!=0:
            k=k+1
            #print('k',k)
            #print('i', i)
    if k==i-1:
            print('число простое')

    else:
            print('число составное')

n=int(input('введите число: '))
int_num(n)