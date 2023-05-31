"""Тесты с использованием pytest для модуля video"""

import pytest
from src.video import Video, PLVideo


@pytest.fixture()
def video_1():
    return Video('AWX4JnAnjBE')


@pytest.fixture()
def playlist_1():
    return PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')


def test_video_id(video_1):
    """Тестируем, что video_id совпадает с ожидаемым и невозможность установить его напрямую"""
    assert video_1.video_id == 'AWX4JnAnjBE'
    with pytest.raises(AttributeError):
        video_1.video_id = '1234'


def test_str_1(video_1):
    """Тестируем метод, возвращающий название видео"""
    assert str(video_1) == 'GIL в Python: зачем он нужен и как с этим жить'


def test_str_2(playlist_1):
    """Тестируем метод, возвращающий название плэйлиста"""
    assert str(playlist_1) == 'MoscowPython Meetup 78 - вступление'




