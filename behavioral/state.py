from __future__ import annotations
from abc import ABC, abstractmethod


class Product:
    """
    Класс товара.
    """
    __state: State

    def __init__(self):
        self.__state = OutOfStock()

    def buy(self):
        """
        Попытка купить товар.
        """
        self.__state.buy()

    def to_order(self):
        """
        Заказать товар.
        """
        self.__state.to_order()
        self.__state = IsOrdered()

    def changeState(self, state):
        self.__state = state


class State(ABC):
    @abstractmethod
    def buy(self):
        pass

    @abstractmethod
    def to_order(self):
        pass


class InStock(State):
    """
    Товар есть в наличии.
    """
    def buy(self):
        print('Покупаем товар.')

    def to_order(self):
        print('Товар есть в наличии, поэтому его не нужно заказывать у поставщика.')


class OutOfStock(State):
    """
    Товара нет в наличии.
    """
    def buy(self):
        print('Нельзя купить товар, так как его нет в наличии. Нужно заказать у поставщика.')

    def to_order(self):
        print('Заказываем товар у поставщика.')


class IsOrdered(State):
    """
    Товар заказан у поставщика.
    """
    def buy(self):
        print('Пока нельзя купить товар, так как его нет в наличии. Но он уже заказан у поставщика.')

    def to_order(self):
        print('Товар уже заказан у поставщика.')


# tests
product1 = Product()
product1.buy()
product1.to_order()
product1.buy()
product1.changeState(InStock())
product1.buy()
