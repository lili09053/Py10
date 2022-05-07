st = input("Введите строку состоящую из латинских букв").lower()
lst = []
key = 'a'
while key != '{':  # следующий символ после Z
    elem = ''  # хранит одинаковые символы
    for sym in st:
        if sym == key:
            elem += sym
    if elem != '':
        lst.append(elem)
    key = chr(ord(key) + 1)
print("".join(lst))