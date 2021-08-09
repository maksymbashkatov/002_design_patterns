from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum


class Responsibility(Enum):
    WRITE_CODE = 'напишет код.'
    FIND_BUG = 'найдёт баг.'
    FIX_BUG = 'исправит баг.'

class ResponsibilityHandler(ABC):
    """
    Интерфейс обработчика обязанности.
    """
    _next_responsibility_handler: ResponsibilityHandler = None

    def set_next(self, handler: ResponsibilityHandler) -> ResponsibilityHandler:
        """
        Передаёт обработку запроса следующему в очереди, если данный объект не может обработать запрос.
        """
        self._next_responsibility_handler = handler
        return handler

    @abstractmethod
    def handle_responsibility(self, request: Responsibility):
        if self._next_responsibility_handler:
            """
            Принимает запрос и если присутсвует тот кто обработает запрос, возвращает ответ,
            если нет, ищет следующего в очереди и повторяет тоже самое, если и его нет, то возвращает ничего.
            """
            return self._next_responsibility_handler.handle_responsibility(request)
        return None

class ProgrammerHandler(ResponsibilityHandler):
    def handle_responsibility(self, request: Responsibility) -> str:
        if request is Responsibility.WRITE_CODE or request is Responsibility.FIX_BUG:
            return f'Программист {request.value}'
        else:
            return super().handle_responsibility(request)

class TesterHandler(ResponsibilityHandler):
    def handle_responsibility(self, request: Responsibility) -> str:
        if request is Responsibility.FIND_BUG:
            return f'Тестер {request.value}'
        else:
            return super().handle_responsibility(request)

# tests
programmer = ProgrammerHandler()
tester = TesterHandler()

programmer.set_next(tester)
print(programmer.handle_responsibility(Responsibility.FIND_BUG))