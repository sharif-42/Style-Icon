import pytest


@pytest.fixture()
def user_create_payload():
    return {
        "username": "test",
        "password": "testpass",
        "email": "test@gmail.com",
        "phone_number": "01780510023",
    }


@pytest.fixture()
def user_create_payload_with_short_password():
    return {
        "username": "test",
        "password": "ts",
        "email": "test@gmail.com",
        "phone_number": "01780510023",
    }

