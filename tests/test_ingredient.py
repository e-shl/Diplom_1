import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    def test_get_price(self):
        test_price = 20
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE,'Экспериментальный соус', test_price)
        assert ingredient.get_price() == test_price

    def test_get_name(self):
        test_name = 'Куриная котлета'
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, test_name, 0)
        assert ingredient.get_name() == test_name

    @pytest.mark.parametrize(
        'type, name, price, test_type',
        [
            [INGREDIENT_TYPE_SAUCE, 'Экспериментальный соус', 20, 'SAUCE'],
            [INGREDIENT_TYPE_FILLING, 'Куриная котлета', 9.99, 'FILLING']
        ]
    )
    def test_get_type(self, type, name, price, test_type):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == test_type