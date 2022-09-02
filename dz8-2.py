def su_chet_num(a):
    sum_chet=0
    kol_cif=0
    while a>0:
        b=a%10
        a=a//10
        print("отрезок", b)
        if b%2==0:
            sum_chet=sum_chet+b
            kol_cif=kol_cif+1
    print('сумма четн цифр: ',sum_chet, 'количество четн цифр: ',kol_cif)
a = int(input('введите число: '))
su_chet_num(a)


