# Generated by Django 4.0.5 on 2022-06-20 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='город')),
                ('percent', models.CharField(max_length=30, verbose_name='доля')),
                ('count', models.CharField(max_length=30, null=True, verbose_name='количество')),
                ('image', models.ImageField(blank=True, null=True, upload_to='coat')),
            ],
            options={
                'verbose_name': 'city',
                'verbose_name_plural': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='навык')),
                ('percent', models.CharField(max_length=30, verbose_name='доля')),
                ('count', models.CharField(max_length=30, null=True, verbose_name='количество')),
            ],
            options={
                'verbose_name': 'skill',
                'verbose_name_plural': 'skills',
            },
        ),
    ]
