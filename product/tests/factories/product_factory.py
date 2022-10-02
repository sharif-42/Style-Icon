import uuid
import factory
from faker import Faker

from django.utils import timezone

from product.models import Product, ProductGroup, ProductType, ProductBrand

fake = Faker()


class BaseFactory(factory.django.DjangoModelFactory):
    class Meta:
        abstract = True

    uuid = uuid.uuid4()
    code = fake.random_number(digits=5)


class ProductGroupFactory(BaseFactory):
    class Meta:
        model = ProductGroup

    name = fake.name()
    description = fake.text()  # fake.sentence()


class ProductTypeFactory(BaseFactory):
    class Meta:
        model = ProductType

    name = fake.name()
    description = fake.text()  # fake.sentence()
    system_type = "handset"


class ProductBrandFactory(BaseFactory):
    class Meta:
        model = ProductBrand

    name = fake.name()
    description = fake.text()  # fake.sentence()


class ProductFactory(BaseFactory):
    class Meta:
        model = Product

    code = "factory-test"
    name = fake.name()
    product_group = factory.SubFactory(ProductGroupFactory)  # Generating FK relations
    product_type = factory.SubFactory(ProductTypeFactory)
    brand = factory.SubFactory(ProductBrandFactory)
    in_stock = fake.random_int()
    short_description = fake.text()
    long_description = fake.text()
    is_available = True
    release_date = timezone.now() + timezone.timedelta(days=1)
    valid_from = timezone.now() - timezone.timedelta(days=10)
    valid_until = timezone.now() + timezone.timedelta(days=10)
