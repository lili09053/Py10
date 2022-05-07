"""
number = input().split()
lst = []
for elem in number:
    elem_1 = int(elem)
    if elem_1 % 2 != 0 and elem_1 % 10 != 3 and elem_1 % 10 != 7:
        new_elem = str(elem_1 ** 2)
        lst.append(new_elem)

print(" ".join(lst))
"""

print(" ".join([str(int(elem) ** 2) for elem in input().split() if
                int(elem) % 2 != 0 and int(elem) % 10 != 3 and int(elem) % 10 != 7]))
