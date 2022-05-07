class A:
    def __init__(self, a=3):
        self.a = a


class B(A):
    pass


class D:
    def __init__(self, a=5):
        self.a = a


class C(D, B):
    pass


c = C()
print(c.a)
