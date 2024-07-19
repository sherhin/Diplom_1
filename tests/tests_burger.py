import pytest
from conftest import create_bun
from conftest import create_burger
from conftest import create_ingredient


class TestBurger:

    def test_burger_set_bun(self):
        bun = create_bun('red bun', 300)
        burger = create_burger()
        burger.set_buns(bun)
        assert burger.bun == bun


    def test_burger_add_ingredient(self):
        ingredient = create_ingredient('sauce', 'sour cream', 200)
        burger = create_burger()
        burger.add_ingredient(ingredient)
        print(burger.ingredients, ingredient)
        assert burger.ingredients == [ingredient]


    def test_burger_move_ingredients(self):
        first_ingredient = create_ingredient('sauce', 'sour cream', 200)
        second_ingredient = create_ingredient('filling', 'cutlet', 100)
        burger = create_burger()
        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(second_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [second_ingredient, first_ingredient]

    # def test_burger_move_ingredients(self):
    #     first_ingredient = create_ingredient('sauce', 'sour cream', 200)
    #     second_ingredient = create_ingredient('filling', 'cutlet', 100)
    #     burger = create_burger()
    #     burger.add_ingredient(first_ingredient)
    #     burger.add_ingredient(second_ingredient)
    #     burger.move_ingredient(0, 1)
    #     assert burger.ingredients == [second_ingredient, first_ingredient]





