summa = input().split(';')
for i in range(len(summa)):
    summa1 = summa[i].split(',')
    lst = []
    for elem in summa1:
        if int(elem) <= 1000000000:
            continue
        lst.append(elem)
    print(','.join(lst))
