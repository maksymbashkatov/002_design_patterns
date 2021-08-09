from __future__ import annotations

import copy
from abc import ABC, abstractmethod

class Smartphone(ABC):
    """
    Прототип смартфона.
    """
    def __init__(self, name: str, screen_size: float, built_in_memory: int, ram: int):
        self._name = name
        self._screen_size = screen_size
        self._built_in_memory = built_in_memory
        self._ram = ram

    def __str__(self):
        return f'name = {self._name}\n' \
               f'screen_size = {self._screen_size}\n' \
               f'built_in_memory = {self._built_in_memory}\n' \
               f'ram = {self._ram}\n'

    @abstractmethod
    def clone(self):
        """
        Копирует экземпляр класса со всеми его значениями.
        """
        pass

    @abstractmethod
    def change_parameters(self,
                          name=None,
                          screen_size=None,
                          built_in_memory=None,
                          ram=None):
        """
        Изменяет параметры класса.
        """
        if name != None:
            self._name = name

        if screen_size != None:
            self._screen_size = screen_size

        if built_in_memory != None:
            self._built_in_memory = built_in_memory

        if ram != None:
            self._ram = ram

class CheapLineSmartphone(Smartphone):
    def __init__(self, name: str, screen_size: float, built_in_memory: int, ram: int, button_smartphone: bool):
        super().__init__(name, screen_size, built_in_memory, ram)
        self.__button_smartphone = button_smartphone

    def __str__(self):
        return super(CheapLineSmartphone, self).__str__() + f'button_smartphone = {self.__button_smartphone}\n'

    def clone(self):
        return copy.deepcopy(self)

    def change_parameters(self,
                          name=None,
                          screen_size=None,
                          built_in_memory=None,
                          ram=None,
                          button_smartphone=None):
        super(CheapLineSmartphone, self).change_parameters(name, screen_size, built_in_memory, ram)
        if built_in_memory != None:
            self.__button_smartphone = button_smartphone

class ExpensiveLineSmartphone(Smartphone):
    def __init__(self, name: str, screen_size: float, built_in_memory: int, ram: int, nfc: bool, fingerprint_on_screen: bool):
        super().__init__(name, screen_size, built_in_memory, ram)
        self.__nfc = nfc
        self.__fingerprint_on_screen = fingerprint_on_screen

    def __str__(self):
        return super(ExpensiveLineSmartphone, self).__str__() + \
               f'nfc = {self.__nfc}\n' \
               f'fingerprint_on_screen = {self.__fingerprint_on_screen}\n'

    def clone(self):
        # return self
        return copy.deepcopy(self)

    def change_parameters(self,
                          name=None,
                          screen_size=None,
                          built_in_memory=None,
                          ram=None,
                          nfc=None,
                          fingerprint_on_screen=None):
        super(ExpensiveLineSmartphone, self).change_parameters(name, screen_size, built_in_memory, ram)
        if nfc != None:
            self.__nfc = nfc

        if fingerprint_on_screen != None:
            self.__fingerprint_on_screen = fingerprint_on_screen

# tests
# Список для смартфонов
smartphone_list = []

# Создаётся экземпляр класса дешёвого смартфона, помещается в список.
cheap_smartphone1 = CheapLineSmartphone('cheap_smartphone1', 3.5, 16, 2, False)
smartphone_list.append(cheap_smartphone1)

# Клонируется экземпляр класса дешёвого смартфона
# тем самым создаётся новый экземпляр - его точная копия.
cheap_smartphone2 = cheap_smartphone1.clone()

# Изменяются значения параметров клона, помещается в список.
cheap_smartphone2.change_parameters(built_in_memory=8, button_smartphone=True)
# cheap_smartphone2.built_in_memory = 8
# cheap_smartphone2.button_smartphone = True
smartphone_list.append(cheap_smartphone2)

# Создаётся экземпляр класса дорогого смартфона, помещается в список.
expensive_smartphone1 = ExpensiveLineSmartphone('expensive_smartphone1', 4.7, 64, 4, False, False)
smartphone_list.append(expensive_smartphone1)

# Клонируется экземпляр класса дорогого смартфона
# тем самым создаётся новый экземпляр - его точная копия.
expensive_smartphone2 = expensive_smartphone1.clone()
# Изменяются значения параметров клона, помещается в список.
expensive_smartphone2.change_parameters(nfc=True, fingerprint_on_screen=True)
smartphone_list.append(expensive_smartphone2)

for smartphone in smartphone_list:
    print(smartphone)

print(expensive_smartphone1 is expensive_smartphone2)