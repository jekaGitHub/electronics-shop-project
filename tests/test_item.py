"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item_default():
    return Item("Смартфон", 10000, 20)


def test_item_init(item_default):
    assert item_default.name == "Смартфон"
    assert item_default.price == 10000
    assert item_default.quantity == 20


def test_item_calculate_total_price(item_default):
    assert item_default.calculate_total_price() == 200000


def test_item_apply_discount(item_default):
    item_default.apply_discount()
    assert item_default.price == 10000.0
