from django.conf import settings
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

# urls/views for tests
CREATE_USER_URL = reverse(f"{settings.API_VERSION_NAMESPACE}:user:user-list-create")
USER_TOKEN_URL = reverse(f"{settings.API_VERSION_NAMESPACE}:user:user-login")


class PublicUserApiTests(TestCase):
    """
    Test the public user create api
    """

    def setUp(self) -> None:
        self.client = APIClient()

    def create_user(self, **kwargs):
        return get_user_model().objects.create_user(**kwargs)

    def test_create_valid_user_successful(self):
        """ Test Create user api for valid user"""
        payload = {
            "username": "test",
            "password": "testpass",
            "email": "test@gmail.com",
            "phone_number": "01780510023",
        }

        response = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNotIn('password', response.data)

    def test_exits_user(self):
        """ Test api for already exists api """
        payload = {
            "username": "test",
            "password": "testpass",
            "email": "test@gmail.com",
            "phone_number": "01780510023",
        }
        user = self.create_user(**payload)
        response = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        payload = {
            "username": "test",
            "password": "ts",
            "email": "test@gmail.com",
            "phone_number": "01780510023",
        }
        response = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_for_valid_credential(self):
        """ Test token is created for valid credentials/user """
        payload = {
            "username": "test",
            "password": "testpass",
        }
        self.create_user(**payload)  # creating user with same token
        response = self.client.post(USER_TOKEN_URL, payload)  # requesting for token with valid credentials
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access_token', response.data)
        self.assertIn('refresh_token', response.data)
        self.assertIn('user_info', response.data)

    def test_create_token_invalid_credentials(self):
        """ Test token is created for invalid credentials/user """
        payload_for_create_user = {
            "username": "test",
            "password": "testpass",
        }
        payload_for_token = {
            "username": "test",
            "password": "testpassss",
        }
        self.create_user(**payload_for_create_user)  # creating user with same token
        response = self.client.post(USER_TOKEN_URL, payload_for_token)  # requesting for token with valid credentials

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn('token', response)

    def test_create_token_for_not_existing_user(self):
        """ Test for that user, which is not in the system """
        payload = {
            "username": "test",
            "password": "testpass",
        }
        response = self.client.post(USER_TOKEN_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertNotIn('token', response)

    def test_create_token_for_missing_field(self):
        """ Test for a missing field"""
        payload = {
            "username": "test",
            "password": "",
        }
        response = self.client.post(USER_TOKEN_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', response)
