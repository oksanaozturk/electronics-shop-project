"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

item1 = Item("Смартфон", 10000, 20)


@pytest.fixture
def fixture_item():
    """Фикстура для тестовых функций"""
    return item1


def test__init__(fixture_item):
    """Тест конструктора-инициализатора Класса Item"""

    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20


def test_calculate_total_price(fixture_item):
    """Тест для метода calculate_total_price"""

    assert item1.calculate_total_price() == 200000


def test_apply_discount(fixture_item):
    """Тест для метода apply_discount"""

    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0
