class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def func(self, other):
        return self.x == other.x and self.y == other.y


p = Point(1, 2)
a = Point(3, 2)

print(p.func(a))

