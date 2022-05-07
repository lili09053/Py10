nstep = int(input())
st = input()
for elem in range(len(st)):
    if st[elem] != " " and st[elem] != "," and st[elem] != '!' and st[elem] != "1":
        elem = int(ord(st[elem]) + nstep)
        print(chr(elem), end='')
    else:
        # a = chr(elem)
        # print(a.replace('%', " "))
        print(st[elem], end="")

