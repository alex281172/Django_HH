from django.core.management.base import BaseCommand
from django.conf import settings
import os
from parserhhapp.models import Cities, Skills

class Command(BaseCommand):

    def handle(self, *args, **options):

        print('Hello')

