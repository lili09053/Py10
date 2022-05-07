class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        if a + b < c or a + c < b or b + c < a:
            raise AttributeError("Строны треугольника заданы неверно")

    def perimeter(self):
        return self.a + self.b + self.c


class EquilateralTriangle(Triangle):

    def __init__(self, a):
        super().__init__(a, a, a)


k = EquilateralTriangle(3)
print(k.perimeter())

a = Triangle(1, 1, 3)