from django.shortcuts import render
from . import models

def location_list_view(request):
    if request.method == 'GET':
        location = models.Location.objects.all()
    return render(request, 'location_list.html', {'location': location})

