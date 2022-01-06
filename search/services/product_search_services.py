from elasticsearch_dsl import Q
from django.utils import timezone
from search.documents.product_document import ProductDocument


class ProductSearchService:

    def get_products(self, query_params):
        term = query_params.get('term')
        now = timezone.now()

        es_query = ProductDocument.search()
        # get active products
        es_query = es_query.query(
            Q("match", is_available=True)
            & Q("range", valid_from={"lte": now})
            & Q("range", valid_until={"gte": now})
        )
        # get products according to search
        es_query = es_query.query(
            Q("match", name=term)
            | Q("match", code=term)
        )
        # query = Q("match", name=term) | Q("match", code=term)
        products = es_query.execute()
        return products
