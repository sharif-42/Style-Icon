from django.utils import timezone
from django.core.cache import cache
from product.models import Product
from rest_utils.exceptions import (
    ProductNotFoundException,
)


class ProductService:
    model = Product

    def __init__(self, request=None, user=None):
        self.request = request
        self.user = user

    def set_cache_product(self, cache_key, product_response):
        """
        Cache product for 1 hour
        :param cache_key: cache_key
        :param product_response: product_response
        :return: None
        """
        cache.set(cache_key, product_response, 60 * 60)

    def get_cached_product(self, cache_key):
        cached_response = cache.get(cache_key)
        return cached_response

    def get_product_by_code(self, code):
        try:
            return self.model.objects.get(code=code)
        except Product.DoesNotExist:
            raise ProductNotFoundException()

    def get_product_by_uuid(self, uuid):
        try:
            return self.model.objects.get(uuid=uuid)
        except Product.DoesNotExist:
            raise ProductNotFoundException()

    def get_active_product_list(self):
        """ Return the product that are available and active in stock"""
        now = timezone.now()
        product_list = self.model.objects.filter(
            is_available=True, valid_from__lte=now, valid_until__gte=now
        )
        return product_list

    def get_product_name_by_product_code(self, product_code):
        try:
            product = self.model.objects.get(code=product_code)
            return product.name
        except Product.DoesNotExist:
            raise ProductNotFoundException()
