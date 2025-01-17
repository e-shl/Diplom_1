import pytest
from unittest.mock import Mock

from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.burger import Burger, Bun
from praktikum.database import Database


class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        bun = Bun('Просто булка', 9.99)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = 'Куриная котлета'
        mock_ingredient.get_price.return_value = 9.99
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0].get_price() == 9.99
        assert burger.ingredients[0].get_name() == 'Куриная котлета'
        assert burger.ingredients[0].get_type() == INGREDIENT_TYPE_FILLING

    def test_remove_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    # Не знаю насколько независимые следующие тесты, но использовать данные из существующего Database проще чем создавать Mock

    def test_move_ingredient(self):
        burger = Burger()
        database = Database()
        burger.add_ingredient(database.available_ingredients()[0])
        burger.add_ingredient(database.available_ingredients()[1])
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == database.available_ingredients()[1]
        assert burger.ingredients[1] == database.available_ingredients()[0]

    def test_get_price(self):
        burger = Burger()
        database = Database()
        burger.set_buns(database.available_buns()[0])
        burger.add_ingredient(database.available_ingredients()[0])
        burger.add_ingredient(database.available_ingredients()[1])
        assert burger.get_price() == 500.0

    def test_get_receipt(self):
        burger = Burger()
        database = Database()
        burger.set_buns(database.available_buns()[0])
        burger.add_ingredient(database.available_ingredients()[0])
        burger.add_ingredient(database.available_ingredients()[3])
        # Каждый ингридиент добавляет новую строку при разделении через '\n'.join(receipt)
        test_receipt = "(==== black bun ====)\n" \
                           "= sauce hot sauce =\n" \
                           "= filling cutlet =\n" \
                           "(==== black bun ====)\n\n" \
                           "Price: 400"
        assert burger.get_receipt() == test_receipt
