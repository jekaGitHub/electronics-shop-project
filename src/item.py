import csv
import os


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
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        raise AssertionError
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.isalpha() and len(value) <= 10:
            self.__name = value
        else:
            self.__name = value[:10].strip()

    @classmethod
    def instantiate_from_csv(cls) -> None:
        try:
            cls.all.clear()
            path_file = os.path.join(os.path.dirname(__file__), 'items.csv')
            with open(path_file, encoding='utf-8', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    # if ('name', 'price', 'quantity') not in row:
                    #     raise InstantiateCSVError('Файл item.csv поврежден')
                    name = row['name']
                    price = float(row['price'])
                    quantity = int(row['quantity'])
                    cls(name, price, quantity)
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')
        except (ValueError, KeyError):
            raise InstantiateCSVError('Файл item.csv поврежден')

    @staticmethod
    def string_to_number(str_num):
        return int(float(str_num))

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


class InstantiateCSVError(Exception):
    def __init__(self, message='Файл item.csv поврежден'):
        self.message = message
