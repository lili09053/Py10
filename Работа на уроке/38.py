"""
c = input()
b = ([str(int(i) ** 2) for i in c.split(" ")])
print(" ".join(b))

b = ([str(int(i) ** 2) for i in c.split(" ") if str(int(i) ** 2)[-1]!='9'])
print(" ".join(([str(int(i) ** 2) for i in input().split(" ") if str(int(i) ** 2)[-1]!='9'])))
"""
number = input().split()
lst = [str(int(elem) ** 2) for elem in number]
print(" ".join(lst))