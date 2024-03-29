from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.utils.functional import cached_property


class Skills(models.Model):
    name = models.TextField(max_length=300, verbose_name = 'навык')
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
    name = models.TextField(max_length=300, verbose_name = 'город')
    percent = models.CharField(max_length=30, verbose_name = 'доля')
    count = models.CharField(max_length=30, null=True, verbose_name = 'количество')
    image = models.ImageField(upload_to='coat', null=True, blank=True, max_length=500)


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


class CitiesSalary(models.Model):
    name = models.TextField(max_length=300, verbose_name = 'город')
    percent = models.CharField(max_length=30, verbose_name = 'доля')
    count = models.CharField(max_length=30, null=True, verbose_name = 'количество')
    salary = models.CharField(max_length=300, verbose_name='зарплата')


    class Meta:
        verbose_name = 'city_salary'
        verbose_name_plural = 'city_salaries'


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
        return f'{self.name}, {self.percent}, {self.count} {self.salary}'


class SkillCloud(models.Model):
    # title = models.CharField(max_length=150)
    cover = models.ImageField(upload_to='images/')
    book = models.ImageField(upload_to='books/')

    # def __str__(self):
    #     return self.title
    class Meta:
        verbose_name = 'skill_cloud'
        verbose_name_plural = 'skill_clouds'
