from burger import Burger
from database import Database
from ingredient import Ingredient
from bun import Bun


def get_available_buns():
    available_buns = {}
    database = Database()
    buns = database.available_buns()
    for bun in buns:
        available_buns[bun.name] = bun.price
    return available_buns

def get_available_ingredients():
    sauces = {}
    fillings = {}

    database = Database()
    ingredients = database.available_ingredients()

    for ingredient in ingredients:
        if ingredient.type == 'SAUCE':
            sauces[ingredient.name] = ingredient.price
        elif ingredient.type == 'FILLING':
            fillings[ingredient.name] = ingredient.price

    return {'sauce': sauces, 'filling': fillings}

def create_bun(name, price):
    bun = Bun(name, price)
    return bun


def create_burger():
    burger = Burger()
    return burger

def create_ingredient(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    return ingredient
