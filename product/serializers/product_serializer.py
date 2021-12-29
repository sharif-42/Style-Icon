from rest_framework import serializers

from product.models import Product


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'uuid',
            'code',
            'name',
            'is_available',
            'in_stock',
            'short_description',
            'pre_order',
            'is_serviceable',
            'weight',
            # TODO: have to add image fields here
        ]


class ProductDetailsSerializer(serializers.ModelSerializer):
    product_group = serializers.SerializerMethodField()
    product_type = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'uuid',
            'code',
            'name',
            'is_available',
            'in_stock',
            'short_description',
            'pre_order',
            'is_serviceable',
            'weight',
            'product_group',
            'product_type',
            'brand',
            # TODO: have to add image fields here
        ]

    def get_product_group(self, instance):
        return instance.name

    def get_product_type(self, instance):
        return instance.name

    def get_brand(self, instance):
        return instance.name

