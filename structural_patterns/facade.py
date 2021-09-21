from random import choice


class Programmer:
    def write_code(self):
        print('Программист пишет код.')

    def fix_bug(self):
        print('Программист исправляет баг.')


class Tester:
    __bug_found: bool

    def find_bug(self):
        """
        Тестер ищет баг. Если находит, то __bug_found становится True и программист снова пишет код.
        Так происходит пока находится баг. Перед новой проверкой код предположительно исправный
        с __bug_found False.
        """
        self.__bug_found = False
        print('Тестер ищет баг.')
        true_or_false = [True, False, True]
        if choice(true_or_false):
            self.__bug_found = True

    def bug_found(self):
        return self.__bug_found


class WriteCodeFacade:
    def __init__(self, programmer: Programmer(), tester: Tester()):
        self.__programmer = programmer
        self.__tester = tester

    def work_with_code(self):
        self.__programmer.write_code()
        self.__tester.find_bug()
        while self.__tester.bug_found():
            self.__programmer.write_code()
            self.__tester.find_bug()


# tests
programmer1 = Programmer()
tester1 = Tester()
facade1 = WriteCodeFacade(programmer1, tester1)
facade1.work_with_code()
