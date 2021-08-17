from abc import ABC, abstractmethod


class Drink:
    """
    Класс напитка который делает бармен.
    """
    def __init__(self):
        self.__list_of_ingredients: list[str] = []

    def add_ingredient(self, ingredient: str):
        print(f"Добавлен ингредиент: {ingredient}")
        self.__list_of_ingredients.append(ingredient)

    def __str__(self):
        return f"Ингридиенты напитка: {self.__list_of_ingredients}"

class DrinkMaker(ABC):
    """
    Класс выступающий шаблоном, для остальных классов создателей уже конкретных напитков.
    """
    def make_drink(self, drink: Drink):
        self.prepare_base(drink)
        self.prepare_filling(drink)

    @abstractmethod
    def prepare_base(self, drink: Drink):
        """
        Приготовить основу напитка.
        """
        pass

    @abstractmethod
    def prepare_filling(self, drink: Drink):
        """
        Приготовить наполнение напитка.
        """
        pass

class TeaMaker(DrinkMaker):
    def prepare_base(self, drink: Drink):
        drink.add_ingredient('hot water')
        drink.add_ingredient('tea leaves')

    def prepare_filling(self, drink: Drink):
        drink.add_ingredient('sugar')
        drink.add_ingredient('lemon slice')

class CoffeeMaker(DrinkMaker):
    def prepare_base(self, drink: Drink):
        drink.add_ingredient('hot water')
        drink.add_ingredient('coffee beans')

    def prepare_filling(self, drink: Drink):
        drink.add_ingredient('sugar')
        drink.add_ingredient('milk')

class Barman:
    def __init__(self, drink_maker: DrinkMaker):
        self.__drink_maker = drink_maker

    def set_drink_maker(self, drink_maker: DrinkMaker):
        self.__drink_maker = drink_maker

    def make_drink(self) -> Drink:
        drink = Drink()
        self.__drink_maker.make_drink(drink)
        return drink

barman = Barman(TeaMaker())
drink1 = barman.make_drink()
print(drink1)

print('---*---')

barman.set_drink_maker(CoffeeMaker())
drink2 = barman.make_drink()
print(drink2)