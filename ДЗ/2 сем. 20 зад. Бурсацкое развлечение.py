# n = input()
# #a = 0 #while int(n) < 1000000000:
# a = int(n[0]) * int(n)
#  if n[0] == 1:
#  break
# n = a
# #print(a)
# ----------------------------------------------
n = int(input())
number = n
figure1 = int(str(n)[0])
while number < 1000000000:
    if figure1 == 1:
        break
    else:
        number *= figure1
    figure1 = int(str(number)[0])

print(number)
