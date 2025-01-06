import pytest

from praktikum.bun import Bun


class TestBun:

    def test_get_name(self):
        test_name = 'Просто булка'
        bun = Bun(test_name, 0)
        assert bun.get_name() == test_name

    def test_get_price(self):
        test_price = 9.99
        bun = Bun('Просто булка', test_price)
        assert bun.get_price() == test_price
