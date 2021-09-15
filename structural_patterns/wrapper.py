class Payment:
    def pay(self):
        print('Оплачиваем товар.')


class BaseWrapper(Payment):
    __wrappee: Payment

    def __init__(self, payment: Payment):
        self.__wrappee = payment

    def pay(self):
        pass


class MobileWrapper(BaseWrapper):
    __mobile_number: str

    def __init__(self, payment: Payment, mobile_number):
        super().__init__(payment)
        self.__mobile_number = mobile_number

    def pay(self):
        print(f'Оплачиваем товар мобильным счётом {self.__mobile_number}.')


class BankCardWrapper(BaseWrapper):
    __bank_card_number: str

    def __init__(self, payment: Payment, bank_card_number):
        super().__init__(payment)
        self.__bank_card_number = bank_card_number

    def pay(self):
        print(f'Оплачиваем товар банковской картой {self.__bank_card_number}.')


# tests
pay1 = Payment()
pay1.pay()

pay2 = MobileWrapper(pay1, '0957779999')
pay2.pay()

pay3 = BankCardWrapper(pay2, '0000111100001111')
pay3.pay()
