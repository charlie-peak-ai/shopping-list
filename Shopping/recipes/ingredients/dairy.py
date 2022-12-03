from Shopping.recipes.core import Categories as c
from Shopping.recipes.core import Ingredient
from Shopping.recipes.core import Quantities as q

Milk = Ingredient(name="Milk", category=c.Dairy, est_price=0.5, quantity=q.Poly)
Cheese = Ingredient(name="Cheese", category=c.Dairy, est_price=0.5, quantity=q.Pack)
Eggs = Ingredient(name="Eggs", category=c.Dairy, est_price=1, quantity=q.Pack)
FetaCheese = Ingredient(name="Feta Cheese", category=c.Dairy, est_price=0, quantity=q.Pack, shop="Asda")
FreshPasta = Ingredient(name="Fresh Pasta", category=c.Dairy, est_price=0, quantity=2, shop="Tesco")
