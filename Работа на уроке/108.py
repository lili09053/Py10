class ReversedList:

    def __init__(self, lst):
        self.lst = list(lst)[::-1]

    def __getitem__(self, i):
        return self.lst[i]

    def __len__(self):
        return len(self.lst)


rl = ReversedList([10, 20, 30, 40])
print(rl[1])
for i in range(len(rl)):
   print(rl[i])
