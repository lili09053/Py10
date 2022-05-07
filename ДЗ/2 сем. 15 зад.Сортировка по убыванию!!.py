n = int(input("Введите количество элементов\n"))
a = []
for _ in range(n):  # добавляем элементы в список
    a.append(int(input("Введите элемент\n")))
for i in range(n - 1):
    for j in range(n - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
a1 = a[:: -1]
print(a1)