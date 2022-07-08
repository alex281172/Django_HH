from .models import Cities, Skills
from .serializer import CitiesSerializer, SkillsSerializer
from rest_framework import viewsets


class CitiesViewSet(viewsets.ModelViewSet):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer


class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer