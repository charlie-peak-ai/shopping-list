from enum import Enum
from typing import List, Union

from pydantic import BaseModel, Field, validator


class Categories(Enum):
    """Food Categories, roughly grouped to make navigating Aldi easier"""

    Meat = 22
    Veg = 1
    Fruit = 2
    Dairy = 3
    Cleaning = 4
    Seasoning = 5
    Alcohol = 6
    Breakfast = 7
    Tinned = 8
    Sauce = 9
    Drink = 10
    DryGood = 11


class Quantities(Enum):
    """Helper class with common purchase quantities"""

    Tin = 1
    Pack = 1
    Jar = 1
    Poly = 1
    Bottle = 1
    Can = 1


class ShoppingBaseModel(BaseModel):
    """Custom BaseModel"""

    class Config:
        """Config settings"""
        use_enum_values = True

    @validator("name", check_fields=False)
    def set_name_to_lowercase(cls, v: str):
        """On all subclasses will set the name value to lower case."""
        return v.lower()


class Ingredient(ShoppingBaseModel):
    """Base Ingredient Class"""

    name: str = Field(..., description="Name of the ingredient")
    category: Union[Categories, int] = Field(..., description="Logical grouping")
    est_price: float = Field(1, description="Rough estimate for cost")
    quantity: Union[Quantities, int] = Field(..., description="How much is one purchase, pack size etc")
    shop: str = Field("Aldi", description="Where to buy this from")


class IngredientQuantity(ShoppingBaseModel):
    """Class for ingredients required in a recipe, quantity"""

    ingredient: Ingredient = Field(..., description="The base ingredient")
    number: int = Field(..., description="How many are required")
    purchase_qty: int = Field(None, description="How many to actually buy")


class Recipe(ShoppingBaseModel):
    """Base Class for a Recipe"""

    name: str = Field(..., description="Name of the recipe")
    ingredients: List[IngredientQuantity] = Field(..., description="List of Ingredients")
    serves: int = Field(..., description="How many servings this makes")
