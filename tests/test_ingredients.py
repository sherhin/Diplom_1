import pytest

from helpers import Helpers as help

class TestIngredients:

    @pytest.mark.parametrize(
        'ingredient_type, ingredient_name, ingredient_price', [
            ('sauce', 'sour cream', 200), ('filling', 'cautlet', 100)
        ]
    )
    def test_ingredient_get_type(self, ingredient_type, ingredient_name, ingredient_price):
        ingredient = help.create_ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert ingredient.get_type() == ingredient_type

    def test_ingredient_get_price(self):
        price = 200
        ingredient = help.create_ingredient('sauce', 'sour cream', price)
        assert ingredient.get_price() == price

    def test_ingredient_get_name(self):
        name = 'sour cream'
        ingredient = help.create_ingredient('sauce', name, 200)
        assert ingredient.get_name() == name
