from django.db import models


class AutoDateModel(models.Model):
    dt_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    dt_updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        abstract = True
