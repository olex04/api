from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_successful(self):
        email = 'teste123@gmail.com'
        password = 'teste123'
        role = 'interviewer'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            role=role
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.check_password(password))

    def new_user_email(self):
        """Teste para o novo email"""
        email = 'teste123@gmail.com'
        user = get_user_model().objects.create_user(email, 'teste123', 'teste123')
        self.assertEqual(user.email, email.lower())

    def new_user_invalid_email(self):
        """Testes para user com email invalido"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'teste123','teste123')

    def create_admin_user(self):
        user = get_user_model().objects.create_adminuser(
            "teste321@gmail.com",
            "teste321"
        )
        self.assertTrue(user.is_admin)
