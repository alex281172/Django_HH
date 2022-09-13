from .models import Cities, Skills, CitiesSalary
from .serializer import CitiesSerializer, SkillsSerializer, CitiesSalarySerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from .permissions import ReadOnly


class CitiesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer


class SkillsViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer


class CitiesSalaryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = CitiesSalary.objects.all()
    serializer_class = CitiesSalarySerializer



