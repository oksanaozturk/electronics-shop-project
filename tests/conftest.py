import pytest
from src.item import Item
from src.phone import Phone
from src.keyboard import Keyboard


@pytest.fixture
def fixture_item():
    """Фикстура для тестовых функций"""

    return Item("Смартфон", 10000, 20)


@pytest.fixture
def fixture_phone():
    """Фикстура для тестовых функций экземпляра класса Phone"""

    return Phone("iPhone 14", 120000, 5, 2)


@pytest.fixture
def fixture_keyboard():
    """Фикстура для тестовых функций экземпляра класса Keyboard"""

    return Keyboard('Dark Project KD87A', 9600, 5)

