from django.db import models

# Create your models here.

class Skills(models.Model):
    name = models.CharField(max_length=30)
    percent = models.CharField(max_length=30)
    count = models.CharField(max_length=30, null=True)


    def __str__(self):
        return self.name

class Cities(models.Model):
    name = models.CharField(max_length=30)
    percent = models.CharField(max_length=30)
    count = models.CharField(max_length=30, null=True)


    def __str__(self):
        return self.name

