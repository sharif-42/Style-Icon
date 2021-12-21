from django.test import TestCase
from user.models import User


class UserModelTests(TestCase):
    def test_create_user_method(self):
        username = 'sharif'
        email = "shariful@test.com"
        password = '123$%^qwer'
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_dashboard_user)

    def test_create_super_user_method(self):
        username = 'sharif'
        email = "shariful@test.com"
        password = '123$%^qwer'
        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))

        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_dashboard_user)
        self.assertTrue(user.is_superuser)
