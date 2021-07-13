from abc import ABC, abstractmethod
from enum import Enum

class Engine(Enum):
    ELECTRIC = 'ELECTRIC' # Электро двигатель.
    PETROL = 'PETROL' # Бензиновый двигатель.

class Transmission(Enum):
    AUTOMATIC = 'AUTOMATIC'
    MECHANICAL = 'MECHANICAL'

class Tires(Enum):
    WINTER = 'WINTER'
    BIG_WINTER = 'BIG_WINTER'
    SUMMER = 'SUMMER'

class Glass(Enum):
    HEAVILY_TONED = 'HEAVILY_TONED' # Сильно тонированный.
    MEDIUM_TONED = 'TONED'
    CLEAR = 'CLEAR'

class Car():
    def __init__(self, name: str):
        self.name = name
        self.engine = None
        self.transmission = None
        self.tires = None
        self.glass = None

    def __str__(self):
        return f"""        Название автомобиля: {self.name}
        Тип двигателя: {self.engine}
        Тип коробки передач: {self.transmission}
        Сезонность шин: {self.tires}
        Тонированность стекла: {self.glass}
        """

class CarBuilder(ABC):
    """
    Абстрактный базовый класс сторителя.
    Задаёт общий интерфейс для строителей наследников.
    """

    car: Car

    @abstractmethod
    def set_engine(self):
        pass

    @abstractmethod
    def set_transmission(self):
        pass

    @abstractmethod
    def set_tires(self):
        pass

    @abstractmethod
    def set_glass(self):
        pass

    def get_car(self) -> Car:
        return self.car


class BigWinterSUVCarBuilder(CarBuilder):
    """
    SUV - внедорожник
    """
    def __init__(self):
        self.car = Car('BigWinterSUV')

    def set_engine(self):
        self.car.engine = Engine.PETROL

    def set_transmission(self):
        self.car.transmission = Transmission.MECHANICAL

    def set_tires(self):
        self.car.tires = Tires.BIG_WINTER

    def set_glass(self):
        self.car.glass = Glass.HEAVILY_TONED

class TeslaCarBuilder(CarBuilder):
    """
    Класс электромобиля.
    """
    def __init__(self):
        self.car = Car('Tesla')

    def set_engine(self):
        self.car.engine = Engine.ELECTRIC

    def set_transmission(self):
        self.car.transmission = Transmission.AUTOMATIC

    def set_tires(self):
        self.car.tires = Tires.SUMMER

    def set_glass(self):
        self.car.glass = Glass.MEDIUM_TONED

class Director:
    """
    Отвечает за поэтапную комплетацию автомобиля.
    """
    __builder: CarBuilder

    def set_builder(self, car_builder: CarBuilder):
        """
        Принимает экземпляр нужного строителя.
        """
        self.__builder = car_builder

    def create_car(self):
        self.__builder.set_engine()
        self.__builder.set_transmission()
        self.__builder.set_tires()
        self.__builder.set_glass()

# tests
director = Director()
for car_builder in (BigWinterSUVCarBuilder(), TeslaCarBuilder()):
    director.set_builder(car_builder)
    director.create_car()
    car = car_builder.get_car()
    print(car)