from django.shortcuts import render
from . import models
from django.views import generic


class LocationListView(generic.ListView):
   model = models.Location
   template_name = 'location_list.html'
   context_object_name = 'location'

   def get_queryset(self):
        return self.model.objects.all()

# def location_list_view(request):
#     if request.method == 'GET':
#         location = models.Location.objects.all()
#     return render(request, 'location_list.html', {'location': location})

