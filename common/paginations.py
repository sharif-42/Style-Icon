from rest_framework.pagination import PageNumberPagination


class BasePageNumberPagination(PageNumberPagination):
    # User different pagination for different list apis
    page_size = 20
    page_size_query_param = 'page_size'


class ProductPageNumberPagination(BasePageNumberPagination):
    page_size = 30


class UserPageNumberPagination(BasePageNumberPagination):
    page_size = 10
