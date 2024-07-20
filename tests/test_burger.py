import pytest

from helpers import Helpers as help


class TestBurger:

    def test_burger_set_bun(self):
        bun = help.create_bun('red bun', 300)
        burger = help.create_burger()
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_burger_add_ingredient(self):
        ingredient = help.create_ingredient('sauce', 'sour cream', 200)
        burger = help.create_burger()
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [ingredient]

    def test_burger_move_ingredients(self):
        first_ingredient = help.create_ingredient('sauce', 'sour cream', 200)
        second_ingredient = help.create_ingredient('filling', 'cutlet', 100)
        burger = help.create_burger()
        burger.add_ingredient(first_ingredient)
        burger.add_ingredient(second_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [second_ingredient, first_ingredient]

    def test_burger_remove_ingredient(self):
        first_ingredient = help.create_ingredient('sauce', 'sour cream', 200)
        second_ingredient = help.create_ingredient('filling', 'cutlet', 100)
        burger = help.create_burger(sauce=first_ingredient, filling=second_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == [second_ingredient]

    @pytest.mark.parametrize(
        'bun_name, bun_price, sauce_name,sauce_price, fill_name, fill_price',
                             [
                                 ('red bun', 300, 'sour cream', 200, 'cutlet', 100),
                                 ('black bun', 100, 'hot sauce', 100, 'dinosaur', 200)
                             ]
    )
    def test_burger_get_price(
            self, bun_name, bun_price, sauce_name, sauce_price,
            fill_name, fill_price
    ):
        bun = help.create_bun(bun_name, bun_price)
        sauce = help.create_ingredient('sauce', sauce_name, sauce_price)
        filling = help.create_ingredient('filling', fill_name, fill_price)
        burger = help.create_burger(bun, sauce, filling)
        total = help.calculate_burger_price(burger)
        burger_price = burger.get_price()
        assert total == burger_price

    @pytest.mark.parametrize(
        'bun_name, bun_price, sauce_name,sauce_price, fill_name, fill_price',
        [
            ('red bun', 300, 'sour cream', 200, 'cutlet', 100),
            ('black bun', 100, 'hot sauce', 100, 'dinosaur', 200)
        ]
    )
    def test_burger_get_receipt(
            self, bun_name, bun_price, sauce_name, sauce_price,
            fill_name, fill_price
    ):
        bun = help.create_bun(bun_name, bun_price)
        sauce = help.create_ingredient('sauce', sauce_name, sauce_price)
        filling = help.create_ingredient('filling', fill_name, fill_price)
        burger = help.create_burger(bun, sauce, filling)
        receipt = burger.get_receipt()
        all_burger = [bun_name, sauce_name, fill_name, str(burger.get_price())]
        for elem in all_burger:
            assert receipt.find(elem)

