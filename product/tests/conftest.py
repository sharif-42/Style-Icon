import pytest

from pytest_factoryboy import register
from product.tests.factories.product_factory import ProductFactory

register(ProductFactory)  # test will use product_factory
