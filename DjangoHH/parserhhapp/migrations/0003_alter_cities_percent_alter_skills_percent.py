# Generated by Django 4.0.5 on 2022-06-13 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parserhhapp', '0002_cities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cities',
            name='percent',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='skills',
            name='percent',
            field=models.CharField(max_length=30),
        ),
    ]
