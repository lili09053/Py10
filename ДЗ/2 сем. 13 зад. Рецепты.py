m = int(input("Введите количество продуктов в холодильнике\n"))
food_in_the_refrigerator = set()
recipes = set()

for i in range(m):
    food_in_the_refrigerator.add(input("Введите название продукта в холодильнике\n"))

n = int(input("Введите количество рецептов\n"))

for j in range(n):
    the_name_of_the_recipe = input("Введите название рецепта\n")
    number_of_ingredients = int(input("Введите количество ингридиентов\n"))
    list_of_ingredients = set()

    for k in range(number_of_ingredients):
        list_of_ingredients.add(input("Введите название ингридиента\n"))
    intersection = list_of_ingredients & food_in_the_refrigerator

    if intersection == list_of_ingredients:
        recipes.add(the_name_of_the_recipe)

for elem in recipes:
    print(elem)
