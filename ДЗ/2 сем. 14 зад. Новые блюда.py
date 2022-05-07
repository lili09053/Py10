m = int(input("Введите число блюд, которое может приготовить столовая\n"))
the_name_of_the_dishes = set()
the_name_of_the_dishes_at_every_day = set()

for i in range(m):
    the_name_of_the_dishes.add(input("Введите название блюда\n"))

n = int(input("Введите число дней для которых есть списки блюд\n"))

for j in range(n):
    k = int(input("Введите количество блюд\n"))
    for _ in range(k):
        the_name_of_the_dishes_at_every_day.add(input("Введите название блюд на день\n"))

diff = the_name_of_the_dishes - the_name_of_the_dishes_at_every_day

for elem in diff:
    print(elem)
