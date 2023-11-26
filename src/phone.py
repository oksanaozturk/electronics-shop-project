from src.item import Item


class Phone(Item):
    """
       Класс для представления товара (телефонов) в магазине.
       """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """Инициализация экземпляров класса

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Количество сим-карт
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        """Создание метода геттер для number_of_sim"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, num_sim):
        """Создание метода сеттер для number_of_sim, для проверки входящего значения количества карт"""
        if not isinstance(num_sim, int) or num_sim <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")
        self.__number_of_sim = num_sim

    def __repr__(self):
        """ Магический метод __repr__, выводит информацию для программистов"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
