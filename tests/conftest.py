import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def fixture_item():
    """Фикстура для тестовых функций"""

    return Item("Смартфон", 10000, 20)


@pytest.fixture
def fixture_phone():
    """Фикстура для тестовых функций экземпляра класса Phone"""

    return Phone("iPhone 14", 120000, 5, 2)
