"""Cathartic home project to help me get the shopping."""
from math import ceil
from typing import List

from Shopping.recipes.recipes import *


class ShoppingList:
    """Class to help me sort a weekly shopping list"""

    def __init__(self, recipe_list: List[Recipe] = None, individual_items: List[IngredientQuantity] = None):
        self.recipe_list = recipe_list
        self.individual_items_list = individual_items
        self.ingredients_dict = {}

        self.main()

    def main(self):
        """Main function"""
        self.process_recipes()
        self.process_one_offs()

        self._calculate_purchase_quantity()
        self.organise_shopping_list()

    def process_recipes(self) -> None:
        """Iterates through the recipe_list and calls functions to add ingredients"""
        recipe: Recipe
        ingredient_quantity: IngredientQuantity
        for recipe in self.recipe_list:
            for ingredient_quantity in recipe.ingredients:
                self._extract_ingredients(ingredient_quantity)

    def process_one_offs(self) -> None:
        """Iterates over the one-offs list and adds to the ingredients list"""
        ingredient_quantity: IngredientQuantity
        for ingredient_quantity in self.individual_items_list:
            self._extract_ingredients(ingredient_quantity)

    def organise_shopping_list(self) -> None:
        """Groups the shopping list up according the Categories"""
        sorted_list = [v for _, v in self.ingredients_dict.items()]
        sorted_list = sorted(sorted_list, key=lambda d: d.ingredient.category)

        i: IngredientQuantity
        for i in sorted_list:
            print(f"{i.purchase_qty:<2}x  {i.ingredient.name:12}")

    def _extract_ingredients(self, ingredient_quantity: IngredientQuantity) -> None:
        """
        Parses the ingredient quantity entries and updates the dictionary of ingredients to buy with amounts.
        """
        name = ingredient_quantity.ingredient.name
        number = ingredient_quantity.number
        if ingredient_quantity.ingredient.name in self.ingredients_dict:
            # Ingredient already exists, need to increase the number
            self.ingredients_dict[name].number += number

        else:
            # Ingredient not in dict, adding
            self.ingredients_dict[name] = ingredient_quantity

    def _calculate_purchase_quantity(self) -> None:
        """Depending on how many of an ingredient are required, work out how much needs purchasing"""

        ingredient_quantity_obj: IngredientQuantity
        for name, ingredient_quantity_obj in self.ingredients_dict.items():
            need = ingredient_quantity_obj.number
            item_qty = ingredient_quantity_obj.ingredient.quantity
            purchase_qty = ceil(need / item_qty)

            self.ingredients_dict[name].purchase_qty = purchase_qty

    def _calculate_cost(self) -> None:
        """Placeholder"""
