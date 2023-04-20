# Django
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    User
)
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


# class ClientManager(BaseUserManager):
#     """ClientManager."""

#     def create_user(
#         self,
#         email: str,
#         password: str
#     ) -> 'Client':

#         if not email:
#             raise ValidationError('Email required')

#         client: 'Client' = self.model(
#             email=self.normalize_email(email),
#             password=password
#         )
#         client.set_password(password)
#         client.save(using=self._db)
#         return client

#     def create_superuser(
#         self,
#         email: str,
#         password: str
#     ) -> 'Client':

#         client: 'Client' = self.model(
#             email=self.normalize_email(email),
#             password=password
#         )
#         client.is_staff = True
#         client.is_superuser = True
#         client.set_password(password)
#         client.save(using=self._db)
#         return client


class Client(User, PermissionsMixin):
    """Client."""

    balance = models.FloatField(
        default=0.0,
        verbose_name='баланс'
    )
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    # objects = ClientManager()

    class Meta:
        ordering = (
            '-date_joined',
        )
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'

