import pytest
from src.phone import Phone


@pytest.fixture
def phone_default():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_phone_init(phone_default):
    phone1 = phone_default
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2
