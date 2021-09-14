from __future__ import annotations
from abc import ABC, abstractmethod


class Role(ABC):
    __name: str

    @property
    def name(self):
        return self.__name

    def __init__(self, name):
        self.__name = name

    @abstractmethod
    def inform(self, chat: Chat):
        """
        Информирование участника чата о нынешнем состоянии чата.
        """
        pass


class Chat:
    _roles: list[Role] = []
    __roles_amount = 0

    @property
    def roles_amount(self):
        return self.__roles_amount

    def join(self, role: Role):
        print(f'{role.name} вошёл в чат.')
        self._roles.append(role)
        Chat.__roles_amount += 1

    def leave(self, role: Role):
        print(f'{role.name} вышел из чата.')
        self._roles.remove(role)
        Chat.__roles_amount -= 1

    def informing_users(self):
        print('--- Информирование всех пользователей чата. ---')
        for role in self._roles:
            role.inform(self)


class Moderator(Role):
    def inform(self, chat: Chat):
        print(f'Добрый день модератор {self.name}, нас {chat.roles_amount} в чате.')


class User(Role):
    def inform(self, chat: Chat):
        print(f'Добрый день пользователь {self.name}, нас {chat.roles_amount} в чате.')


chat1 = Chat()
role1 = Moderator('Moderator1')
chat1.join(role1)

role2 = User('User1')
chat1.join(role2)

role3 = User('User2')
chat1.join(role3)

chat1.informing_users()

chat1.leave(role2)
chat1.informing_users()