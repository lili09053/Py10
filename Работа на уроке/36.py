lst = []


for elem in range(int(input())):
    lst.append(elem ** 2)

print(*[i for i in lst], sep='\n')
