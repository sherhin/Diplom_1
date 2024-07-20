from burger import Burger
from database import Database
from ingredient import Ingredient
from bun import Bun

class Helpers:

    @staticmethod
    def get_available_buns():
        """Метод получения доступных булочек"""
        available_buns = {}
        database = Database()
        buns = database.available_buns()
        for bun in buns:
            available_buns[bun.name] = bun.price
        return available_buns

    @staticmethod
    def create_bun(name, price):
        """Метод создания булочки"""
        bun = Bun(name, price)
        return bun

    @staticmethod
    def create_burger(bun=None, sauce=None, filling=None):
        """Метод создания бургера"""
        burger = Burger()
        burger.set_buns(bun) if bun else None
        burger.add_ingredient(sauce) if sauce else None
        burger.add_ingredient(filling) if filling else None
        return burger

    @staticmethod
    def create_ingredient(ingredient_type, name, price):
        """Метод создания ингредиента"""
        ingredient = Ingredient(ingredient_type, name, price)
        return ingredient

    @staticmethod
    def calculate_burger_price(burger):
        """Метод подсчета стоимости бургера"""
        ingredients_price = 0
        bun_price = burger.bun.get_price()
        ingredients = burger.ingredients
        for ingredient in ingredients:
            ingredients_price += ingredient.get_price()
        return (bun_price * 2) + ingredients_price
