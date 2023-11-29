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
    fixture_keyboard.change_lang()
    assert str(fixture_keyboard.language) == "RU"

    fixture_keyboard.change_lang()
    assert str(fixture_keyboard.language) == "EN"
