from django.db import models
class Squirrel(models.Model):
   Latitude = models.CharField(
           max_length=100,
           help_text='latitude of location of the squirrel',
           blank=False,
           )
   Longitude = models.CharField(
           max_length=100,
           help_text='longitude of location of the squirrel',
           blank=False,
           )
   Unique_Squirrel_ID = models.CharField(
           max_length=100,
           help_text='Unique Squirrel ID',
           unique=True,
           blank = False,
           )
   Shift = models.CharField(
           max_length=100,
           help_text='AM or PM',
           blank=True,
           )
   Date = models.CharField(
           max_length=100,
           help_text='Date',
           blank=True,
           )
   Age = models.CharField(
           max_length=100,
           help_text='age of the squirrel',
           blank=True,
           )
# Create your models here.
