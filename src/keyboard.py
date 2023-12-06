from src.item import Item


class MixinChange:
    """
    Вспомогательный Mixin Класс для  хранению и изменению раскладки клавиатуры
    Для Класса предусмотрено 2 варианта раскладки клавиатуры:
    language_1 = 'EN'
    language_2 = 'RU'
    """

    language_1 = 'EN'
    language_2 = 'RU'

    def __init__(self) -> None:
        """Инициализация атрибутов класса"""
        self.__language = self.language_1

    @property
    def language(self) -> str:
        """Созданием приватности для атрибута language"""
        return self.__language

    def __str__(self) -> str:
        """Магический метод __str__ дл яэкземпляров Класса"""
        return self.__language

    def change_lang(self) -> str:
        """Метод для изменения языка клавиатуры"""
        if self.__language == self.language_1:
            self.__language = self.language_2
            return self.language

        elif self.language == self.language_2:
            self.__language = self.language_1
            return self.language


class Keyboard(Item, MixinChange):
    """Класс для товара “клавиатура”"""

    pass

    # def __init__(self, name: str, price: float, quantity: int) -> None:
    #     """Инициализация экземпляров класса
    #
    #        :param name: Название товара.
    #        :param price: Цена за единицу товара.
    #        :param quantity: Количество товара в магазине.
    #     """
    #     super().__init__(name, price, quantity)
