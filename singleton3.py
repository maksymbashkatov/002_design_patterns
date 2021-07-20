class Database:
    instance = None # Переменная для хранения экземпляра класса.

    def __init__(self):
        if Database.instance is not None:
            self.get_instance()

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Database()
        return cls.instance

# С помощью статического метода создаю экземпляр класса
admin = Database.get_instance()
# Дальше пытаюсь вновь создать экземпляр класса, но поскольку он создан
# в переменную помещаетса ссылка на уже существующий
user1 = Database.get_instance()
user2 = Database.get_instance()

print(user1)
print(user2)