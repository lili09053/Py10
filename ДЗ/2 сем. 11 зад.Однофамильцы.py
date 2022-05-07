n = int(input("Введите количество работников\n"))
surnames = set()
same = set()    # Список однофамильцев (первых мы не досчитываем, будем приблавлять размер множества к итоговому счёту)
count = 0

for _ in range(n):
    elem = input("Введите фамилию сотрудника\n")
    if elem in surnames:
        count += 1
        same.add(elem)
    else:
        surnames.add(elem)
if count == 0:
    print(count)
else:
    print(count + len(same))
