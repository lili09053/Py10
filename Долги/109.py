#(+ метод __call__)

class SquareFunction:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        return self.a * x ** 2 + self.b * x + self.c


k = SquareFunction(1, 7, 9)
print(k(-2))

