import pytest

from praktikum.database import Database


class TestDatabase:

    def test_get_available_buns(self):
        database = Database()
        assert len(database.available_buns()) == 3

    def test_get_available_ingredients(self):
        database = Database()
        assert len(database.available_ingredients()) == 6