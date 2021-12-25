from django.utils.translation import gettext_lazy as _
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from ..serializers import (
    UserInputSerializer,
    UserOutputSerializer
)
from ..services.user_service import UserService


class UserListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = UserInputSerializer  # input serializer
    output_serializer_class = UserOutputSerializer  # output serializer
    service_class = UserService
    # permission_classes = [IsAdminUser]
    # TODO: add required permission classes
    # TODO: Add pagination for list api

    def list(self, request, *args, **kwargs):
        users = self.service_class().get_user_list()
        serializer = self.output_serializer_class(users, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self,  request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.service_class().create_user(**serializer.validated_data)
        output_serializer = self.output_serializer_class(user)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)


class UserLoginApiView(TokenObtainPairView):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """
    serializer_class = TokenObtainPairSerializer
    output_user_serializer_class = UserOutputSerializer
    service_class = UserService

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        authenticated_user = self.service_class(request=request).user_login(
            username=request.data['username'],
            password=request.data['password']
        )
        if authenticated_user:
            custom_response = {
                'user_info': self.output_user_serializer_class(authenticated_user).data,
                'access_token': serializer.validated_data['access'],
                'refresh_token': serializer.validated_data['refresh']
            }
            return Response(custom_response, status=status.HTTP_200_OK)
        else:
            custom_response = {
                "message": _("Unable to authenticate with provided credentials!")
            }
            return Response(custom_response, status=status.HTTP_401_UNAUTHORIZED)

