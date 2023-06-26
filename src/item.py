import csv
import os

from src.exceptions import InstantiateCSVError


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

        Item.all.append(self)

    def __add__(self, other):
        if issubclass(self.__class__, other.__class__) or issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        return None

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 11:
            self.__name = name
        else:
            raise Exception("Длина наименования товара превышает 10 символов.")

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
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, filename='../src/items.csv'):
        Item.all = []

        if not os.path.exists(filename):
            raise FileNotFoundError('Отсутствует файл item.csv')
        try:
            with open(filename, 'r', encoding='UTF-8') as csvfile:
                reader = csv.DictReader(csvfile)
                if len(reader.fieldnames) != 3:
                    raise InstantiateCSVError('Файл item.csv поврежден')
                [cls((row['name']), float(row['price']), int(row['quantity'])) for row in reader]

        except (InstantiateCSVError, KeyError, TypeError):
            raise InstantiateCSVError('Файл item.csv поврежден')

    @staticmethod
    def string_to_number(string):
        return int(float(string))
