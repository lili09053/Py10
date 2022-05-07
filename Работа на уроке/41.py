numbers = [int(elem) for elem in input().split()]  # преобразование из строки в число
a, b = [int(elem) for elem in input().split()]
print(sum(numbers[a: b + 1]))

#  *****
numbers = [int(elem)**2 for elem in input().split()]  # преобразование из строки в число
a, b = [int(elem) for elem in input().split()]
print(sum(numbers[a: b + 1]))

