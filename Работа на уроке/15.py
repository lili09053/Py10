number = int(input())
figure1 = int(str(number)[0])
while number < 1000000000:
    if figure1 == 1:
        break
    else:
        number *= figure1
    figure1 = int(str(number)[0])

print(number)
