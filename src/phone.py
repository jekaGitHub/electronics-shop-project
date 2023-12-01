from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if not isinstance(self, self.__class__) or not isinstance(other, other.__class__):
            raise TypeError("Экземпляры не принадлежат классам Item и Phone")
        return self.quantity + other.quantity

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        """
        Сеттер для проверки number_of_sim на целое число больше нуля.
        """
        if not isinstance(number_of_sim, int) or number_of_sim <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        self.__number_of_sim = number_of_sim
