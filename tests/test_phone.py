import pytest
from src.phone import Phone


def test__init__(fixture_phone):
    """Тест конструктора-инициализатора Класса Item"""

    assert fixture_phone.name == "iPhone 14"
    assert fixture_phone.price == 120000
    assert fixture_phone.quantity == 5
    assert fixture_phone.number_of_sim == 2


def test_repr(fixture_phone):
    """Тест для магического метода __repr__"""
    assert repr(fixture_phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim(fixture_phone):
    """Тест для метода сеттер number_of_sim, для проверки входящего значения количества карт"""
    fixture_phone.number_of_sim = 1
    assert fixture_phone.number_of_sim == 1

    with pytest.raises(ValueError):
        fixture_phone.number_of_sim = 0
        assert str(fixture_phone.number_of_sim) == "Количество физических SIM-карт должно быть целым числом больше нуля"


def test_add(fixture_phone):
    """Тест для метода, реализующего сложение экземпляров класса
               (сложение по количеству товара в магазине)
            """
    phone2 = Phone("iPhone 13", 110000, 10, 2)
    assert fixture_phone + phone2 == 15
