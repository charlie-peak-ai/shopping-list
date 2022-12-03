from Shopping.recipes.core import Categories, Ingredient, Quantities

Bacon = Ingredient(name="Bacon", category=Categories.Meat, est_price=2.50, quantity=12)
Mince = Ingredient(name="Mince", category=Categories.Meat, est_price=3.0, quantity=Quantities.Pack)
Chicken = Ingredient(name="Chicken", category=Categories.Meat, est_price=1, quantity=6)
Sausage = Ingredient(name="Sausage", category=Categories.Meat, est_price=2, quantity=8)
