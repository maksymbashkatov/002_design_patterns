from __future__ import annotations
from abc import ABC, abstractmethod


class RestaurantEmployee(ABC):
    @abstractmethod
    def accept(self, client: Client):
        """
        Метод для вызова нужного метода обслуживания посетителя.
        """
        pass


class Cook(RestaurantEmployee):
    def accept(self, client: Client):
        client.get_food(self)

    def give_food(self):
        print('Повар готовит еду.')


class Barman(RestaurantEmployee):
    def accept(self, client: Client):
        client.get_drink(self)

    def give_drink(self):
        print('Бармен наливает напиток.')


class Client(ABC):
    @abstractmethod
    def get_food(self, cook: Cook):
        cook.give_food()

    @abstractmethod
    def get_drink(self, barman: Barman):
        barman.give_drink()


class Sportsman(Client):
    def get_food(self, cook: Cook):
        cook.give_food()
        print('Спортсмен получает здоровую нежирную еду.\n')

    def get_drink(self, barman: Barman):
        barman.give_drink()
        print('Спортсмен получает свежевыжатый сок.\n')


class NonSportsman(Client):
    def get_food(self, cook: Cook):
        cook.give_food()
        print('Неспортсмен получает вкусную но вредную жирную еду.\n')

    def get_drink(self, barman: Barman):
        barman.give_drink()
        print('Неспортсмен получает разливное пиво.\n')


# tests
visitor1 = Sportsman()
visitor2 = NonSportsman()
cook = Cook()
barman = Barman()

cook.accept(visitor1)
cook.accept(visitor2)

barman.accept(visitor1)
barman.accept(visitor2)
