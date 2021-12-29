from django.utils import timezone

from product.models import Product


class ProductService:
    model = Product

    def __init__(self, request=None, user=None):
        self.request = request
        self.user = user

    def get_product_by_uuid(self, uuid):
        return self.model.objects.get(uuid=uuid)

    def get_active_product_list(self):
        """ Return the product that are available and active in stock"""
        now = timezone.now()
        product_list = self.model.objects.filter(
            is_available=True, valid_from__lte=now, valid_until__gte=now
        )
        return product_list
