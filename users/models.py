from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRoles:
    USER = 'user'
    SUPPORT = 'support'
    choices = (
        (USER, "Пользователь"),
        (SUPPORT, "Саппорт"),
    )


class User(AbstractUser):
    role = models.CharField(choices=UserRoles.choices, default='user', max_length=12)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.first_name}{self.last_name}"
