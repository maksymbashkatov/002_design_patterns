from abc import ABC, abstractmethod

class Car(ABC):
    """
    Стандартный автомобиль со скоростью в километрах.
    """
    @abstractmethod
    def set_speed(self, speed: float):
        pass

    @abstractmethod
    def get_speed(self) -> float:
        pass

class CarMiles(ABC):
    """
    Нестандартный автомобиль со скоростью в милях.
    """
    @abstractmethod
    def set_miles_speed(self, miles_speed: float):
        pass

    @abstractmethod
    def get_miles_speed(self) -> float:
        pass

class CarAdapterSpeed(Car, CarMiles):
    """
    Адаптивный класс наследуемый от стандартного интефейса, который работает с клиентским кодом,
    а также от нестантартного интефеса с которым не работает клиентский код.
    """
    def set_speed(self, speed: float):
        self.set_miles_speed(speed)
        self.__speed = round(self.__miles_speed / 1.60934, 2)

    def get_speed(self) -> float:
        return self.__speed

    def set_miles_speed(self, miles_speed: float):
        self.__miles_speed = miles_speed

    def get_miles_speed(self) -> float:
        return self.__miles_speed

class EuropeCar(Car):
    """
    Класс наследуемый от стандартного интефейса, который работает с клиентским кодом.
    """
    def set_speed(self, speed: float):
        self.__speed = speed

    def get_speed(self):
        return self.__speed

#tests
def print_kilometres_speed(car: Car):
    print(f'Скорость авто {car.get_speed()} км/ч')

car1 = EuropeCar()
car1.set_speed(180)
print_kilometres_speed(car1)

car2 = CarAdapterSpeed()
car2.set_speed(250)
print_kilometres_speed(car2)
print(f'Скорость авто {car2.get_miles_speed()} миль/ч')