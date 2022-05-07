import sys
total = 0
count = 0
for elem in sys.stdin:
    total += int(elem.strip())
    count += 1
print(total/count)

# -----------------------------------------------------------------------------------------------
import sys
lst = list(map(int, sys.stdin))
print(sum(lst)/len(lst))


