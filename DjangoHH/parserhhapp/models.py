from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.utils.functional import cached_property


class Skills(models.Model):
    name = models.CharField(max_length=30, verbose_name = 'навык')
    percent = models.CharField(max_length=30, verbose_name = 'доля')
    count = models.CharField(max_length=30, null=True, verbose_name = 'количество')

    class Meta:
        verbose_name = 'skill'
        verbose_name_plural = 'skills'

    @cached_property
    def skills_all_cached(self):
        skills_cached = Skills.objects.all()
        return skills_cached


    def __str__(self):
        return self.name

    def has_name(self):
        return self.name is None

    def has_percent(self):
        return self.percent is None

    def has_count(self):
        return self.count is None

    def some_method(self):
        return 'test'

    def __str__(self):
        return f'{self.name}, {self.percent}, {self.count}'




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

    def has_name(self):
        return self.name is None

    def has_percent(self):
        return self.percent is None

    def has_count(self):
        return self.count is None

    def has_image(self):
        return bool(self.image)

    def __str__(self):
        return f'{self.name}, {self.percent}, {self.count}'