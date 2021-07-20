class MetaSingleton(type):
    """
    Метакласс, который определить действия при создании экземпляров для своих наследников.
    """
    __instance = None

    def __call__(cls):
        """
        Если экземпляр класса существует, то возвращаем его, иначе создаём его.
        :return: экземпляр класса
        """
        if cls.__instance is None:
            cls.__instance = super(MetaSingleton, cls).__call__()
        return cls.__instance

class Moneybox(metaclass=MetaSingleton):
    """
    Класс который делегирует поведение создание экземпляров метаклассу.
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
# Создаётся 2 переменных для хранения ссылки на экземпляры класса Moneybox.
moneybox1 = Moneybox() # Создан экземпляр класса Moneybox.
moneybox2 = Moneybox() # Попытка создать ещё один экземпляр класса Moneybox.

# Манипуляции доказывающие, что переменные хранят ссылку на один и тот же экземпляр класса.
moneybox1.put_money(100)
moneybox1.get__amount_of_money()
moneybox2.get__amount_of_money()
moneybox2.take_money(50.45)
moneybox1.get__amount_of_money()
moneybox2.get__amount_of_money()

# Доказательство, что переменные хранят ссылку на один объект.
print(moneybox1)
print(moneybox2)

# Доказательство, что переменные хранят ссылку на один объект путём показывания уникального идентификатора объекта.
print(id(moneybox1))
print(id(moneybox2))