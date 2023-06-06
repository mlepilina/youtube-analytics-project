"""Тесты с использованием pytest для модуля playlist"""
import datetime

import pytest
from src.playlist import PlayList


@pytest.fixture()
def playlist_1():
    return PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')


def test_playlist_title(playlist_1):
    """Тестируем вывод названия плэйлиста"""
    assert playlist_1.title == "Moscow Python Meetup №81"


def test_playlist_url(playlist_1):
    """Тестируем вывод ссылки на плэйлист"""
    assert playlist_1.url == "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw"


def test_total_duration(playlist_1):
    """Тестируем вывод общей длительности всех видео плэйлиста"""
    assert isinstance(playlist_1.total_duration, datetime.timedelta)
    assert str(playlist_1.total_duration) == "1:49:52"


def test_total_seconds(playlist_1):
    """Тестируем вывод общей длительности всех видео плэйлиста в секундах"""
    assert playlist_1.total_duration.total_seconds() == 6592.0


def test_show_best_video(playlist_1):
    """Тестируем вывод ссылки на видео с самым большим кол-вом лайков"""
    assert playlist_1.show_best_video() == "https://youtu.be/cUGyMzWQcGM"

