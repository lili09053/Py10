lst1 = ["Районы", "Жилые", "Я", "Ухожу"]
lst2 = ["Кварталы", "Массивы", "Ухожу", "Красиво"]
lst3 = []
i = 0
while i < len(lst1):
    lst3.append(lst1[i])
    lst3.append(lst2[i])
    i += 1
print(lst3)