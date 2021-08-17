class Memento:
    """
    Фиксирует текущее состояние.
    """
    def __init__(self, state: list[str]):
        self.__state = state

    def get_state(self) -> list[str]:
        return self.__state

class Coffee:
    """
    Создатель, имеет полный доступ к снимку.
    """
    def __init__(self):
        self.__list_of_ingredients: list[str] = []

    def add_ingredient(self, ingredient: str):
        print(f"В кофе добавлен ингредиент: {ingredient}")
        self.__list_of_ingredients.append(ingredient)

    def save(self):
        """
        Сохраняет состояние.
        """
        # return Memento(self.__list_of_ingredients)
        return Memento(self.__list_of_ingredients[:])

    def restore(self, memento: Memento):
        """
        Возвращает предыдущее состояние.
        """
        self.__list_of_ingredients = memento.get_state()

    def __str__(self):
        return f"Текущее состояние кофе: {self.__list_of_ingredients}"

class Barista:
    """
    Опекун, имеет доступ к снимку через создателя.
    """
    def __init__(self, coffee: Coffee):
        self.__coffee = coffee
        self.__coffee_states: list[Memento] = []

    def add_ingredient_to_coffee(self, ingredient: str):
        # В список состояний, сохраняется текущее состояние списка с ингредиентами.
        self.__coffee_states.append(self.__coffee.save())
        # В список ингредиентов добавляется новый ингредиент.
        self.__coffee.add_ingredient(ingredient)
        # for memento in self.__coffee_states:
        #     print(f'--- {memento.get_state()}')

    def undo_add_ingredient(self):
        """
        Отменить добавление ингредиента.
        """
        if len(self.__coffee_states) == 0:
            print('В кружке нет ингредиентов.')
        else:
            # Удаляется последнее состояние из списка состояний.
            self.__coffee.restore(self.__coffee_states.pop())
            print('Предыдущий ингредиент удалён.')

# tests
coffee = Coffee()
barista = Barista(coffee)
print(coffee)
barista.add_ingredient_to_coffee('boiling water')
barista.add_ingredient_to_coffee('coffee')
barista.add_ingredient_to_coffee('milk')
barista.add_ingredient_to_coffee('salt')
print(coffee)
barista.undo_add_ingredient()
barista.add_ingredient_to_coffee('sugar')
print(coffee)