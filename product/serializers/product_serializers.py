from rest_framework import serializers

from product.models import Product
from product.serializers.product_brand_serializers import ProductBrandSerializer
from product.serializers.product_group_serializers import ProductGroupSerializer
from product.serializers.product_type_serializers import ProductTypeSerializer


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
        return ProductGroupSerializer(instance.product_group).data

    def get_product_type(self, instance):
        return ProductTypeSerializer(instance.product_type).data

    def get_brand(self, instance):
        return ProductBrandSerializer(instance.brand).data
