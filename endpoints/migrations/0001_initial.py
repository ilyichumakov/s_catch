# Generated by Django 4.0 on 2022-03-20 21:58

from django.db import migrations, models
import django.db.models.deletion


def insert_methods(apps, schema_editor):
    from endpoints.models import Method

    all_methods = [
        Method.METHOD_GET,
        Method.METHOD_POST,
        Method.METHOD_PUT,
        Method.METHOD_PATCH,
        Method.METHOD_DELETE,
    ]
    for method in all_methods:
        Method.objects.create(method_name=method)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Method',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method_name', models.CharField(max_length=10, verbose_name='Имя метода')),
            ],
            options={
                'verbose_name': 'Метод запроса',
                'verbose_name_plural': 'Методы запроса',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('dt_updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('human_name', models.CharField(max_length=100, unique=True, verbose_name='Наименование')),
                ('system_name', models.CharField(max_length=100, unique=True, verbose_name='Системное имя')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Описание')),
                ('base_url', models.CharField(max_length=200, unique=True, verbose_name='URL проекта')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='EndPointGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('dt_updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('human_name', models.CharField(max_length=100, unique=True, verbose_name='Наименование')),
                ('system_name', models.CharField(max_length=100, unique=True, verbose_name='Системное имя')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Описание')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='endpoints.project')),
            ],
            options={
                'verbose_name': 'Каталог эндпоинтов',
                'verbose_name_plural': 'Каталоги эндпоинтов',
            },
        ),
        migrations.CreateModel(
            name='EndPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('dt_updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('url', models.CharField(max_length=200, verbose_name='URL')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Описание')),
                ('payload', models.TextField(blank=True, max_length=10000, null=True, verbose_name='Описание формата ответа')),
                ('allowed_methods', models.ManyToManyField(to='endpoints.Method', verbose_name='Разрешенные методы')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='endpoints.endpointgroup')),
            ],
            options={
                'verbose_name': 'Эндпоинт',
                'verbose_name_plural': 'Эндпоинты',
            },
        ),
        migrations.RunPython(insert_methods),
    ]
