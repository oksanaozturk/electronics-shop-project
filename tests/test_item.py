"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import os


def test__init__(fixture_item):
    """Тест конструктора-инициализатора Класса Item"""

    assert fixture_item.name == "Смартфон"
    assert fixture_item.price == 10000
    assert fixture_item.quantity == 20


def test_calculate_total_price(fixture_item):
    """Тест для метода calculate_total_price"""

    assert fixture_item.calculate_total_price() == 200000


def test_apply_discount(fixture_item):
    """Тест для метода apply_discount"""

    Item.pay_rate = 0.8
    fixture_item.apply_discount()
    assert fixture_item.price == 8000.0


def test_name(fixture_item):
    """
    Тест для Сеттер @property,который делает проверку имени на соответствие заданному параметру длины
    """
    assert fixture_item.name == 'Смартфон'
    fixture_item.name = 'Электроприбор'
    assert fixture_item.name == 'Электропри'


def test_instantiate_from_csv():
    """Тест для Kласс-метода, инициализирующий экземпляры класса `Item` данными из файла src/items.csv"""
    Item.instantiate_from_csv(os.path.join('..', 'src', 'items.csv'))
    assert len(Item.all) == 5
    assert Item.all[1].name == 'Ноутбук'
    assert Item.all[2].price == 10
    assert Item.all[4].quantity == 5


def test_string_to_number():
    """Тест для вспомогательного метода tring_to_number"""

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr(fixture_item):
    """Тест для магического метода __repr__"""
    assert repr(fixture_item) == "Item('Смартфон', 10000, 20)"


def test_str(fixture_item):
    """Тест для магического метода __str__"""
    assert str(fixture_item) == 'Смартфон'


def test_add(fixture_item, fixture_phone):
    """Тест для метода, реализующего сложение экземпляров класса
               (сложение по количеству товара в магазине)
            """
    item2 = Item('Ноутбук',1000,3)
    assert fixture_item + item2 == 23
    assert fixture_item + fixture_phone == 25




