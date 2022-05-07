class Selector:

    def __init__(self, lst=None):
        if lst:
            self.lst = lst.copy()
        else:
            self.lst = []

    def get_odds(self):
        lst1 = []
        for elem in self.lst:
            if elem % 2 != 0:
                lst1.append(elem)
        print(*lst1)

    def get_evens(self):
        lst2 = []
        for elem in self.lst:
            if elem % 2 == 0:
                lst2.append(elem)
        print(*lst2)


sel = Selector([1, 2, 3, 4, 5, 6, 7, 8])
sel.get_evens()
sel.get_odds()