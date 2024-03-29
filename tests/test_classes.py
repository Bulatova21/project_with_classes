from src.class_category import Category
from src.class_product import Product
import pytest


@pytest.fixture()
def category_teh():
    return Category("Техника", "Электрические приборы", ["утюг", "пылесос", "кофемашинка"])


def test_init_category(category_teh):
    assert category_teh.name == "Техника"
    assert category_teh.description == "Электрические приборы"
    assert category_teh.product == ["утюг", "пылесос", "кофемашинка"]
    assert category_teh.total_number_of_categories == 1
    assert category_teh.total_number_of_unique_products == 3

@pytest.fixture()
def product_teh():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_init_product(product_teh):
    assert product_teh.name == "Samsung Galaxy C23 Ultra"
    assert product_teh.description == "256GB, Серый цвет, 200MP камера"
    assert product_teh.price == 180000.0
    assert product_teh.quantity == 5