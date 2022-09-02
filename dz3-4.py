a = int(input("введите цифру "))
count_chet = 0
sum_chet = 0
i=1
while i <=a:
    i=i+1
    if  i % 2 == 0:
        count_chet = count_chet + 1
        sum_chet = i + sum_chet

print('количество четных цифр: ', count_chet)
print('сумма четных цифр: ', sum_chet)

