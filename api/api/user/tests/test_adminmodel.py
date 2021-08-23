from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client

"""
class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='teste123@gmail.com',
            password='teste123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='teste123Dev@gmail.com',
            password='teste123',
            name='UserTesteAdmin',
        )

    def test_users_listed(self):
        """"Testa os users""""
        url = reverse('admin:core_user_changelist')
        rest = self.client.get(url)

        self.assertContains(rest, self.user.name)
        self.assertContains(rest, self.user.email)

    def test_users_next_page(self):
        """"Testa os users"""""
        url = reverse('admin:core_user_changelist', args=[self.user.id])
        rest = self.client.get(url)

        self.assertEqual(rest.status_code, 200)

"""