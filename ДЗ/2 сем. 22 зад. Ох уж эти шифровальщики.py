st = input()
for elem in range(len(st)-1):
    print(ord(st[elem]), end=', ')
print(ord(st[len(st)-1]), end=' ')
