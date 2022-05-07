n = int(input("Введите количество лекарств\n"))
list_of_herbs = set()
for i in range(n):
    m = int(input("Введите количество компонентов\n"))
    for j in range(m):
        list_of_herbs.add(input("Введите название травы\n"))
for elem in list_of_herbs:
    print(elem)
