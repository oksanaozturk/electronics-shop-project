import pytest


def test__init__(fixture_keyboard):
    """Тест конструктора-инициализатора Класса Keyboard"""

    assert fixture_keyboard.name == "Dark Project KD87A"
    assert fixture_keyboard.price == 9600
    assert fixture_keyboard.quantity == 5
    assert fixture_keyboard.language == "EN"


def test__str__(fixture_keyboard):
    """Тест для магического метода __str__"""

    assert str(fixture_keyboard.language) == "EN"


def test_change_lang(fixture_keyboard):
    """Тест для проверки метода пор смене языка"""
    fixture_keyboard.change_lang()
    assert str(fixture_keyboard.language) == "RU"

    fixture_keyboard.change_lang()
    assert str(fixture_keyboard.language) == "EN"


def test_language(fixture_keyboard):
    """Тест для проверки работы геттера при отсутвии сеттера(нельза сменить язык на другой, приватный аргумент)"""
    with pytest.raises(AttributeError):
        fixture_keyboard.language = 'CH'
