lst = []

for elem in range(int(input())):
    lst.append(str(elem ** 2))

print(" ".join(lst))

# ----------------------------------------------------------------

print(" ".join([str(elem ** 2) for elem in range(int(input()))]))
