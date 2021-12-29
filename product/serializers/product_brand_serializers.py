from rest_framework import serializers

from product.models import ProductBrand


class ProductBrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductBrand
        fields = [
            'uuid',
            'code',
            'name'
        ]
