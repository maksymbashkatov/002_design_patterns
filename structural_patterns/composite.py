from __future__ import annotations
from abc import ABC, abstractmethod


class Ingredient(ABC):
    """
    Интерфейс ингрредиента кебаба, как составного так и обычного.
    """
    _name: str
    _cost: int = 0

    def get_name(self):
        return self._name

    @abstractmethod
    def get_cost(self):
        pass


class SimpleIngredient(Ingredient):
    def __init__(self, name, cost):
        self._name = name
        self._cost = cost

    def get_cost(self):
        return self._cost


class CompositeIngredient(Ingredient):
    __ingredients: list[Ingredient]

    def __init__(self, name):
        self.__ingredients = []
        self._name = name

    def get_cost(self):
        sum_cost = 0
        for ingredient in self.__ingredients:
            sum_cost += ingredient.get_cost()
        self._cost = sum_cost
        return self._cost

    def add(self, *ingredients):
        for ingredient in ingredients:
            self.__ingredients.append(ingredient)

    def remove(self, ingredient_name):
        for ingredient in self.__ingredients:
            if ingredient.get_name() == ingredient_name:
                self.__ingredients.remove(ingredient)

    def print_ingredients(self):
        print(f'{self.get_name()} состоит из: ')
        for i in self.__ingredients:
            print(f'\t - {i.get_name()}')


# tests
sauce = CompositeIngredient('соус')
sauce.add(SimpleIngredient('майонез', 2), SimpleIngredient('кетчуп', 1), SimpleIngredient('чеснок', 1))

kebab = CompositeIngredient('кебаб')
kebab.add(SimpleIngredient('мясо', 5), SimpleIngredient('лаваш', 3), sauce, SimpleIngredient('сахар', 2))
print(f'{kebab.get_name()} стоит {kebab.get_cost()}$.')
kebab.remove('сахар')
print(f'{kebab.get_name()} стоит {kebab.get_cost()}$.')
kebab.print_ingredients()
