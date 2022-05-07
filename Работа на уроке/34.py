# условие задачи: извлечь каждое третье слово. использовать split и join
st = input().split()[2::3]


# ----------------------------------------
st = input().split()
for elem in range(2, len(st), 3):
    print(st[elem], end=' ')








