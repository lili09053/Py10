
lst = []
lst1 = []
word = input("Введите слово для создания списка\n")

while word != 'стоп':
    lst.append(word)
    word = input("Внесите слово в список\n")

for slovo in lst:
    slovo1 = "".join(reversed(list(slovo)))
    lst1.append(slovo1)

intersection = list(set(lst) & set(lst1))

value_index = []

for elem in intersection:
    value_index.append(lst.index(elem))

print(sorted(value_index))


"""
index = 0
for elem in lst:
    ispolyndrom = True
    i = 0
    while (ispolyndrom != False or i <  len(elem) // 2 + 1):
        print(i)
        if elem[i] != elem[len(elem) - 1 - i]:
            ispolyndrom = False
        i += 1
    if ispolyndrom == True:
            print(index)
    index += 1
"""
