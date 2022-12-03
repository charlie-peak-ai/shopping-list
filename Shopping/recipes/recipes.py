from Shopping.recipes.core import IngredientQuantity, Recipe
from Shopping.recipes.ingredients import *

Bolognese = Recipe(
    name="Bolognese",
    serves=12,
    ingredients=[
        IngredientQuantity(ingredient=Bacon, number=6),
        IngredientQuantity(ingredient=Mince, number=1),
        IngredientQuantity(ingredient=RedOnion, number=4),
        IngredientQuantity(ingredient=TinLentils, number=3),
        IngredientQuantity(ingredient=TinTomatoes, number=4),
    ],
)
SweetPotatoChilli = Recipe(
    name="Sweet Potato Chilli",
    serves=12,
    ingredients=[
        IngredientQuantity(ingredient=CuminSeeds, number=1),
        IngredientQuantity(ingredient=ChilliPaste, number=1),
        IngredientQuantity(ingredient=RedOnion, number=2),
        IngredientQuantity(ingredient=FreshCoriander, number=1),
        IngredientQuantity(ingredient=TinBlackBean, number=3),
        IngredientQuantity(ingredient=TinTomatoes, number=3),
        IngredientQuantity(ingredient=FetaCheese, number=3),
    ],
)

ThaiCurry = Recipe(
    name="Thai Curry",
    serves=6,
    ingredients=[
        IngredientQuantity(ingredient=ThaiCurrySauce, number=1),
        IngredientQuantity(ingredient=SpringOnion, number=2),
        IngredientQuantity(ingredient=RedPepper, number=2),
        IngredientQuantity(ingredient=CoconutMilk, number=2),
        IngredientQuantity(ingredient=Chicken, number=4),
    ],
)

SausageParp = Recipe(
    name="Sausage Parp",
    serves=2,
    ingredients=[
        IngredientQuantity(ingredient=Sausage, number=3),
        IngredientQuantity(ingredient=Passatta, number=200),
        IngredientQuantity(ingredient=FennelSeeds, number=1),
        IngredientQuantity(ingredient=FreshPasta, number=1),
        IngredientQuantity(ingredient=FreshParsely, number=0.5),
    ],
)
