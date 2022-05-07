class Balance:

    def __init__(self):
        self.left = 0
        self.right = 0

    def add_right(self, n):
        self.right += n

    def add_left(self, m):
        self.left += m

    def result(self):
        if self.right > self.left:
            return "R"
        if self.right < self.left:
            return "L"
        if self.right == self.left:
            return "="


balance = Balance()
balance.add_left(10)
balance.add_right(5)
print(balance.result())
