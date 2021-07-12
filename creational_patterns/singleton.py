class SingletonBase(type):
    """
    Базовый метакласс.
    """
    _instances = {} # словарь для хранения единственного экземпляра класса

    def __call__(cls, *args, **kwargs):
        """
        Если экземпляр класса существует, то он возвращается,
        если нет, то создаётся и помещается в словарь.
        :return: экземпляр класса
        """
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Moneybox(metaclass=SingletonBase):
    """
    Класс наследник от метакласса. Представляет копилку.
    """
    def __init__(self):
        self.__amount_of_money = 0 # Количество денег.

    def put_money(self, money: float):
        """
        Положить деньги в копилку.
        """
        self.__amount_of_money += money

    def take_money(self, money: float):
        """
        Взять деньги с копилки, если они там есть.
        """
        if self.__amount_of_money < money:
            raise Exception('Столько денег нет в копилке, возьми меньше, имей совесть...')
        else:
            self.__amount_of_money -= money

    def get__amount_of_money(self):
        print(self.__amount_of_money)

# tests
# Создаю 2 переменных для хранения ссылки на экземпляры класса Moneybox
moneybox1 = Moneybox() # Создаю экземпляр класса Moneybox
moneybox2 = Moneybox() # Попытка создать ещё один экземпляр класса Moneybox

# Манипуляции доказывающие, что переменные хранят ссылку на один и тот же экземпляр класса
moneybox1.put_money(100)
moneybox1.get__amount_of_money()
moneybox2.get__amount_of_money()
moneybox2.take_money(50)
moneybox1.get__amount_of_money()
moneybox2.get__amount_of_money()

# Доказательство, что переменные хранят ссылку на один объект
print(moneybox1)
print(moneybox2)

# Доказательство, что переменные хранят ссылку на один объект путём показывания уникального идентификатора объекта
print(id(moneybox1))
print(id(moneybox2))