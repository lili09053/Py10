word = input()
position = int(input())
favorite_character = input()
for elem in range(1, len(word)):

if word[elem] == favorite_character:
    print('Да')
elif word[elem] != favorite_character:
        print('Нет')
else:
        print('Ошибка')
