import csv
import os
csv_file = os.path.join('..', 'src', 'items.csv')


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """
        Сеттер @property делает проверку имени на соответствие заданному параметру длины
        :param name: Название товара.
        """

        if len(name) < 10:
            self.__name = name
        else:
            self.__name = name[:10]

    def __repr__(self):
        """ Магический метод __repr__, выводит информацию для программистов"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Магический метод __str__, выводит информацию для пользователей"""
        return f"{self.name}"

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls, csv_file) -> None:
        """
        Kласс-метод, инициализирующий экземпляры класса `Item` данными из файла src/items.csv

        Перед созданием классов по данным из файла, строка all очищается через компнду clear()

        :param csv_file from src/items.csv
        """
        Item.all.clear()
        try:
            with open(csv_file, newline='', encoding='windows-1251') as csvfile:
                reader = list(csv.DictReader(csvfile))
                for row in reader:
                    name = row['name']
                    price = int(row['price'])
                    quantity = int(row['quantity'])
                    cls(name, price, quantity)

        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")

        except (KeyError, ValueError, TypeError):
            raise InstantiateCSVError("Файл item.csv поврежден")

    @staticmethod
    def string_to_number(num_string: str) -> int:
        """
        Cтатический метод, возвращающий число из числа-строки
        :param num_string: str (Ex: '5', '5.5', '5.0')
        """
        return int(float(num_string))

    def __add__(self, other) -> int:
        """Метод, реализующий сложение экземпляров класса
           (сложение по количеству товара в магазине)
        """
        if not isinstance(other, self.__class__):
            raise ValueError("нельзя сложить `Phone` или `Item` с экземплярами не `Phone` или `Item` классов")
        else:
            return self.quantity + other.quantity


class InstantiateCSVError(Exception):
    """
    Класс-исключение для обработки исключений при повреждении файла `items.csv`,
    при котором будет прописываться ошибка “_Файл item.csv поврежден_”

    """
    pass
    # Первый вариант инициализации
    # def __init__(self, message='Файл item.csv поврежден'):
    #     super().__init__()
    #     self.message = message
    # def __init__(self, *args):
    #     self.message = args[0] if args else 'Файл item.csv поврежден'
    #
    # Второй вариант инициализации
    # def __str__(self):
    #     return f'{self.message}'
