from ShoppingList import *

if __name__ == "__main__":
    ShoppingList(
        recipe_list=[Bolognese, SweetPotatoChilli, ThaiCurry, SausageParp],
        individual_items=[
            IngredientQuantity(ingredient=Porridge, number=10),
            IngredientQuantity(ingredient=Milk, number=2),
            IngredientQuantity(ingredient=Bread, number=2),
            IngredientQuantity(ingredient=Apples, number=1),
            IngredientQuantity(ingredient=Jam, number=1),
            IngredientQuantity(ingredient=Coffee, number=1),
            IngredientQuantity(ingredient=Pasta, number=4),
        ],
    )
