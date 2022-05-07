n = int(input("Введите количество слов в списке\n"))
lst1 = []  # знаем число элементов
lst2 = []  # вводим до слова СТОП

for elem in range(n):
    word = input("Внесите слово в список\n")
    lst1.append(word)
print(lst1)

slovo = input("Введите слово для создания списка\n")

while slovo != 'стоп':
    lst2.append(slovo)
    slovo = input("Внесите слово в список\n")
print(lst2)




