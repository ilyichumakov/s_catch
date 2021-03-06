# Generated by Django 3.2.12 on 2022-04-25 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpointgroup',
            name='human_name',
            field=models.CharField(max_length=100, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='endpointgroup',
            name='system_name',
            field=models.CharField(max_length=100, verbose_name='Системное имя'),
        ),
        migrations.AlterUniqueTogether(
            name='endpointgroup',
            unique_together={('project', 'human_name'), ('project', 'system_name')},
        ),
    ]
