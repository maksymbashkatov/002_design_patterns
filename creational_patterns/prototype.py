from __future__ import annotations
from abc import ABC, abstractmethod

class Animal(ABC):
    __weight: int
    __max_age: int

    def __init__(self, source: Animal):
        self.__weight = source.__weight
        self.__max_age = source.__max_age

    @abstractmethod
    def clone(self) -> Animal:
        pass

class Human(Animal):
    __name: str
    __id_number: int

    def __init__(self, source: Human):
        super().__init__(source)
        self.__name = source.__name
        self.__id_number = source.__id_number

    def clone(self) -> Animal:
        return Human(self)

class Cat(Animal):
    __is_wool: bool

    def __init__(self, source: Cat):
        super().__init__(source)
        self.__is_wool = source.__is_wool

# tests
animals: list

# human1 = Human()