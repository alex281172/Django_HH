from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Skills(models.Model):
    name = models.CharField(max_length=30, verbose_name = 'навык')
    percent = models.CharField(max_length=30, verbose_name = 'доля')
    count = models.CharField(max_length=30, null=True, verbose_name = 'количество')

    class Meta:
        verbose_name = 'skill'
        verbose_name_plural = 'skills'



    def __str__(self):
        return self.name

class Cities(models.Model):
    name = models.CharField(max_length=30, verbose_name = 'город')
    percent = models.CharField(max_length=30, verbose_name = 'доля')
    count = models.CharField(max_length=30, null=True, verbose_name = 'количество')
    image = models.ImageField(upload_to='coat', null=True, blank=True)

    class Meta:
        verbose_name = 'city'
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name

