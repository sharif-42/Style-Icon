from rest_framework import status, generics
from rest_framework.response import Response

from product.services import ProductService
from product.serializers import (
    ProductListSerializer,
    ProductDetailsSerializer,
)


class ProductListApiView(generics.ListAPIView):
    """ This api will consumed by FE """
    serializer_class = ProductListSerializer
    service_class = ProductService

    def list(self, request, *args, **kwargs):
        product_list = self.service_class().get_active_product_list()
        serializer = self.serializer_class(product_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductDetailsApiView(generics.RetrieveAPIView):
    """ This api will consumed by FE """
    serializer_class = ProductDetailsSerializer
    service_class = ProductService

    def get(self, request, *args, **kwargs):
        product = self.service_class().get_product_by_uuid(uuid=kwargs.get('uuid'))
        serializer = self.serializer_class(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
