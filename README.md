# IEOR E4501 Final Project 
# Squirrel Tracker: A Visualization Web Application for Tracking Squirrels 
## Background 
This is a web appllication project developed with Django, a tool in python, that allow us keep track of all known squirrels. We used a dataset from the **2018 Central Park Squirrel Census**, and visualized the sightings of squirrels by adding, updating, viewing, and analyzing the squirrel data.  

## Dataset
In the project, we import [**2018 Central Park Squirrel Census**](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw) dataset. This is a csv file that included 3024 sightings and 30 variables such as ID, date, age, shift, and so on. 

## Prerequisites
Using Python 3.6+, and undering Django web framwork and Git version control.

## Management Commands 
**Import:** 
A command that can import data from a csv file called 2018 Central Park Squirrel Census. The path should be located after the management commmands in the command line like below.

```sh
python manage.py import_data/path/to/file.csv
```

**Export:**
A command that can export data in a csv format. Again, the path should be located after the management commands in the command line like below.

```sh
python manage.py export_data/path/to/file.csv
```

## API

### Map View
A view that shows a map that displays the location of the squirrel sightings on an OpenStreets map. 

[**Squirrel Map**](https:)

### Squirrel Lists View
A view that lists all squirrel sightings with links to view each sighting 

[**Squirrel Lists**](https:)

### Squirrel Update View 
A view to update a particular sighting 

[**Squirrel Update**](https:)

### Squirrel Create View
A view to create a new sighting 

[**Squirrel Create**](https:)

### Squirrel Stats View 
A view with general stats about the sightings 

[**Squirrel Stats**](https:)

## Dependent Resources
[**Django**](https://www.djangoproject.com/)

[**Django-Leaflet**](https://django-leaflet.readthedocs.io/en/latest/)

## Documentation 
The full description for this project can be found in [**Squirrel Tracker**](https://docs.google.com/document/d/1SPv3fMDKiemrR86rD-S9ecvI2npz3PljDzwCfxK2x5g/edit)

## Contributors 
**Group Name:** Yilin & Savannah 

**Section:** 3 

**Contributors:** Yilin Liu, Savannah Wang 

**UNIs:** **[yl4585, rw2840]**

**Link:** For more information, please go to this [**Project**]() to see our application web page.
