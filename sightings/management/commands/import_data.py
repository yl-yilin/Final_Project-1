#method to import data from csv file

import csv
from django.core.management.base import BaseCommand
from sightings.models import Squirrel
class Command(BaseCommand):
   help = 'Get squirrel data into squirrel'
   def add_arguments(self,parser):
       parser.add_argument('squirrel_file', help='file containing squirrel project')
   def handle(self,*args,**options):
       file_ = options['squirrel_file']
       with open(file_) as fp:
           reader = csv.DictReader(fp)
           id_list = list()
           for item in reader:
               if item['Unique Squirrel ID']not in id_list:
                   squirrel = Squirrel()
                   squirrel.Latitude = float(item['X']),
                   squirrel.Longitude = float(item['Y']),
                   squirrel.Unique_Squirrel_ID = item['Unique Squirrel ID']
                   squirrel.Shift = item['Shift']
                   squirrel.Date = item['Date']
                   squirrel.Age = item['Age']
                   id_list.append(item['Unique Squirrel ID'])
                   squirrel.save()
               else:
                   continue
       msg = f'Importing from {file_}'
       self.stdout.write(self.style.SUCCESS(msg))
