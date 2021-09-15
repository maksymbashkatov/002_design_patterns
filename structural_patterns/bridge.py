from __future__ import annotations
from abc import ABC, abstractmethod


class Car(ABC):
    __engine: Engine
    _max_power: int = 0

    def __init__(self, engine):
        self.__engine = engine

    def power_up(self, up):
        self.__engine.power += up

    def power_down(self, down):
        self.__engine.power -= down

    def info(self):
        print(f'Его мощность: {self.__engine.power}.\n')

class ElectroCar(Car):
    def info(self):
        print('Это электрокар.')
        super().info()

class PetrolCar(Car):
    def info(self):
        print('Это обычный автомобиль.')
        super().info()

class Engine:
    __power: int = 0

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, new_power):
        if new_power >= 0:
            self.__power = new_power
        else:
            print('Мощность не может быть меньше нуля.')


class ElectroEngine(Engine):
    pass

class PetrolEngine(Engine):
    pass


# tests
car1 = ElectroCar(ElectroEngine())
car1.info()
car1.power_up(100)
car1.info()

car2 = PetrolCar(PetrolEngine())
car2.power_up(50)
car2.info()
car2.power_down(10)
car2.info()
