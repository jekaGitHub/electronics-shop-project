import pytest
from src.keyboard import Keyboard


@pytest.fixture
def keyboard_default():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_keyboard_init(keyboard_default):
    kb = keyboard_default
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang()
    assert str(kb.language) == "EN"
