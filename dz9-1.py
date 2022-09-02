k=0
l=0
def F(n):
 global k
 global l
 print('*')
 k=k+1
 #print('k',k)
 if n >= 1:
   print('*')

   l = l + 1
   #print('l',l)
   F(n-1)
   F(n//2)
 #return k+l

n=int(input())
F(n)
#print(F(n))
print('k и l после функции', k+l)
