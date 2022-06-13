from django.core.management.base import BaseCommand
from parserhhapp.models import Cities, Skills

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Hello')

