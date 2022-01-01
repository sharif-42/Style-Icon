from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from product.models import (
    Product,
    ProductBrand,
    ProductType,
    ProductGroup,
)


@registry.register_document
class ProductDocument(Document):
    pk = fields.IntegerField()
    product_group = fields.ObjectField(properties={
        'name': fields.TextField(),
        'description': fields.TextField(),
        'is_available': fields.BooleanField(),
    })
    product_type = fields.ObjectField(properties={
        'name': fields.TextField(),
        'description': fields.TextField(),
        'system_type': fields.TextField(),
        'is_available': fields.BooleanField(),
    })
    brand = fields.ObjectField(properties={
        'name': fields.TextField(),
        'description': fields.TextField(),
        'is_available': fields.BooleanField(),
    })
    uuid = fields.KeywordField()
    code = fields.KeywordField()

    class Index:
        # Name of the Elasticsearch index
        name = 'products'
        # See Elasticsearch Indices API reference for available settings
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = Product
        queryset_pagination = 2000
        fields = [
            'name',
            'in_stock',
            'short_description',
            'long_description',
            'weight',
            'release_date',
            'pre_order',
            'is_serviceable',
            'is_available',
            'service_period',
            'valid_from',
            'valid_until',
        ]
        related_models = [
            ProductType,
            ProductGroup,
            ProductBrand,
        ]
        rebuild_from_value_list = True

    def get_instances_from_related(self, related_instance):
        """ If related_models is set, define how to retrieve the Product instance(s) from the related model.
            The related_models option should be used with caution because it can lead in the index
            to the updating of a lot of items.
        """
        if isinstance(related_instance, ProductType):
            return related_instance.products.all()
        if isinstance(related_instance, ProductBrand):
            return related_instance.products.all()
        if isinstance(related_instance, ProductBrand):
            return related_instance.products.all()
