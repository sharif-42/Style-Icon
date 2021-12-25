from django.conf import settings
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse(f"{settings.API_VERSION_NAMESPACE}:user:user-list-create")


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
