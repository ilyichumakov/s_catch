from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    dt_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    dt_updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
