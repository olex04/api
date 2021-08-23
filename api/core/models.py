from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extras):
        """Cria user"""
        if not email:
            raise ValueError('Indique o Email')
        user = self.model(email=self.normalize_email(email), **extras)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_adminuser(self, email, password):
        """Cria e guarda a conta Admin"""
        user = self.create_user(email,password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Adiciona email ao user"""
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    object = UserManager()

    USERNAME_FIELD = 'email'




