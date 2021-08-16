from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def next(self) -> list:
        pass

    @abstractmethod
    def has_next(self) -> bool:
        pass

class IterableCollection(ABC):
    @abstractmethod
    def create_iterator(self) -> Iterator:
        pass

class Roulette(IterableCollection):
    def __init__(self):
        print('Which parity of number do you choose?')
        self.player_choice = input('Enter even or odd to pick: ')
        if self.player_choice == 'even':
            self.__roulette_numbers = [number for number in range(2, 37) if number % 2 == 0]
        else:
            self.__roulette_numbers = [number for number in range(1, 36) if number % 2 != 0]

    def create_iterator(self) -> Iterator:
        return RouletteNumberIterator(self.__roulette_numbers)

class RouletteNumberIterator(Iterator):
    def __init__(self, roulette_numbers: list):
        self.__roulette_numbers = roulette_numbers
        self.__index = 0

    def next(self):
        number = self.__roulette_numbers[self.__index]
        self.__index += 1
        return number

    def has_next(self) -> bool:
        return False if self.__index >= len(self.__roulette_numbers) else True

# tests
roulette1 = Roulette()
roulette_iterator1 = roulette1.create_iterator()
while roulette_iterator1.has_next():
    print(roulette_iterator1.next())

print('---')
roulette2 = Roulette()
roulette_iterator2 = roulette2.create_iterator()
print(roulette_iterator2.next())
print(roulette_iterator2.next())