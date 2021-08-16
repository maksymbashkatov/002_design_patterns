from __future__ import annotations
from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: BaseComponent, event: str):
        pass

class Game(Mediator):
    def __init__(self, keyboard: Keyboard, person_on_screen: PersonOnScreen):
        self.__keyboard = keyboard
        self.__keyboard.mediator = self
        self.__person_on_screen = person_on_screen
        self.__person_on_screen.mediator = self

    def notify(self, sender: BaseComponent, event: str):
        if event == 'push_w':
            self.__person_on_screen.go_forward()
        elif event == 'push_s':
            self.__person_on_screen.go_back()

class BaseComponent:
    @property
    def mediator(self):
        return self.__mediator

    @mediator.setter
    def mediator(self, mediator: Mediator):
        self.__mediator = mediator

class Keyboard(BaseComponent):
    def push_w(self):
        print('Нажата клавиша w.')
        self.mediator.notify(self, 'push_w')

    def push_s(self):
        print('Нажата клавиша s.')
        self.mediator.notify(self, 'push_s')

class PersonOnScreen(BaseComponent):
    def go_forward(self):
        print('Идёт вперёд.')
        self.mediator.notify(self, 'go_forward')

    def go_back(self):
        print('Идёт назад.')
        self.mediator.notify(self, 'go_back')

# tests
keyboard = Keyboard()
person_on_screen = PersonOnScreen()

game1 = Game(keyboard, person_on_screen)
keyboard.push_w()
keyboard.push_s()

print('---')
game2 = Game(keyboard, person_on_screen)
keyboard.push_w()
keyboard.push_w()