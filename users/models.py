from django.contrib.auth.models import AbstractUser

from common import AutoDateModel


class User(AbstractUser, AutoDateModel):

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
