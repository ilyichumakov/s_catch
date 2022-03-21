from django.core.exceptions import ValidationError
from django.db import models

from common import AutoDateModel


class Project(AutoDateModel):
    human_name = models.CharField("Наименование", max_length=100, unique=True)
    system_name = models.CharField("Системное имя", max_length=100, unique=True)
    description = models.TextField("Описание", max_length=2000, null=True, blank=True)
    base_url = models.CharField("URL проекта", max_length=200, unique=True)

    def __str__(self):
        return f"Проект {self.human_name}"

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class EndPointGroup(AutoDateModel):
    human_name = models.CharField("Наименование", max_length=100, unique=True)
    system_name = models.CharField("Системное имя", max_length=100, unique=True)
    description = models.TextField("Описание", max_length=2000, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)

    def __str__(self):
        return f"Каталог {self.human_name}"

    class Meta:
        verbose_name = "Каталог эндпоинтов"
        verbose_name_plural = "Каталоги эндпоинтов"


class Method(models.Model):
    METHOD_GET = 'GET'
    METHOD_POST = 'POST'
    METHOD_PUT = 'PUT'
    METHOD_PATCH = 'PATCH'
    METHOD_DELETE = 'DELETE'

    method_name = models.CharField("Имя метода", max_length=10)

    def __str__(self):
        return self.method_name

    class Meta:
        verbose_name = "Метод запроса"
        verbose_name_plural = "Методы запроса"


class EndPoint(AutoDateModel):
    name = models.CharField("Наименование", max_length=100)
    url = models.CharField("URL", max_length=200)
    description = models.TextField("Описание", max_length=2000, null=True, blank=True)
    allowed_methods = models.ManyToManyField(Method, verbose_name="Разрешенные методы")
    payload = models.TextField("Описание формата ответа", max_length=10000, null=True, blank=True)
    group = models.ForeignKey(EndPointGroup, on_delete=models.PROTECT)

    def __str__(self):
        return f"Эндпоинт {self.name}"

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.pk:
            if EndPoint.objects.filter(url=self.url, group__project_id=self.group.project_id).exists():
                raise ValidationError("Such endpoint is already exist in this project")
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        verbose_name = "Эндпоинт"
        verbose_name_plural = "Эндпоинты"
