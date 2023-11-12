"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item

item1 = Item("Смартфон", 10000, 20)

# TestCase#1 конструктора-инициализатора Класса Item
assert item1.name == "Смартфон"
assert item1.price == 10000
assert item1.quantity == 20

# TestCase#2 для метода calculate_total_price
assert item1.calculate_total_price() == 200000

# TestCase#3 для метода apply_discount
Item.pay_rate = 0.8
item1.apply_discount()
assert item1.price == 8000.0
