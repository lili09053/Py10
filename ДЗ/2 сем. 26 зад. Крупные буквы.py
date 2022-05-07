sym = ['   ', '  *', ' * ', ' **', '*  ', '* *', '** ', '***'] # строка из символов
alphabet = ['25755', '65656', '25452'] # закодированные буквы АВС
letter = input()
for i in range(5):
    for j in letter:
        code = int(alphabet[ord(j) - ord('A')][i])
        print("  ".join(sym[code]))



  #  print('  '.join([sym[int(alphabet[ord(j) - ord('A')][i])] ]))
