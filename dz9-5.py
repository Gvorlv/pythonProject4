import time
def decor(fff):
    def wrapper(n):
        start_time = time.time()
        fff(n)
        end_time = time.time()-start_time
        print(end_time)
    return wrapper
@decor
def fkt(n):
    fact = 1
    for i in range(2, n + 1):
        fact = fact * i
    print("The factorial of ", n, " is: ", fact)
n = int(input())
fkt(n)

#fk=decor(fkt)
#fk()
