from __future__ import annotations
from abc import ABC, abstractmethod

class FilmStudio(ABC):
    """
    Базовый класс Создатель. Объявляет фабричный метод, возвращает новые объекты фильмов в зависимости от студии с
    с котрой подписан контракт.
    """
    @abstractmethod
    def create_film(self):
        """
        Фабричный метод.
        :return: объект фильма
        """
        pass

    def basic_business_logic(self):
        # Вызов фабричного метода, чтобы получить объект-фильм.
        film = self.create_film()
        # Сообщение о том от какой компании будет доставлен в кинотеатр фильм.
        print(film.go_to_theater())

class UniversalPictures(FilmStudio):
    def create_film(self) -> Film:
        return UniversalPicturesFilm()

class NewLineCinema(FilmStudio):
    def create_film(self) -> Film:
        return NewLineCinemaFilm()

class Film(ABC):
    """
    Базовый класс продукта. Определяет общий интерфейс фильмов.
    """
    @abstractmethod
    def go_to_theater(self):
        """
        :return: строку с информаией о том от какой компании будет доставлен в кинотеатр фильм
        """
        pass

class UniversalPicturesFilm(Film):
    def go_to_theater(self) -> str:
        return 'В кинотеатр отправляется фильм компании UniversalPictures.'

class NewLineCinemaFilm(Film):
    def go_to_theater(self) -> str:
        return 'В кинотеатр отправляется фильм компании NewLineCinema.'

# tests
def contract_with(film_studio: FilmStudio):
    """
    Запускает базовую бизнес-логику.
    :param film_studio: объект киностудии
    """
    film_studio.basic_business_logic()

contract_with(UniversalPictures())
contract_with(NewLineCinema())