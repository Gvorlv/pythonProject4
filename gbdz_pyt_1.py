'''
1. Поработайте с переменными, создайте несколько, выведите на экран.
Запросите у пользователя некоторые числа и строки и сохраните в переменные,
затем выведите на экран.
'''
per1=int(input('введите целое число'))
per2=input('введите строку')
per3=True
print (per1, per2, per3)

'''
2. Пользователь вводит время в секундах. 
Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. 
Используйте форматирование строк.
'''
sek1=int(input())
chas=sek1//3600
#print(chas, 'час')
ostsek=sek1-(chas*3600)
minu=ostsek//60
#print(minu, 'минут')
sek2=ostsek%60
#print(sek2, 'сек')
print(f'{chas} час {minu} минут {sek2} секунд')

'''
3. Узнайте у пользователя число n. 
Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. 
Считаем 3 + 33 + 333 = 369.
'''
chis=input('введите число')
chis0=int(chis)
chis1=int(chis*2)
chis2=int(chis*3)
print(chis0+chis1+chis2)

'''
4. Пользователь вводит целое положительное число. 
Найдите самую большую цифру в числе. 
Для решения используйте цикл while и арифметические операции.
'''
chislo=int(input())
nost=0
kost=0
maxchis=0
while chislo>0:
    kost = chislo % 10
    chislo=chislo//10

    if maxchis<kost:
        maxchis=kost
print(maxchis)

'''
5. Запросите у пользователя значения выручки и издержек фирмы. 
Определите, с каким финансовым результатом работает фирма. 
Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. 
Выведите соответствующее сообщение.
'''
'''
6. Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке. 
Далее запросите численность сотрудников фирмы 
и определите прибыль фирмы в расчёте на одного сотрудника.
'''
vir=int(input('введите выручку'))
izd=int(input('введите издержки'))
itog=vir-izd
if itog>0:
    print('компатия с прибылью')
    rent = itog / vir
    print(f'рентабельность={rent}')
    kolsotr = int(input('введите колич сотрудников'))
    prib_na_sotr=itog/kolsotr
    print(f'прибыль на сотрудника={prib_na_sotr}')

elif itog==0:
    print('прибыль = 0')
else:
    print('компатия с убытком')

'''
7 (Дополнительно). Спортсмен занимается ежедневными пробежками. 
В первый день его результат составил a километров. 
Каждый день спортсмен увеличивал результат на 10% относительно предыдущего. 
Требуется определить номер дня, на который результат спортсмена составит не менее b километров. 
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
'''
res1den=int(input('результат в 1й день'))
kilomnemenee=int(input('не менее'))
i=1
c=0
while kilomnemenee > res1den:
    print(f'{i} день {res1den} км')
    res1den = res1den + res1den*0.1
    i=i+1
print(f'{i} день {res1den} км')



