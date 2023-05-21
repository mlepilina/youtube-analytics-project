"""Тесты с использованием pytest для модуля channel."""
import json

import pytest
from src.channel import Channel, api_key, youtube


def test_api_key():
    '''Тестируем существование api-ключа'''
    assert api_key == 'AIzaSyDUZLRoOpF7OfeVheZqw9hYMcGZVY6Feok'


@pytest.fixture()
def moscow_python():
    return Channel('UC-OVMPlMA3-YCIeg4z5z23A')


def test_print_info(moscow_python):
    '''Тестируем, что функция ничего не возвращает'''
    assert moscow_python.print_info() is None


def test_get_service(moscow_python):
    '''Тестируем, что функция возвращает объект youtube'''
    assert moscow_python.get_service() == youtube


def test_to_json(moscow_python):
    '''Тестируем, что функция ничего не возвращает и создается файл .json'''
    assert moscow_python.to_json('moscowpython.json') is None
    with open('moscowpython.json') as f:
        saved_json = json.load(f)
    assert saved_json['title'] == 'MoscowPython'


def test_channel_id(moscow_python):
    '''Тестируем, что channel_id совпадает с ожидаемым и невозможность установить его напрямую'''
    assert moscow_python.channel_id == 'UC-OVMPlMA3-YCIeg4z5z23A'
    with pytest.raises(AttributeError):
        moscow_python.channel_id = '1234'
