from Shopping.recipes.core import Recipe, IngredientQuantity
from Shopping.recipes.ingredients import *

Bolognese = Recipe(
    name="Bolognese",
    serves=16,
    ingredients=[
        IngredientQuantity(ingredient=Bacon, number=1),
        IngredientQuantity(ingredient=Mince, number=1),
        IngredientQuantity(ingredient=RedOnion, number=4),
        IngredientQuantity(ingredient=TinLentils, number=3),
        IngredientQuantity(ingredient=TinTomatoes, number=4),
    ],
)
