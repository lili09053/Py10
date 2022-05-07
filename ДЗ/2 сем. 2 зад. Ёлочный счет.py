n = int(input())
current_num = 1
current_line = 1
while current_num <= n:
    for i in range(current_line):
        print(current_num, end=' ')
        current_num += 1
        if current_num > n:
            break
    current_line += 1
    print()
