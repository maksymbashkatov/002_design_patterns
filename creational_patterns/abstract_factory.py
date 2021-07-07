from __future__ import annotations
from abc import ABC, abstractmethod

class FilmStudio(ABC):
    """
    Базовый класс Создатель. Объявляет фабричные методы, возвращает новые объекты фильмов в зависимости от жанра фильма,
    а также студии с с которой подписан контракт.
    """
    @abstractmethod
    def _create_fantasy_film(self) -> FantasyFilm:
        """
        Фабричный метод.
        :return: в переопределённых будет возвращать объект фильма жара Fantasy от нужной компании
        """
        pass

    @abstractmethod
    def _create_drama_film(self) -> DramaFilm:
        """
        Фабричный метод.
        :return: в переопределённых будет возвращать объект фильма жара Drama от нужной компании
        """
        pass

    def basic_business_logic(self, genre: str):
        # Вызов фабричного метода, чтобы получить объект-фильм, в зависимости от выбранного жанра
        film = self._create_fantasy_film() if genre == 'Fantasy' else self._create_drama_film()
        # Сообщение о том от какой компании будет доставлен в кинотеатр фильм.
        print(film._go_to_theater())

class UniversalPictures(FilmStudio):
    def _create_fantasy_film(self) -> FantasyFilm:
        return UniversalPicturesFilmFantasy()

    def _create_drama_film(self) -> DramaFilm:
        return UniversalPicturesFilmDrama()

class NewLineCinema(FilmStudio):
    def _create_fantasy_film(self) -> FantasyFilm:
        return NewLineCinemaFilmFantasy()

    def _create_drama_film(self) -> DramaFilm:
        return NewLineCinemaFilmDrama()

class FantasyFilm(ABC):
    """
    Базовый класс продукта. Определяет общий интерфейс фильмов жанра Fantasy.
    """

    _name = 'Fantasy'

    @abstractmethod
    def _go_to_theater(self):
        """
        :return: строку с информаией о том от какой компании будет доставлен в кинотеатр фильм
        """
        pass

class DramaFilm(ABC):
    """
    Базовый класс продукта. Определяет общий интерфейс фильмов жанра Drama.
    """

    _name = 'Drama'

    @abstractmethod
    def _go_to_theater(self):
        """
        :return: строку с информаией о том от какой компании будет доставлен в кинотеатр фильм
        """
        pass

class UniversalPicturesFilmFantasy(FantasyFilm):
    def _go_to_theater(self) -> str:
        return 'В кинотеатр отправляется фильм компании UniversalPictures. Жанр фильма {}.'.format(self._name)

class UniversalPicturesFilmDrama(DramaFilm):
    def _go_to_theater(self) -> str:
        return 'В кинотеатр отправляется фильм компании UniversalPictures. Жанр фильма {}.'.format(self._name)

class NewLineCinemaFilmFantasy(FantasyFilm):
    def _go_to_theater(self) -> str:
        return 'В кинотеатр отправляется фильм компании NewLineCinema. Жанр фильма {}.'.format(self._name)

class NewLineCinemaFilmDrama(DramaFilm):
    def _go_to_theater(self) -> str:
        return 'В кинотеатр отправляется фильм компании NewLineCinema. Жанр фильма {}.'.format(self._name)

# tests
def contract_with(film_studio: FilmStudio, genre: str):
    """
    Запускает базовую бизнес-логику.
    :param film_studio: объект киностудии
    :param genre: жанр фильма
    """
    film_studio.basic_business_logic(genre)

contract_with(UniversalPictures(), 'Drama')
contract_with(NewLineCinema(), 'Fantasy')