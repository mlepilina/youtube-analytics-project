"""Тесты с использованием pytest для модуля channel."""
import pytest
from src.channel import Channel, api_key


def test_api_key():
    assert api_key == 'AIzaSyDUZLRoOpF7OfeVheZqw9hYMcGZVY6Feok'


@pytest.fixture()
def moscow_python():
    return Channel('UC-OVMPlMA3-YCIeg4z5z23A')


def test_print_info(moscow_python):
    assert moscow_python.print_info() is None

