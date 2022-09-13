import pytest
from django.conf import settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from django.contrib.auth import get_user_model

# urls/views for tests
LIST_CREATE_URL = reverse(f"{settings.API_VERSION_NAMESPACE}:user:user-list-create")
LOGIN_URL = reverse(f"{settings.API_VERSION_NAMESPACE}:user:user-login")

pytestmark = pytest.mark.django_db


class TestUserListCreateAPI:
    """
        Test the user list create api
    """

    def test_user_create_api(self, user_create_payload):
        response = APIClient().post(LIST_CREATE_URL, user_create_payload)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["username"] == user_create_payload["username"]

    def test_password_too_short(self, user_create_payload_with_short_password):
        response = APIClient().post(LIST_CREATE_URL, user_create_payload_with_short_password)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_user_list_api(self, user_create_payload):
        """ Test User List API"""
        # Test with empty list
        response = APIClient().get(LIST_CREATE_URL)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 0

        # New testing with creating 1 user
        user = get_user_model().objects.create_user(**user_create_payload)
        response = APIClient().get(LIST_CREATE_URL)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1


class TestUserLoginAPI:
    """
        Test User login API.
    """

    def test_create_token_for_valid_credential(self, user_create_payload):
        """ Test token is created for valid credentials/user """

        user = get_user_model().objects.create_user(**user_create_payload)  # creating user with same token
        response = APIClient().post(LOGIN_URL, user_create_payload)  # requesting for token with valid credentials

        assert response.status_code == status.HTTP_200_OK
        assert response.data["user_info"]["username"] == user_create_payload["username"]
        assert response.data["user_info"]["email"] == user_create_payload["email"]
        assert 'access_token' in response.data.keys()
        assert 'refresh_token' in response.data.keys()

    def test_create_token_for_invalid_credential(self, user_create_payload):
        """ Test token is created for valid credentials/user """
        user = get_user_model().objects.create_user(**user_create_payload)

        user_create_payload["password"] = "wrong_password"
        response = APIClient().post(LOGIN_URL, user_create_payload)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.data["message"] == "Unable to authenticate with provided credentials!"
