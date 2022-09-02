with open('zadanie3.txt') as f:
    cf=["a", "b", "c", "d"]
    nf=["aa", "bb", "cc", "dd"]

    pus_st = '\n'
    #for i in f:
    k=f.readlines() #создаю переменную куда записываю список из сток файла
    #print(k)

    print(k)
    #st='\n'
    for j in range(0,4):  #делаю цикл для создания 4 файлов с именем j
        #cf=cf[j]
        #nf=[j]
        cf[j]=open(nf[j], 'w')
        for i in k: #пытаюсь добавить хоть какие то строки из переменной k в файл j
            cf[j].write(i)


            if i==pus_st: #добавляю пока не наткнусь на пустую строку

                break  #пытаюсь перейти ко 2й итерации цикла с j чтобы создать 2й файл но судя по всему ничего не работает


            #print(i)
        #print('1',j)





# for i in k:
#     while i!='\n':
#
#
#
# count=0
# for i in f:
#     if i!='\n':
#         count+=1
#         #print(i, end='')
# print(count)
#
#
