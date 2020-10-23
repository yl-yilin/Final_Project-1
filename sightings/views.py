
from django.shortcuts import render

from .models import Squirrel
from .forms import SquirrelForm


from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from django.db.models import Avg, Max, Min, Count


# Create your views here.
def list_of_squirrels(request):
   list_squirrels = Squirrel.objects.all()
   context = {'squirrels': list_squirrels}
   return render(request, 'sightings/list_squirrel.html', context)

def add(request):
       if request.method=='Post':
               form = SquirrelForm(request.POST)
               if form.is_valid():
                       form.save()
                       return redirect(f'/sightings/')
       else:
               form = SquirrelForm()
       context ={
               'form':form
                       }
       return render(request, 'sightings/add.html', context)
def squirrel_id(request, squirrel_id):
    squirrel = get_object_or_404(Squirrel, Unique_Squirrel_ID=squirrel_id)
    if request.method=='Post':
        form = SquirrelForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{squirrel_id}')
    else:
        form = SquirrelForm(instance=squirrel)
    context ={'form':form}
    return render(request, 'sightings/squirrel_id.html', context)

def stats(request):
    squirrels = Squirrel.objects.all()
    total = len(squirrels)
    lattitude = squirrels.aggregate(minimum=Min('Latitude'),maximum=Max('Latitude'))
    longitude = squirrels.aggregate(minimum=Min('Longitude'),maximum=Max('Longitude'))
    age = squirrels.aggregate(minimum=Min('Age'),maximum=Max('Age'))
    shift = list(squirrels.values_list('Shift').annotate(Count('Shift')))
    context = {'total': total,
               'lattitude': lattitude,
               'longitude': longitude,
               'age': age,
               'shift': shift
              }
    return render(request, 'sightings/stats.html', context)

# Create your views here.
