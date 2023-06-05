"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import *


@pytest.fixture
def product_list_1():
    return Item("Пулемет", 25000, 5)


def test_calculate_total_price(product_list_1):
    assert product_list_1.calculate_total_price() == 125000


def test_apply_discount(product_list_1):
    Item.pay_rate = 0.5
    product_list_1.apply_discount()
    assert product_list_1.price == 12500


def test_string_to_number():
    assert Item.string_to_number('12.8') == 12


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'
