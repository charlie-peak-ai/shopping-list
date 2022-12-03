from Shopping.recipes.core import Categories as c
from Shopping.recipes.core import Ingredient
from Shopping.recipes.core import Quantities as q

TinLentils = Ingredient(name="Tin Lentils", category=c.Tinned, est_price=0.5, quantity=q.Tin)
TinTomatoes = Ingredient(name="Tin Tomatoes", category=c.Tinned, est_price=0.5, quantity=q.Tin)
TinBlackBean = Ingredient(name="Tin Black Beans", category=c.Tinned, est_price=0.5, quantity=q.Tin)
CoconutMilk = Ingredient(name="Tin Coconut Milk", category=c.Tinned, est_price=0.5, quantity=q.Tin)
KidneyBeans = Ingredient(name="Kidney Beans", category=c.Tinned, est_price=1, quantity=q.Tin)

Passatta = Ingredient(name="Passatta", category=c.DryGood, est_price=0.5, quantity=500)
TomatoPuree = Ingredient(name="TomatoPuree", category=c.DryGood, est_price=0.5, quantity=500)

Rice = Ingredient(name="Rice", category=c.DryGood, est_price=1, quantity=q.Pack)
Pasta = Ingredient(name="Pasta", category=c.DryGood, est_price=1, quantity=q.Pack)

JalfreziPaste = Ingredient(name="Jalfrezi Paste", category=c.Sauce, est_price=1, quantity=q.Jar)
MangoChutney = Ingredient(name="Mango Chutney", category=c.Sauce, est_price=1, quantity=q.Jar)
ThaiCurrySauce = Ingredient(name="Thai Curry Sauce", category=c.Sauce, est_price=1, quantity=q.Jar)
