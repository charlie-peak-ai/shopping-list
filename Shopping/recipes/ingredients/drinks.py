from Shopping.recipes.core import Categories as c
from Shopping.recipes.core import Ingredient
from Shopping.recipes.core import Quantities as q

Wine = Ingredient(name="Wine", category=c.Alcohol, est_price=1, quantity=q.Bottle)
Tonic = Ingredient(name="Tonic", category=c.Alcohol, est_price=1, quantity=q.Can)
Beer = Ingredient(name="Beer", category=c.Alcohol, est_price=1, quantity=q.Can)
Juice = Ingredient(name="Juice", category=c.Drink, est_price=1, quantity=q.Bottle)
