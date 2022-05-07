class FoodInfo:

    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def get_proteins(self):
        return self.proteins

    def get_fats(self):
        return self.fats

    def get_carbohydrates(self):
        return self.carbohydrates

    def get_kcalories(self):
        return (4 * self.proteins.__add__(9 * self.fats)).__add__(4 * self.carbohydrates)

    def __add__(self, other):
        return fi1.__add__(fi2)


#  fi = FoodInfo(proteins, fats, carbohydrates)
fi1 = FoodInfo.get_kcalories()
fi2 = FoodInfo.get_kcalories()
fi = FoodInfo.__add__()
print(fi)

