from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class UserAdminTests(TestCase):
    def setUp(self):
        """
        pre set up admin page to run the test cases
        """
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username='admin@gmail.com',
            password='testpassword',
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            username='testadmin@gmail.com',
            password='testpassword',
        )

    def test_user_listed(self):
        """
        test the user listed on the user list page
        """
        url = reverse('admin:user_user_changelist')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertContains(res, self.user.username)

    def test_user_change_page(self):
        """
        Test user change page

        """
        url = reverse('admin:user_user_change', args=[self.user.id]) # /admin/user/user/1/change
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertContains(res, self.user.username)

    def test_user_create_page(self):
        """
        Test user create/add page
        """
        url = reverse('admin:user_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)





