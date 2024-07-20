import pytest

from helpers import Helpers as help


class TestBun:

    @pytest.mark.parametrize('buns_name, buns_price', help.get_available_buns().items())
    def test_bun_get_name(self, buns_name, buns_price):
        bun = help.create_bun(buns_name, buns_price)
        assert bun.get_name() == buns_name

    @pytest.mark.parametrize('buns_name, buns_price', help.get_available_buns().items())
    def test_bun_get_price(self, buns_name, buns_price):
        bun = help.create_bun(buns_name, buns_price)
        assert bun.get_price() == buns_price
