from __future__ import annotations
from abc import ABC, abstractmethod

class SendPhoto:
    def __init__(self, connect_strategy: MessangerStrategy):
        self.__connect_strategy = connect_strategy

    def get_strategy(self) -> MessangerStrategy:
        return self.__connect_strategy

    def send(self):
        print(f'Send photo by {self.__connect_strategy.get_name()}.')

class MessangerStrategy(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

class Telegram(MessangerStrategy):
    def get_name(self):
        return 'Telegram'

class Viber(MessangerStrategy):
    def get_name(self):
        return 'Viber'

class WhatsApp(MessangerStrategy):
    def get_name(self):
        return 'WhatsApp'

# tests
send_photo1 = SendPhoto(Viber())
send_photo1.send()

send_photo2 = SendPhoto(Telegram())
send_photo2.send()

send_photo3 = SendPhoto(WhatsApp())
send_photo3.send()