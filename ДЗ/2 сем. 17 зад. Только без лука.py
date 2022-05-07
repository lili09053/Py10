n = int(input("Введите количество рецептов\n"))
lst = []
for i in range(n):
    points = input("Введите пункты рецепта\n")
    if "лук" in points:
        continue
    lst.append(points)
print(", ".join(lst))

