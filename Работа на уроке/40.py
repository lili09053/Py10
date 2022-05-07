words = input("Введите строку \n").split()
words_with_lenghts = [(len(word), word) for word in words]
print(max(words_with_lenghts))

#  ****
print(max([(len(word), word) for word in input("Введите строку повторно\n").split()]))
