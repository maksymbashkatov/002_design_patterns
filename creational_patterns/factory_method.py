from __future__ import annotations
from abc import ABC, abstractmethod

class FilmStudio(ABC):
    """
    Базовый класс Создатель. Объявляет фабричный метод, возвращает новые объекты фильмов в зависимости от студии с
    с которой подписан контракт.
    """
    @abstractmethod
    def _create_film(self) -> Film:
        """
        Фабричный метод.
        :return: в переопределённых будет возвращать объект фильма от нужной компании
        """
        pass

    def basic_business_logic(self):
        # Вызов фабричного метода, чтобы получить объект-фильм.
        film = self._create_film()
        # Сообщение о том от какой компании будет доставлен в кинотеатр фильм.
        print(film._go_to_theater())

class UniversalPictures(FilmStudio):
    def _create_film(self) -> Film:
        return UniversalPicturesFilm()

class NewLineCinema(FilmStudio):
    def _create_film(self) -> Film:
        return NewLineCinemaFilm()

class Film(ABC):
    """
    Базовый класс продукта. Определяет общий интерфейс фильмов.
    """
    @abstractmethod
    def _go_to_theater(self):
        """
        :return: строку с информаией о том от какой компании будет доставлен в кинотеатр фильм
        """
        pass

class UniversalPicturesFilm(Film):
    def _go_to_theater(self) -> str:
        return 'В кинотеатр отправляется фильм компании UniversalPictures.'

class NewLineCinemaFilm(Film):
    def _go_to_theater(self) -> str:
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