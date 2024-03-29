from django.urls import path, include
from .models import Cities, Skills, CitiesSalary
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class CitiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cities
        fields = ['name', 'percent', 'count', 'url']

class SkillsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skills
        fields = ['name', 'percent', 'count', 'url']

class CitiesSalarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CitiesSalary
        fields = ['name', 'salary', 'percent', 'count', 'url']