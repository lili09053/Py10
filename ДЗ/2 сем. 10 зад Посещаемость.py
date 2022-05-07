number_of_pages = int(input("Введите количество листов\n"))
list_of_surnames = set()  # Список присутствующих на конкретном уроке (начиная со второго урока)
list_of_attendees = set()  # Список присутствующих на всех уроках (на первом уроке присуствовали все, кто на нём был
number_of_rows = int(input("Введите количество присутствующих на 1-ом уроке\n"))
for j in range(number_of_rows):  # цикл для первого листочка (если был один урок, то на всех уроках присутствовали
    # все, кто был на первом уроке)
    list_of_attendees.add(input("Введите фамилию присутствующего\n"))
for i in range(number_of_pages - 1):
    number_of_rows = int(input("Введите количество присутствующих на уроке\n"))
    for j in range(number_of_rows):
        list_of_surnames.add(input("Введите фамилию присутствующего\n"))
list_of_attendees = list_of_attendees & list_of_surnames
for elem in list_of_attendees:
    print(elem)
