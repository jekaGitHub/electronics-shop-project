"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item, InstantiateCSVError
from src.phone import Phone


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


def test_string_to_number():
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("5.0") == 5
    assert Item.string_to_number("5.5") == 5


def test_name_setter(item_default):
    item = item_default
    item.name = "СуперСмартфон"
    assert item.name == "СуперСмарт"


def test_instantiate_from_csv():
    Item.instantiate_from_csv("src/items.csv")
    assert len(Item.all) == 5
    assert Item.all[0].name == "Смартфон"


def test_repr_and_str_item():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'


def test_add_item_and_phone(item_default, phone_default):
    item1 = item_default
    phone1 = phone_default
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10


# Тест для ошибки FileNotFoundError
def test_instantiate_from_csv_not_found_file_error():
    with pytest.raises(FileNotFoundError, match='Файл не найден!'):
        Item.instantiate_from_csv()


# Тест для ошибки InstantiateCSVError
def test_instantiate_from_csv_error():
    with pytest.raises(InstantiateCSVError, match='Файл повреждён!'):
        Item.instantiate_from_csv()
