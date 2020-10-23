#exporting data

from django.core.management.base import BaseCommand, CommandError
from sightings.models import Squirrel
from django.apps import apps
import csv

class Command(BaseCommand):
    help = 'exports all information to csv files'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):
        with open(kwargs['path'], 'w', newline='') as csvfile:
            attributes = ['Latitude',
            			'Longitude',
            			'Unique_Squirrel_ID',
            			'Shift',
            			'Date',
            			'Age']
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            writer.writerow(attributes)
            for row in Squirrel.objects.all():
                writer.writerow([getattr(row, attribute) for attribute in attributes])
