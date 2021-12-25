from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from ..models import User

from ..serializers import (
    UserInputSerializer,
    UserOutputSerializer
)
from ..services.user_service import UserService


class UserListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = UserInputSerializer  # input serializer
    output_serializer_class = UserOutputSerializer  # output serializer
    service_class = UserService()
    # permission_classes = [IsAdminUser]
    # TODO: add required permission classes
    # TODO: Add pagination for list api

    def list(self, request, *args, **kwargs):
        users = self.service_class.get_user_list()
        serializer = self.output_serializer_class(users, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self,  request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.service_class.create_user(**serializer.validated_data)
        output_serializer = self.output_serializer_class(user)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)

