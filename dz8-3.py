def fkt(n):
    fact=1
    for i in range(2,n+1):
       fact=fact*i
    print("The factorial of ",n," is: ",fact)
n=int(input())
fkt(n)