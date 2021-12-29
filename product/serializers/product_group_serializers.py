from rest_framework import serializers

from product.models import ProductGroup


class ProductGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductGroup
        fields = [
            'uuid',
            'code',
            'name',
        ]
