import math
p=3.14
def pltrap(a, b, h): #площадь трапеции
    return (a+b)/2*h
def plkrug(r): #площадь круга
    return p*(r**2)
def plkolca(rb, rm): #площадь кольца
    return p * ((rb**2)-(rm**2))
def plpovkonus(h, r): #площадь боковой поверхности конуса
    return p*r*(math.sqrt(r**2+h**2))