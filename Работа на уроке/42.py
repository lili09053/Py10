words = input().upper().split()  # получаем список слов
letters_of_words = [list(word) for word in words]
robo_words = ['-'.join(lst) for lst in letters_of_words]
print(' '.join(robo_words))

# ****

print(' '.join(['-'.join(elem) for elem in [list(word) for word in input().upper().split()]]))
