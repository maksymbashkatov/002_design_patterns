from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        """
        Делегирует полученную команду на исполнение получателю (исполнителю).
        """
        pass

class Programmer:
    def write_code(self):
        print('Программист напишет код.')

    def fix_bug(self):
        print('Программист исправит баг.')

class Tester:
    def find_bug(self):
        print('Тестер найдёт баг.')

class WriteCodeCommand(Command):
    def __init__(self, executor: Programmer):
        self.__executor = executor

    def execute(self):
        self.__executor.write_code()

class FixBugCommand(Command):
    def __init__(self, executor: Programmer):
        self.__executor = executor

    def execute(self):
        self.__executor.fix_bug()

class FindBugCommand(Command):
    def __init__(self, executor: Tester):
        self.__executor = executor

    def execute(self):
        self.__executor.find_bug()

class Manager:
    """
    Отправитель команд.
    """
    __list_of_commands: list[Command]

    def __init__(self):
        self.__list_of_commands = []

    def add_commands(self, *commands):
        """
        Добавлет команды на выполнение в список команд.
        """
        for command in commands:
            self.__list_of_commands.append(command)

    def start_work(self):
        """
        Запускает выполнение команд.
        """
        for command in self.__list_of_commands:
            command.execute()

    def stop_work(self):
        """
        Очищает историю выполнения команд.
        """
        self.__list_of_commands.clear()

    def cancel_command(self):
        """
        Операция отмены (последней команды из стека).
        """
        self.__list_of_commands.pop()

# tests
programmer = Programmer()
tester = Tester()
manager = Manager()
manager.add_commands(WriteCodeCommand(programmer),
                     FindBugCommand(tester),
                     FixBugCommand(programmer))
# manager.cancel_command()
manager.start_work()
manager.stop_work()

# manager.add_commands(WriteCodeCommand(programmer),
#                      FindBugCommand(tester),
#                      WriteCodeCommand(programmer),
#                      FindBugCommand(tester),
#                      FixBugCommand(programmer))
# manager.start_work()